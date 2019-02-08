#!/usr/bin/env python
# coding: utf-8


import psycopg2 as pg2
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import seaborn as sns
import matplotlib.pyplot as plt
from googletrans import Translator
import numpy as np
from IPython.display import Image, display,HTML
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

Top5_Overall = df.sort_values('num_subscribers', ascending = False)[:5]
Top5_Business = df[df['category'] == 'Business'].sort_values('num_subscribers', ascending = False)[:5]
Top5_Development = df[df['category'] == 'Development'].sort_values('num_subscribers', ascending = False)[:5]
Top5_Personal = df[df['category'] == 'Personal_Development'].sort_values('num_subscribers', ascending = False)[:5]
Top5_IT = df[df['category'] == 'IT_&_Software'].sort_values('num_subscribers', ascending = False)[:5]
Top5_Teaching = df[df['category'] == 'Teaching_&_Academics'].sort_values('num_subscribers', ascending = False)[:5]
Top5_Design = df[df['category'] == 'Design'].sort_values('num_subscribers', ascending = False)[:5]
Top5_Marketing = df[df['category'] == 'Marketing'].sort_values('num_subscribers', ascending = False)[:5]
Top5_Health = df[df['category'] == 'Health_&_Fitness'].sort_values('num_subscribers', ascending = False)[:5]
Top5_Office = df[df['category'] == 'Office_Productivity'].sort_values('num_subscribers', ascending = False)[:5]
Top5_Lifestyle = df[df['category'] == 'Lifestyle'].sort_values('num_subscribers', ascending = False)[:5]
Top5_Music = df[df['category'] == 'Music'].sort_values('num_subscribers', ascending = False)[:5]
Top5_Photography = df[df['category'] == 'Photography'].sort_values('num_subscribers', ascending = False)[:5]
  