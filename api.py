import requests
import html
#the api gives otherwise weird looking answers


def get_question(category, difficulty):
    
    #if the question type is changed than the answer extraction needs an update
    #the category type is a number not the name
    params ={"amount":1,"category":category,"difficulty":difficulty, "type":"multiple"}
    url ="https://opentdb.com/api.php?"
    api_answer = requests.get(url, params = params)
    
    #unpacking the json
    answer = api_answer.json()
    
    #changing the element in to a readable result
    question_with_html = answer['results'][0]['question']
    question = html.unescape(question_with_html)
    
    wrong_answers_with_html = answer['results'][0]['incorrect_answers']
    wrong_answers = html.unescape(wrong_answers_with_html)
    #This gives a list with the wrong answers
    
    correct_answer_with_html = answer['results'][0]['correct_answer']
    correct_answer = html.unescape(correct_answer_with_html)
    
    #putting all the results in a tuple
    trivia_packet = (question, wrong_answers, correct_answer)
    return trivia_packet
    #example response:('Who painted The Starry Night?',['Pablo Picasso', 'Leonardo da Vinci', 'Michelangelo'],'Vincent van Gogh')

#example call of the function: get_question(25,"easy")