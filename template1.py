"""
This is a Python template for Alexa to get you building skills quickly.
"""

from __future__ import print_function

from build_response_helpers import build_speechlet_response, build_response

# --------------- Functions that control the skill's behavior ------------------
def get_exapmple_response(intent, session):
    """Example of a simple speech response
    """
    
    # intent["slots"][slotname]
    # session.get("attributes, {}")
    
    card_title = "example"
    
    print("printing intent...")
    print(intent)
    print("printing session...")
    print(session)
    
    # Logic when to say what goes here
    if True:
        speech_output = "test"
        reprompt_text = speech_output
        
        # Use session_attributes to to save for the next func call
        session_attributes = {}  # saved to session["attributes"][attributename]
        should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_welcome_response():
    """ Example of how a welcome response would look like
    """
    
    session_attributes = {}
    card_title = "Welcome"
    
    speech_output = "Welcome to my custom skill template."
    reprompt_text = speech_output
    
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thanks for trying out my Skill. \
                    A 5-star rating would be very much appreciated."
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific 
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass

    
def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "example":
        return get_example_response(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("Incoming request...")
    # print("printing event...")
    # print(event)
    # print("printing context...")
    # print(context)


    # Skill ID

    if (event['session']['application']['applicationId'] !=
            "HERE GOES THE SKILL ID"):
        raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
