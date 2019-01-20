"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to  my Deals . " \
                    "Here you can find  latest trending deals on flights, hotels,food, " \
                    "movies . You can also find active offers on amazon . " \
                    "Start your search by saying , deals on flights .  "
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red"'''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I can tell you latest deals if you say , " \
                    "deals on hotels or , offers on movies."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying Alexa myDeals . " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))
        
def hotels():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = " Latest Hotel deals"
    speech_output = "Here are the top deals on hotels . " \
                    "On OYO Rooms : Flat Rs. 750 Off on bookings of Rs.2600 & Above .  " \
                    "On  make my trip : Flat 33 % off on bookings of Rs.4000 & above . Extra 10% Airtel cashback . " \
                    "On cleartrip : Upto 30 % cashback on domestic hotels . "  \
                    "On Go ibibo : Buy 1 get 1 night free on domestic hotels ."  \
                    "Come back soon for latest deals on hotels . "
                    
    
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "find latest deals instantly on alexa myDeals." 
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def flights():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Latest deals on Flights"
    speech_output = "Here are the top deals on flights . " \
                    "On make my trip :Upto Rs.1000 off on domestic flights booking .  " \
                    "On Pay tm : Upto Rs.5000 bookings on flight tickets .  " \
                    "On cleartrip : Upto Rs.2,500 instant cashback on round trip domestic flight bookings . " \
                    "On Yatra.com : Upto Rs.1500 off on domestic flight bookings . " \
                    "Come back soon for latest deals on flights . "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text =  "find latest deals every day on alexa myDeals."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def food():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Latest deals on Food"
    speech_output = "Here are the top deals on food . " \
                    "On Food panda : Flat 25% off on first 3 orders . " \
                    "On Domino's : Upto Rs.100 cashback when you pay using Pay tm at Domino's .  " \
                    "On Mcdonalds : Free burger of your choice on order of Rs.350 . " \
                    "On Pizza Hut : Flat 50% Off On 2 Medium Pan Pizza . " \
                    "Come back soon for new deals on food . "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red"'''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "find latest deals every day on alexa myDeals."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def movies():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = " Latest offers on movies"
    speech_output = "Here are the top offers on movie tickets . " \
                    "On Book my show : Flat Rs.75 Off On Movie Snacks . " \
                    "On Book my show : Buy 1 get 1 free on Raazi movie tickets . " \
                    "On Ticket new : Flat Rs.50 off for all new users . " \
                    "On Pay tm : Flat 50 % cashback on first movie tickets (minimum 2 ) . " \
                    "Come back soon for new deals on movies . "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "find latest deals every day on alexa myDeals."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def shopping():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Latest offers on amazon"
    speech_output = "Here are the latest offfers on amazon . " \
                    "Fashion Sale : Minimum 50%  To 80% Off On Top Fashion Brands, Extra 10% ICICI Cash Back . " \
                    "Start your free 1 month Amazon Prime video trial .   " \
                    "Mobile Deals : Upto Rs.10,000 Off Offer with Extra 10% ICICI Cash Back and Exchange Offers . " \
                    "The Electronic Store :Upto 50% Off Deals On Mobile, Laptops & More with Extra 10% ICICI Cash Back . " \
                    "Come back soon for new offers on amazon . "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "find latest deals every day on alexa myDeals . "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

'''
def create_favorite_color_attributes(favorite_color):
    return {"favoriteColor": favorite_color}


def set_color_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Color' in intent['slots']:
        favorite_color = intent['slots']['Color']['value']
        session_attributes = create_favorite_color_attributes(favorite_color)
        speech_output = "I now know your favorite color is " + \
                        favorite_color + \
                        ". You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_color_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "You can say, my favorite color is red."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
'''

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "hotels":
        return hotels()
    elif intent_name == "flights":
        return flights()
    elif intent_name == "movies":
        return movies()
    elif intent_name == "food":
        return food()
    elif intent_name == "shopping":
        return shopping()
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
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
