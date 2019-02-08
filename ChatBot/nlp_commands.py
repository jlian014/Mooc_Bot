###################################################################
######## NLP analysis   ###########################################
###################################################################

"""

    nlp_commands.py
    
    This file handles three things,
    
    1. IBM watson api calls
    2. Custom NLP functions (nlp_solutions)
    3. Talk to backend system to retrieve data
    
    Once all the processing is completed, it sends the output back to main program.

"""

import os,sys
sys.path.append(os.path.normpath(os.getcwd()))
import random
from config import service, workspace_id
from chatbot_functions import *
import pandas as pd
from slack_commands import top_five,slack_tiles,loading
from Recommender import *

def handle_command(message, channel, message_user, context):
    """
        NLP analysis on top of the conversation
    """
    current_action = '' # Intialize current action to empty
    slack_output = ''   # Intialize Slack output to empty
    
  # Send message to Assistant service.
    response = service.message(
    workspace_id = workspace_id,
    input = {'text': message},
    context = context).get_result()
       
    try:
        slack_output = ''.join(response['output']['text'])
    except:
        slack_output = ''
      
    try:
        if response['context']['currentIntent'] == "recommend_moocs":
            search_term = str(response['context']['course_obj']) 
            loading(channel)
            print(search_term)
            mooc = semantic_search(search_term, df, BASE_VECTORS, scaled_foctor)
            top_five(channel, mooc)
            search_term = ''
    except:
        pass
             
  # Update the stored context with the latest received from the dialog.
    context = response['context']
       
    res = ''
    
    try:
        if response['context']['currentIntent'] == "hello":
            slack_tiles(channel)
    except:
        pass
    try:
        if response['context']['currentIntent'] == "Popular":
            top_five(channel, Top5_Overall)
    except:
        pass    
    try:
        if response['context']['currentIntent'] == "Development":
            top_five(channel, Top5_Development)
    except:
        pass    
    try:
        if response['context']['currentIntent'] == "Business":
            top_five(channel, Top5_Business)
    except:
        pass  
    try:
        if response['context']['currentIntent'] == "Personal":
            top_five(channel, Top5_Personal)
    except:
        pass
    try:
        if response['context']['currentIntent'] == "IT":
            top_five(channel, Top5_IT)
    except:
        pass
    try:
        if response['context']['currentIntent'] == "Teaching":
            top_five(channel, Top5_Teaching)
    except:
        pass
    try:
        if response['context']['currentIntent'] == "Design":
            top_five(channel, Top5_Design)
    except:
        pass    
    try:
        if response['context']['currentIntent'] == "Marketing":
            top_five(channel, Top5_Marketing)
    except:
        pass
    try:
        if response['context']['currentIntent'] == "Health":
            top_five(channel, Top5_Health)
    except:
        pass 
    try:
        if response['context']['currentIntent'] == "Office":
            top_five(channel, Top5_Office)
    except:
        pass 
    try:
        if response['context']['currentIntent'] == "Lifestyle":
            top_five(channel, Top5_Lifestyle)
    except:
        pass 
    try:
        if response['context']['currentIntent'] == "Music":
            top_five(channel, Top5_Music)
    except:
        pass     
    try:
        if response['context']['currentIntent'] == "Photography":
            top_five(channel, Top5_Photogrphy)
    except:
        pass    
   
    return(context,slack_output)