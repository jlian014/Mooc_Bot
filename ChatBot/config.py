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

SLACK_BOT_TOKEN='xoxb-522150663810-528835316439-tpB1awf6K72lCCmVjN28EiWr'
SLACK_VERIFICATION_TOKEN='DQJpML1oPDMep1MkI6txDBeC' 

# instantiate Slack client
slack_client = SlackClient(SLACK_BOT_TOKEN) # do not change this parameter

###################################################################
######## Watson service configuration   ##########################
###################################################################

service = watson_developer_cloud.AssistantV1(
    iam_apikey = '14oGuiHlj-84TIyuzRBfgOKpNWKYfQipWF2JxDmXSWjS', # replace with Password
    version = '2018-09-20'
)

workspace_id = 'd4e954b4-28ac-41bb-82f9-fee4c2aa7c5a' # replace with Assistant ID
