import re
import responses as res

#This funtion checks the probability that the user message requires a particular response 
def message_prob(user_message, recognised_words, single_response=False, required_words=[]):
    message_certain = 0
    has_req_words = True

    for words in user_message:
        if words in recognised_words:
            message_certain += 1
    
    prob = float(message_certain)/ float(len(recognised_words))

    for words in required_words:
        if words not in user_message:
            has_req_words = False
            break
    
    if has_req_words or single_response:
        return int(prob*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def resp(bot_resp, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_resp] = message_prob(message, list_of_words, single_response, required_words)

    #Response ------------------------------------------
    resp(res.greating, ['hello', 'hi', 'hey', 'heyyy', 'sup', 'heyo'], single_response=True)
    resp(res.bot_name, ['what', 'is', 'your', 'name'], required_words=['your', 'name'])
    resp(res.feeling, ['how', 'are', 'you', 'doing'], required_words=['how', 'you'])
    resp(res.description, ['what', 'are', 'you'], required_words=['what'])
    resp('Bye', ['bye', 'im', 'done', 'end'], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return res.unknown() if highest_prob_list[best_match] < 1 else best_match


#Creating the function that will return the responses based on the users input
def get_response(user_input):
    message = re.split(r'\s+|[,;?!.-_]\s*', user_input.lower()) #this splits the input message into an array and remove the symbols in the []
    response = check_all_messages(message)
    return response



while True:
    print('MarkBot: ' + get_response(input('You: ')))
    