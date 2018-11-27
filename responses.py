"""
Class for creating the Alexa responses that the user gets

Set 'SSML=True' for adding the <speak> tag (and reducing the speech rate to 90%)

Make sure to write all of your speech output with this class so that it is 
    easier to translate all of it at the same time

TO DO:
    Make possible to translate

"""

class Response:
    def __init__(self, speech_output, reprompt_text="", SSML=False):
        self.speech_output = speech_output
        self.reprompt_text = reprompt_text
        
        if SSML:
            self.speech_output = "<speak><prosody rate='90%'>" + self.speech_output + "</prosody></speak>"
            self.reprompt_text = "<speak><prosody rate='90%'>" + self.reprompt_text + "</prosody></speak>"




#-------------------------------------------------------------------------------




#-------------------------------------------------------------------------------

all_responses = {"sample": "test"
    
}
