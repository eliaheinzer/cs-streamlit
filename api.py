import requests
import html
#the api gives otherwise weird looking answers


def get_question(difficulty, category):
    #getting 5 questions at the time so the request delay is not a problem
    amount = 5
    trivia_packet = []
    #if the question type is changed than the answer extraction needs an update
    #the category type is a number not the name
    params ={"amount":amount,"difficulty":difficulty, "type":"multiple"}
    
    #giving the possibility that category is none which returns random questions
    if category is not None:
        params["category"] = category
    url ="https://opentdb.com/api.php?"
    api_answer = requests.get(url, params = params)
    
    #unpacking the json
    answer = api_answer.json()
    
    #changing the element in to a readable result and distributing each in a tuple
    for i in range(0,amount):
        question_with_html = answer['results'][i]['question']
        question = html.unescape(question_with_html)
    
        wrong_answers_with_html = answer['results'][i]['incorrect_answers']
        wrong_answers = html.unescape(wrong_answers_with_html)
    #This gives a list with the wrong answers
    
        correct_answer_with_html = answer['results'][i]['correct_answer']
        correct_answer = html.unescape(correct_answer_with_html)
        question_packet= (question, wrong_answers, correct_answer)
        trivia_packet.append(question_packet)
    #putting all the results in a tuple
    
    return trivia_packet
    #example response:('Who painted The Starry Night?',['Pablo Picasso', 'Leonardo da Vinci', 'Michelangelo'],'Vincent van Gogh')

#example call of the function: get_question("easy", 25)