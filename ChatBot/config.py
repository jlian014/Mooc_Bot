###################################################################
######## Configuration files for Bot   ##########################
###################################################################

"""
    config.py 
    
    This files has all the configurations for your bot.
    
"""

import os
import watson_developer_cloud
from slackclient import SlackClient
###################################################################
######## Slack configuration   ##########################
###################################################################

SLACK_BOT_TOKEN=''
SLACK_VERIFICATION_TOKEN='' 

# instantiate Slack client
slack_client = SlackClient(SLACK_BOT_TOKEN) # do not change this parameter

###################################################################
######## Watson service configuration   ##########################
###################################################################

service = watson_developer_cloud.AssistantV1(
    iam_apikey = '', # replace with Password
    version = '2018-09-20'
)

workspace_id = '' # replace with Assistant ID
