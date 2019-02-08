#!/usr/bin/env python
# coding: utf-8

# In[36]:


import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import nltk
import re
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from rake_nltk import Rake
import psycopg2 as pg2
from sql_table import *

#get_ipython().run_line_magic('run', 'sql_table.py')

def con_cur_to_db(dbname=DBNAME, dict_cur=None):
    ''' 
    Returns both a connection and a cursor object for your database
    '''
    con = pg2.connect(host=IP_ADDRESS,
                  dbname=dbname,
                  user=USER,
                  password=PASSWORD)
    if dict_cur:
        cur = con.cursor(cursor_factory=RealDictCursor)
    else:
        cur = con.cursor()
    
    return con, cur

def execute_query(query, dbname=DBNAME, dict_cur=None, command=False):
    '''
    Executes a query directly to a database, without having to create a cursor and connection each time. 
    '''
    con, cur = con_cur_to_db(dbname, dict_cur)
    cur.execute(f'{query}')
    if not command:
        data = cur.fetchall()
        col_names = []
        for elt in cur.description:
            col_names.append(elt[0])
        con.close()
        return data, col_names
    con.commit()
    con.close()

query = '''
SELECT *
FROM udemy
'''
data, column_names = execute_query(query)


df = pd.DataFrame(data, columns=column_names)


df['headline'] = df['headline'].fillna('No headlines')
df['description'] = df['description'].fillna('No description')

df.reset_index(inplace=True)


df['description']=[re.sub('[^a-zA-Z0-9.#+]', ' ', str(row), flags=re.M|re.I) for row in df['description']]

module_url = "https://tfhub.dev/google/universal-sentence-encoder/2" #@param ["https://tfhub.dev/google/universal-sentence-encoder/2", "https://tfhub.dev/google/universal-sentence-encoder-large/3"]

embed = hub.Module(module_url)

def clean_words(raw_text):       
    letters_only = re.sub("[^a-zA-Z0-9.#+]", " ", raw_text)
    words = letters_only.lower().split()
    stops = set(stopwords.words('english'))
    extra_stops = set(['learn','course'])
    nostop_words = [w for w in words if not w in stops]
    meaningful_words = [w for w in nostop_words if not w in extra_stops]
    lemmatizer = WordNetLemmatizer()
    lem_words = [lemmatizer.lemmatize(w) for w in meaningful_words]
    return(" ".join(lem_words))

def get_features(texts):
    if type(texts) is str:
        texts = [texts]
    tf.logging.set_verbosity(tf.logging.ERROR)
    with tf.Session() as sess:
        sess.run([tf.global_variables_initializer(), tf.tables_initializer()])
        return sess.run(embed(texts))

BASE_VECTORS = get_features(df['objectives_summary'].values)


df['num_subscribers'] = df['num_subscribers'].astype('int64')
df['avg_rating_recent'] = df['avg_rating_recent'].astype('float64')

norm = (df['avg_rating_recent'] * df['num_subscribers'])/(df['num_subscribers']+1000)
scaled_foctor = MinMaxScaler().fit_transform(norm.values.reshape(-1,1))

def semantic_search(query, dataframe, vectors, scale):
    query = clean_words(query)
    print("Extracting features...")
    query_vec = get_features(query)
    sim = cosine_similarity(vectors, query_vec)
    dataframe['scaled_sim'] = sim*scale
    top_5 = df.sort_values('scaled_sim', ascending=False)[:5]
    return top_5





