###########################################################
######## Slack Interface codes   ##########################
###########################################################

"""
    slack_commands.py
    
    This file contains all the slack related processing commands.     

"""

import os
import time
import re
from slackclient import SlackClient
from config import slack_client
import datetime

MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events,bot_id):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == bot_id:
                message_user = event['user']
                team = event['team']
                channel = event['channel']
                start_timestamp = datetime.datetime.fromtimestamp(float(event['event_ts'])).strftime('%Y-%m-%d %H:%M:%S')
                return user_id,message_user,message,team,channel,start_timestamp
    return None, None, None, None, None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def output_command(channel,slack_output):
    
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=slack_output
    )


def loading(channel):
    attachments_json = [
        {
            "fallback": "No course inforamtion.",
            "color": "#36a64f",
            "pretext": "MOOC recommender system ",
            "author_name": "Udemy online courses",
            "author_link": "http://Udemy.com",
            "author_icon": 'https://about.udemy.com/wp-content/uploads/2017/10/NewUlogo-large-1.png',                 "image_url": 'https://i.pinimg.com/originals/12/50/89/125089ee636b8eaafa296cc62fe21a9f.gif'   
        }
    ]
    slack_client.api_call(
      "chat.postMessage",
      channel=channel,
      text = 'Got it, Mooc Recommender is trying to find the courses that match to your search, it will take a while!, thank you for your patient!',
      attachments=attachments_json
    )     

def slack_tiles(channel):
    attachments_json = [
        {"title": 'Development'},
        {"title": 'Business'},
        {"title": 'IT & Software'},
        {"title": 'Office Productivity'},
        {"title": 'Personal Development'},
        {"title": 'Design'},
        {"title": 'Marketing'},
        {"title": 'Lifestyle'},
        {"title": 'Photography'},
        {"title": 'Health & Fitness'},
        {"title": 'Music'},
        {"title": 'Teaching & Academics'}
        ]
  
    # Send a message with the above attachment, asking the user if they want coffee
    slack_client.api_call(
      "chat.postMessage",
      channel=channel,
      text="Hi, there! I can recommend Udemy online courses!",
      attachments=attachments_json
    )      
        
def top_five(channel,dataframe):
    
    attachments_json = [
        {
            "fallback": "No course inforamtion.",
            "color": "#36a64f",
            "pretext": "MOOC recommender system ",
            "author_name": "Udemy online courses",
            "author_link": "http://Udemy.com",
            "author_icon": 'https://about.udemy.com/wp-content/uploads/2017/10/NewUlogo-large-1.png',
            "title": dataframe['title'].values[0],
            "title_link": 'https://udemy.com' + dataframe['url'].values[0],
            "text": dataframe['headline'].values[0],
             "fields": [
                 {
                     "title": "Course Length",
                     "value": dataframe['content_info'].values[0],
                 },
                 {
                     "title": "Number of Subscribers",
                     "value": str(dataframe['num_subscribers'].values[0]),
                 }                 
             ],
             "image_url": dataframe['image_304x171'].values[0],
             "footer": "MooC Bot",
             "footer_icon" : 'https://cdn.freebiesupply.com/logos/large/2x/slack-logo-icon.png',
             "ts": 123456789
        },
        {
            "fallback": "No course inforamtion.",
            "color": "#36a64f",
            "pretext": "MOOC recommender system ",
            "author_name": "Udemy online courses",
            "author_icon": 'https://about.udemy.com/wp-content/uploads/2017/10/NewUlogo-large-1.png',            
            "author_link": "http://Udemy.com",
            "title": dataframe['title'].values[1],
            "title_link": 'https://udemy.com' + dataframe['url'].values[1],
            "text": dataframe['headline'].values[1],
             "fields": [
                 {
                     "title": "Course Length",
                     "value": dataframe['content_info'].values[1],
                 },
                 {
                     "title": "Number of Subscribers",
                     "value": str(dataframe['num_subscribers'].values[1]),
                 }                 
             ],
             "image_url": dataframe['image_304x171'].values[1],
             "footer": "MooC Bot",
             "footer_icon" : 'https://cdn.freebiesupply.com/logos/large/2x/slack-logo-icon.png',
             "ts": 123456789
        },
        {
            "fallback": "No course inforamtion.",
            "color": "#36a64f",
            "pretext": "MOOC recommender system ",
            "author_name": "Udemy online courses",
            "author_link": "http://Udemy.com",
            "author_icon": 'https://about.udemy.com/wp-content/uploads/2017/10/NewUlogo-large-1.png',            "author_icon": "http://flickr.com/icons/bobby.jpg",
            "title": dataframe['title'].values[2],
            "title_link": 'https://udemy.com' + dataframe['url'].values[2],
            "text": dataframe['headline'].values[2],
             "fields": [
                 {
                     "title": "Course Length",
                     "value": dataframe['content_info'].values[2],
                 },
                 {
                     "title": "Number of Subscribers",
                     "value": str(dataframe['num_subscribers'].values[2]),
                 }                 
             ],
             "image_url": dataframe['image_304x171'].values[2],
             "footer": "MooC Bot",
             "footer_icon" : 'https://cdn.freebiesupply.com/logos/large/2x/slack-logo-icon.png',
             "ts": 123456789
        },
        {
            "fallback": "No course inforamtion.",
            "color": "#36a64f",
            "pretext": "MOOC recommender system ",
            "author_name": "Udemy online courses",
            "author_link": "http://Udemy.com",
            "author_icon": 'https://about.udemy.com/wp-content/uploads/2017/10/NewUlogo-large-1.png',            
            "title": dataframe['title'].values[3],
            "title_link": 'https://udemy.com' + dataframe['url'].values[3],
            "text": dataframe['headline'].values[3],
             "fields": [
                 {
                     "title": "Course Length",
                     "value": dataframe['content_info'].values[3],
                 },
                 {
                     "title": "Number of Subscribers",
                     "value": str(dataframe['num_subscribers'].values[3]),
                 }                 
             ],
             "image_url": dataframe['image_304x171'].values[3],
             "footer": "MooC Bot",
             "footer_icon" : 'https://cdn.freebiesupply.com/logos/large/2x/slack-logo-icon.png',
             "ts": 123456789
        },
        {
            "fallback": "No course inforamtion.",
            "color": "#36a64f",
            "pretext": "MOOC recommender system ",
            "author_name": "Udemy online courses",
            "author_link": "http://Udemy.com",
            "author_icon": 'https://about.udemy.com/wp-content/uploads/2017/10/NewUlogo-large-1.png',            
            "title": dataframe['title'].values[4],
            "title_link": 'https://udemy.com' + dataframe['url'].values[4],
            "text": dataframe['headline'].values[4],
             "fields": [
                 {
                     "title": "Course Length",
                     "value": dataframe['content_info'].values[4],
                 },
                 {
                     "title": "Number of Subscribers",
                     "value": str(dataframe['num_subscribers'].values[4]),
                 }                 
             ],
             "image_url": dataframe['image_304x171'].values[4],
             "footer": "MooC Bot",
             "footer_icon" : 'https://cdn.freebiesupply.com/logos/large/2x/slack-logo-icon.png',
             "ts": 123456789
        }        
    ]
    
    slack_client.api_call(
      "chat.postMessage",
      channel=channel,
      attachments=attachments_json
    )    