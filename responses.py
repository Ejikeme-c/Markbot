import random

greating = 'Hello'

bot_name = 'You can call me Mark'

description = 'I am a very low level chat bot that has predefined responses'

feeling = 'As a chat bot i have no feelings, what about you?'


def unknown():
    response = ['I dont understand',
                'I do not have a response for that yet', 'try asking me something different'][random.randrange(3)]
    
    return response