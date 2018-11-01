""" 
Helpers that build all of the responses
"""

import re

def get_plaintext(ssml):
    """Convert speech_output with ssml tags and newlines into plain text."""
    regex = re.compile("<.*?>")
    plaintext = re.sub(regex, "", ssml)
    return " ".join(plaintext.split())

def build_speechlet_response(output, reprompt_text, should_end_session, card_title=None, output_type="PlainText"):
    """
    Builds the response object for the output dict. Dict will get interpreted as json.
    Valid output types are: "PlainText", "SSML"
    Very clunky, could probably be improved
    """
    
    json_output = {
        'outputSpeech': {
            'type': output_type,
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': output_type,
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    
    if card_title:
        json_output["card"] = {
            'type': 'Simple',
            'title': card_title,
            'content': get_plaintext(output)
        }
    
    if output_type == "SSML":
        del json_output["outputSpeech"]["text"]
        del json_output["reprompt"]["outputSpeech"]["text"]

        json_output["outputSpeech"]["ssml"] = output
        json_output["reprompt"]["outputSpeech"]["ssml"] = reprompt_text   
    
    return json_output



def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

