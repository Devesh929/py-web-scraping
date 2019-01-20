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
            'title':   title,
            'content':  output
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
    speech_output = "Welcome to  myDeals . " \
                    "Here you can find  latest trending deals on flights, hotels,food, " \
                    "movies . You can also find active offers on amazon . " \
                    "Start your search by saying , deals on flights or deals on amazon .  "
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
                    "On OYO Rooms :  Flat 60% Off on OYO Room Bookings of Minimum Rs. 1000 .  " \
                    "On Fab hotels : Flat Rs. 400 Off on All Fab Hotels  . " \
                    "On Goibibo :  Upto 60% Off on Domestic Hotels  . " \
                    "On Make My Trip : Flat 30% Off on Domestic Hotel Bookings of Minimum Rs. 3000 ." \
                    "On OYO Rooms :Flat 53% Off with 30% OYO Money on Room Bookings .  " \
                    "Come back soon for latest offers on  hotels . "
    
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "find latest deals instantly on alexa myDeals." 
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def flights():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Latest deals on Flights"
    speech_output = "Here are the top deals on flights . " \
                    "On Goibibo :Upto Rs.1000 off on domestic flights booking .  " \
                    "On Make My Trip:  Upto Rs. 800 Instant Discount on Domestic Flights .  " \
                    "On cleartrip :  Upto Rs. 1,500 Cashback on Domestic Flights Above Rs. 1000   . " \
                    "On Pay Pal: Flat 50% Cashback on First Transaction . " \
                    "Come back soon for latest offers on  flights . "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text =  "find latest deals every day on alexa myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def food():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Latest deals on Food"
    speech_output = "Here are the top deals on food . " \
                    "On zomato :  Flat 50% Off on Your First Order   . " \
                    "On Pizza Hut : 50% Off on Any Medium Pan Pizza , Only for Take Away Orders  . " \
                    "On Mcdonalds : Buy 1 McSpicy Chicken Burger and Get the other One Free, only Monday to Thursday  . " \
                    "On Swiggy : Flat 50 % Off on First 5 Swiggy Orders . " \
                    "Come back soon for latest offers on  food . "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red"'''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "find latest deals every day on alexa myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def movies():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = " Latest offers on movies"
    speech_output = "Here are the top offers on movie tickets . " \
                    "On INOX movies : First Movie Ticket Free on INOX App Minimum 2 Tickets . " \
                    "On PVR Cinemas : Upto Rs. 200 Cashback Via PhonePe . " \
                    "On Book My Show : Book Tickets using PayPal and get upto Rs. 300 Cashback . " \
                    "On Ticket 4 u : Book Tickets for Telugu, Tamil, Kannada, Hindi and English Movies at the Best Prices. " \
                    "Come back soon for latest offers on  movies . "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def flipkart():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Latest deals on Flipkart"
    speech_output = "These are the Latest deals on flipkart . " \
                    "Upto 80% Off on Laptops, Cameras and More  . " \
                    "Get the Flipkart Plus Annual Membership at Zero Fee "\
                    "Upto 89% Off on Headphones  . " \
                    "Come back soon for latest deals on amazon . "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))  
        
def amaz():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Latest deals on Amazon"
    speech_output = "These are the Latest deals on Amazon. " \
                    "Amazon Fashion Value Fest: Everything Under Rs. 799  . " \
                    "Upto 35% Off on Mountain Cycles  "\
                    "Babys Bonanza: Upto 50% Off on Baby Products . " \ 
                    "Amazon Exclusive: Mi Band 3 at Rs. 1999 " \
                    "Come back soon for latest deals on amazon . "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
        
def myntra():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Latest deals on Myntra"
    speech_output = "These are the Latest deals on Myntra. " \
                    "Half Price Store: Flat 50% Off on Everything  . " \
                    "Upto Rs. 300 Off on Minimum Purchase of Rs. 999 New User.  "\
                    "Extra 5% Off on Minimum Purchase of Rs. 1,799  . " \ 
                    "Come back soon for latest deals on myntra . "
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
def netflix():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "These are the trending shows on Netflix"
    speech_output = "Trending shows on Netflix you can watch . " \
                    "The Last Kingdom  ." \
                    "House of Cards, I suggest you to binge this first ." \
                    "Daredevil"\
                    "Dead Set" \
                    "The Last Kingdom  ." \
                    "House of Cards ." \
                    "Daredevil"\
                    "Chilling Adventures of Sabrina" \
                    "Maniac."
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
                
def prime():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Trending shows on Amazon Prime"
    speech_output ="Trending shows on Amazon Prime you can watch . " \
                    "Hannibal ." \
                    "The Wire." \
                    "Six feet under, this is awesome I should say"\
                    "Poldark"
                    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
                
def comedy():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "These are the comedy shows you can watch."
    speech_output = "I know these will make you laugh hard . " \
                    "Veep, quite a sarcastic one." \
                    "Frasier." \
                    "Glow"\
                    "Better call Saul"
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
                
def suspense():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Suspense thrillers for you"
    speech_output = "So here are the suspense thrillers for you . " \
                    "Stranger Things" \
                    "Mindhunter, " \
                    "Ozark"\
                    "Black Mirror"
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
                
def classics():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output ="So here are the classic TV shows for you . " \
                    "House of Cards" \
                    "Breaking Bad, this.is.awesome  " \
                    "Master of none"\
                    "Making a murderer"
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
                
def sports():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the sports realted TV shows"
    speech_output = "These are sports realted TV shows for you . " \
                    "The White shadow" \
                    "Coach " \
                    "GLOW, you should watch this art "
                    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
                
        
                
def horror():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output ="Lets get ready to scream. " \
                    "American Horror Story, how can I not mention this." \
                    "Supernatural is also a  good time killer" \
                    "Castlevania" \
                    "Fear the walking dead, wish you a sweet time."
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
                
def scifi():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Sci-fi things for you"
    speech_output ="Lets get into science world with these-. " \
                    "Lost in Space, even you will get lost in this." \
                    "3%" \
                    "Dark Matter" \
                    "Star Trek" \
                    "Altered Carbon "
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
                
        

def rakuten():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Here are the Most related APIs in this category . " \
                    "The Electronic Store : Upto 50% Off Deals On Mobile, Laptops & More with Extra 10% ICICI Cash Back . " \
                    "Come back soon for latest deals on amazon . "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def commerce():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "E mail check invalid or valid  ." \
                    "BIN Lookup." \
                    "Deals and Coupons"\
                    "27 coupons" \
                    "Noodlio Pay Smooth Paytm."
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def communication():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Nexmo Number Insight  ." \
                    "Tele Sign Phone ID ." \
                    "Telesign Score"\
                    "2Factor Authentication - India API Package" \
                    "SMS Gateway."
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def data():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Crunchbase  ." \
                    "Words API." \
                    "Random Famous Quotes."\
                    "Sentiment Analysis." \
                    "Dialex."
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def devices():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "IMEI info  ." \
                    "Jawbone UP ." \
                    "Mashape"\
                    "Open Environment Data Project API Package." \
                    "Ubidots."
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def ecommerce():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "ebay  ." \
                    "Gumroad ." \
                    "Shopify "\
                    "Behance" \
                    "Kite."
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def education():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output ="Here are the Most related APIs in this category  . " \
                    "Numbers  ." \
                    "Random quotes." \
                    "Pro Profs Quiz "\
                    "Instructables" \
                    "Hacker Earth "
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def email():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Send Grid ." \
                    "Mail Chimp ." \
                    "Mail box layer. "\
                    "Amazon SES" \
                    "Email labs."
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def entertainment():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Imgur  ." \
                    "Meme Generator ." \
                    "Hearthstone "\
                    "Love Calculator" \
                    "They Said So."
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def events():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output ="Here are the Most related APIs in this category  . " \
                    "Eventbrite API ." \
                    "Eventful ." \
                    "Ticket master. "
                    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def finance():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Currency Converter  ." \
                    "Digital Currency Tickers ." \
                    "Bank IFSC and MICR ,India API Package. "\
                    "Yahoo Finance." \
                    "Bitcointy ."
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def gaming():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Discord Bot ." \
                    "Guild Wars 2 ." \
                    "Poke . "\
                    "League of Legends ." \
                    "Minecraft ."
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
        
def location():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Telize ." \
                    "Open API 1.2 ." \
                    "Boundaries IO . "\
                    "Redline ZIP Code ." \
                    "IP Info ."
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def logistics():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Lob ." \
                    "Postmates API ." \
                    "Hyper Track . "\
                    "On Fleet" \
                    "Shippo ."
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def machine():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Wit AI " \
                    "Amazon ML" \
                    "Google Safe browsing. "\
                    "Api API" \
                    "Microsoft Content Moderator API Package"
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def mapping():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Zillow " \
                    "Google Geocoding API " \
                    "Google Places. "\
                    "Google timezone API" \
                    "MAPBOX Duration. "
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def media():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output ="Here are the Most related APIs in this category  . " \
                    "Text Analysis . " \
                    "Animetrics Face Recognition " \
                    "Sand Cage" \
                    "Face Recognition and Face Detection API Package. " \
                    "musixmatch. "
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def medical():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output ="Here are the Most related APIs in this category  . " \
                    "Life Expectancy . " \
                    "BMI Calculator " \
                    "Human " \
                    "Ebola Outbreak . " \
                    "23 and Me "
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
        
def search():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Giphy . " \
                    "Geo Ranker " \
                    "Google books " \
                    "Bing Search " \
                    "Microsoft Academic"
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def social():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Pinterest " \
                    "Full contact Enrich " \
                    "Slack " \
                    "Foursquare " \
                    "Botometer Pro "
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def sports():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "He"Here are the Most related APIs in this category  . " \
                    "Cricket live scores . " \
                    "winbot soccer API" \
                    "Premier League Live Scores " \
                    "Football Prediction. " \
                    "Soccer sports Open Data "
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def text:
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Text analytics . " \
                    "Twinword text Analysis. " \
                    "Sentiment Analysis " \
                    "Alchemy Text. " \
                    "Lexalytics. "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def translation():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output ="Here are the Most related APIs in this category  . " \
                    "Translation by Microsoft . " \
                    "Google Translate " \
                    "Language layer " \
                    "Yandex Translate . " \
                    "IBM Watson Language "
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def travel():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output ="Here are the Most related APIs in this category  . " \
                    "Skyscanner Flight Search . " \
                    "webcams.travel " \
                    "World airports" \
                    "Trail API . " \
                    "Zilyo "
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
        
def weather():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Yahoo Weather API" \
                    "Darksky " \
                    "Accu weather " \
                    "Aeris weather. " 
                    
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def visual():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Microsoft computer vision . " \
                    "AWS Recognition " \
                    "clarfi v 2 " \
                    "kairos API " \
                    "Microsost Face API"
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def business():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "company check " \
                    "domainr " \
                    "indeed" \
                    "rapleaf " \
                    "who is lookup. "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def advertising():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Facial detection and facial features API package . " \
                    "Deep social" \
                    "app search " \
                    "Global Hyper Local Events " \
                    "zip info. "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def foo():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Yelp API " \
                    "Recipe Food Nutrition " \
                    "Nutritionix " \
                    "Zomato. " \
                    "Big oven. "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def music():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Last FM" \
                    "Spotify public API " \
                    "iTunes " \
                    "Deezer . " \
                    "Soundcloud "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def payments():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output ="Here are the Most related APIs in this category  . " \
                    "Stripe . " \
                    "Square e commerce " \
                    "Pay pal " \
                    "Blockchain . " \
                    "coinbase. "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
        
def storage():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Google Cloud Storage . " \
                    "Amazon S3 " \
                    "Dropbox " \
                    "Openload . " \
                    "Google Drive. "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def science():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output ="Here are the Most related APIs in this category  . " \
                    "Nasa API . " \
                    "Newton. " \
                    "Strain. " \
                    "Open AQ platform. " \
                    "Breezometer. "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
def sms():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Most related APIs in this category  . " \
                    "Telesign SMS Verify . " \
                    "Nexmo SMS vERIFY. " \
                    "Twilio. " \
                    "Plivo . " \
                    "Twilio Copilot. " 
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        
                                                                                                                                                                                                                                                                                                                                        
def shopping():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Here are the Most related APIs in this category"
    speech_output = "Here are the Here are the Most related APIs in this category . " \
                    "Fashion Sale : Minimum 50%  To 80% Off On Top Fashion Brands, Extra 10% ICICI Cash Back . " \
                    "Start your free 1 month Amazon Prime video trial .   " \
                    "Amazon Coupons: Upto 55% OFF Electronics & Accessories . " \
                    "The Electronic Store : Upto 50% Off Deals On Mobile, Laptops & More with Extra 10% ICICI Cash Back . " \
                    "Come back soon for latest deals on amazon . "
    
    '''speech_output = "Welcome to the Alexa Skills Kit sample. " \
                    "Please tell me your favorite color by saying, " \
                    "my favorite color is red" '''
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Get latest deals instantly on alexa  " \
                    "myDeals."
    should_end_session = True
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
    elif intent_name == "flipkart":
        return flipkart()
    elif intent_name == "amaz":
        return amaz()
    elif intent_name == "myntra":
        return myntra()   
    elif intent_name == "netflix":
        return netflix()
    elif intent_name == "prime":
        return prime()
    elif intent_name == "comedy":
        return comedy() 
    elif intent_name == "suspense":
        return suspense() 
    elif intent_name == "classics":
        return classics()    
    elif intent_name == "horror":
        return horror()  
    elif intent_name == "scifi":
        return scifi() 
     elif intent_name == "rakuten":
        return rakuten()   
    elif intent_name == "commerce":
        return commerce()
    elif intent_name == "communication":
        return communication()
    elif intent_name == "data":
        return data()
    elif intent_name == "devices":
        return devices()
    elif intent_name == "ecommerce":
        return ecommerce()
    elif intent_name == "education":
        return education()
    elif intent_name == "email":
        return email()
    elif intent_name == "entertainment":
        return entertainment()
    elif intent_name == "events":
        return events()
    elif intent_name == "finance":
        return finance()
    elif intent_name == "gaming":
        return gaming()
    elif intent_name == "location":
        return location()
    elif intent_name == "logistics":
        return logistics()
    elif intent_name == "machine":
        return machine()
    elif intent_name == "mapping":
        return mapping()
    elif intent_name == "media":
        return media()  
    elif intent_name == "medical":
        return medical()
    elif intent_name == "search":
        return search()
    elif intent_name == "social":
        return social()
    elif intent_name == "sports":
        return sports()    
    elif intent_name == "text":
        return text()
    elif intent_name == "translation":
        return translation()
    elif intent_name == "travel":
        return travel()
    elif intent_name == "weather":
        return weather()
    elif intent_name == "visual":
        return visual()
    elif intent_name == "business":
        return business()
    elif intent_name == "advertising":
        return advertising()
    elif intent_name == "foo":
        return foo()
    elif intent_name == "music":
        return music()   
    elif intent_name == "payments":
        return payments()
    elif intent_name == "storage":
        return storage()
    elif intent_name == "science":
        return science()
    elif intent_name == "sms":
        return sms()    
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
