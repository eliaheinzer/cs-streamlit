import streamlit as st
import requests
from api import get_question
import random

#Page set up and Title

st.set_page_config(page_title="TRIVIA HERO", page_icon=":blue_heart:", layout="wide")

st.markdown("<h1 style='text-align: center; color: orange;'>Welcome to TRIVIA HERO!</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: yellow;'>A fun game to expand your knowledge</h4>", unsafe_allow_html=True)

#player name
player_name = st.text_input("Enter your name:")

if player_name:
    st.write(f"Welcome {player_name}! If you want to listen to music while playing, click this button:")  

    #Music Imput
    audio="music.mp3"
    if st.button("play music"):
        st.audio(audio)
    
#choose a category   

def get_random_categories():
    url = "https://opentdb.com/api_category.php"
    response = requests.get(url)
    categories = response.json()['trivia_categories']
    select_categories = random.sample(categories, 4)

    ## Adding a random category option
    select_categories.append({'id':None, 'name':'Random'})
    return select_categories

if 'start_game' not in st.session_state:
    st.session_state['start_game'] = False

if 'selected_categories' not in st.session_state:
    st.session_state['selected_categories'] = get_random_categories()
    st.session_state['start_game'] = True
    
if 'category' not in st.session_state:
    st.session_state['category'] = None 
           
                
st.session_state ['category'] = st.selectbox("Pick a category:", options=st.session_state['selected_categories'], format_func=lambda x: x['name'], index=0, key='category_select')

if st.session_state['category']:
    st.write(f"You've selected category: {st.session_state['category']['name']}")

st.session_state['difficulty'] = st.selectbox("Pick a difficulty:", ["easy", "medium", "hard"], index=0, key='difficulty_select')

if "highscore" not in st.session_state:
    st.session_state["highscore"] = 0

if 'score' not in st.session_state:
    st.session_state['score']= 0


def get_question_for_random_category(category):
    if category is None:
        random_category = random.choice(st.session_state['selected_categories'])
        category = random_category['id']
                      

def get_new_question():
    category = st.session_state["category"]["id"]
    if category == "Random":
        category = None

    difficulty = st.session_state["difficulty"]

    #importing the results from the api if all the current questions are used
    if st.session_state['question_counter'] == 0:
        st.session_state['api_result'] = get_question(difficulty, category)
        #Informing user about trying again
        if st.session_state['api_result'] == False:
            st.error("You were too fast, try again")
            #stopping game to remove potential bug, if user tries to play with the old displayed question
            st.session_state['start_game'] = False
            return

    #breaking up the results packet
    current_question_packet = st.session_state['api_result'][st.session_state['question_counter']]
    
    st.session_state["question"] = current_question_packet[0]

    #both parts are lists before concatenating
    incorrect_answers = current_question_packet[1]
    correct_answer = current_question_packet[2]

    st.session_state["correct_answer"] = correct_answer

    # Ensure all answers are strings and combine them
    st.session_state["answers"] = [str(answer) for answer in incorrect_answers + [correct_answer]]


    #getting rid of the fixed order
    random.shuffle(st.session_state["answers"])

    st.session_state['selected_answer'] = None

    #Cycling through the 5 questions
    st.session_state['question_counter'] += 1
    if st.session_state['question_counter'] == 5:
        st.session_state['question_counter'] = 0


def display_question():
    st.subheader(st.session_state["question"])
    
    cols = st.columns(4)
    
    #listing out the answers
    for idx, ans in enumerate(st.session_state["answers"]):
        with cols[idx]:
            if st.button(ans, key=ans):
                st.session_state['selected_answer'] = ans
                return True  # A button was clicked
    return False  # No button was clicked, does not check the answer

def process_answer():
    #Check if answer is correct
    if st.session_state['selected_answer'] == st.session_state["correct_answer"]:
        st.success("Correct Answer! Congrats!")
        st.session_state['score'] += 1
        get_new_question()
    #subtract a live if answer is wrong
    else:
        st.session_state['lives'] -= 1
        st.error(f"Wrong, you have {st.session_state['lives']} lives left!")
            #if there are no lives left in this session end this round otherwise restart
        if st.session_state['lives'] <= 0:
            st.write(f"Final Score: {st.session_state['score']}")
            
            

            #Check if a new highscore is achieved and congratulate if done
            if st.session_state['score'] > st.session_state['highscore']:
                st.session_state['highscore'] = st.session_state['score']
                st.write(f"Congratulations you have a new Highscore. Your new Highscore is: {st.session_state['highscore']}")
            st.session_state['score'] = 0
            st.session_state['selected_categories'] = get_random_categories()
            st.session_state['start_game'] = False
        else:
            get_new_question() #get a new question

# Initialize session state keys
if 'start_game' not in st.session_state:
    st.session_state['start_game'] = False
    st.session_state['lives'] = 3
    st.session_state['score'] = 0
    st.session_state['selected_answer'] = None

if st.button("Start Game"):
    #giving the player the starting lives and resetting the score 
    st.session_state['start_game'] = True
    st.session_state['lives'] = 3
    st.session_state['score'] = 0
    st.session_state['question_counter'] = 0
    #get question
    get_new_question()

#actual process of the code starts
if st.session_state['start_game']:
    if 'question' in st.session_state:
        if display_question():
                process_answer()


#Display lives, score and highscore
if 'lives' in st.session_state:
    hearts = st.session_state['lives']
    heart_symbol = '\U00002764'
    st.write(f'{heart_symbol * hearts}')

st.write(f'Your Score: {st.session_state["score"]}')
st.write(f'Your Highscore is: {st.session_state["highscore"]}')
