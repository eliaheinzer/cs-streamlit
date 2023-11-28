import streamlit as st
import requests
from api import get_question
import random


st.set_page_config(page_title="TRIVIA HERO", page_icon=":blue_heart:", layout="wide")

st.title("Welcome to TRIVIA HERO")
st.header ("A fun game to expand your knowledge")


st.session_state['category'] = st.selectbox("Pick a category:", ["9", "10", "11"], index=0, key='category_select')
st.session_state['difficulty'] = st.selectbox("Pick a difficulty:", ["easy", "medium", "hard"], index=0, key='difficulty_select')


#start_game = st.button("CLICK HERE TO START THE GAME")


#game_over = #muss noch definiert werden

        # DELETE THIS CODE, JUST FOR TESTING!!!
        # DELETE THIS CODE, JUST FOR TESTING!!!
        # DELETE THIS CODE, JUST FOR TESTING!!!
        # DELETE THIS CODE, JUST FOR TESTING!!!

def fetch_new_question():
    category = st.session_state["category"]
    difficulty = st.session_state["difficulty"]
    api_result = get_question(category, difficulty)
    st.session_state["question"] = api_result[0]
    st.session_state["answers"] = api_result[1] + [api_result[2]]
    st.session_state["correct_answer"] = api_result[2]
    random.shuffle(st.session_state["answers"])
    st.session_state['selected_answer'] = None

def display_question():
    st.subheader(st.session_state["question"])
    for ans in st.session_state["answers"]:
        if st.button(ans, key=ans):
            st.session_state['selected_answer'] = ans
            return True  # A button was clicked
    return False  # No button was clicked

def process_answer():
    if st.session_state['selected_answer'] == st.session_state["correct_answer"]:
        st.write("Correct Answer! Congrats!")
        st.session_state['score'] += 1
    else:
        st.write("Wrong, GAME OVER!")
        st.session_state['lives'] -= 1

    if st.session_state['lives'] <= 0:
        st.write(f"Final Score: {st.session_state['score']}")
        st.session_state['start_game'] = False
    else:
        fetch_new_question()  # Fetch a new question for the next round

# Initialize session state keys
if 'start_game' not in st.session_state:
    st.session_state['start_game'] = False
    st.session_state['category'] = "General Knowledge"
    st.session_state['difficulty'] = "Easy"
    st.session_state['lives'] = 3
    st.session_state['score'] = 0
    st.session_state['selected_answer'] = None

if st.button("Start Game"):
    st.session_state['start_game'] = True
    st.session_state['lives'] = 3
    st.session_state['score'] = 0
    fetch_new_question()

if st.session_state['start_game']:
    if 'question' in st.session_state:
        if display_question():
            process_answer()


        # DELETE THIS CODE, JUST FOR TESTING!!!
        # DELETE THIS CODE, JUST FOR TESTING!!!
        # DELETE THIS CODE, JUST FOR TESTING!!!
        # DELETE THIS CODE, JUST FOR TESTING!!!


            
# if start_game:
#     category = st.session_state["category"]
#     difficulty = st.session_state["difficulty"]
#     lives = 3
#     score = 0
#     #setting the lives and score to the starting values
#     while lives > 0:
#         api_result = get_question(category, difficulty)
#         question = api_result[0]
#         correct_answer = api_result[2]
#         #wrong_answer = #muss noch definiert werden
#         answers = api_result[1]
#         answers.append(correct_answer)


#         st.subheader(question)
        
#         random.shuffle(answers)

#         if 'selected_answer' not in st.session_state:
#             st.session_state['selected_answer'] = None

#         for ans in answers:
#             if st.button(ans, key=ans):
#                 st.session_state['selected_answer'] = ans
#                 # Break after a button is clicked

#         #mehrere Probleme: streamlit führt die seite jeweils neu aus nachdem etwas geklickt wird. (machbar aber kompliziert mit session_state
#                         #hauptproblem: sobald ein knopf gedrückt wird wird nicht wie geplant etwas angezeigt sondern das spiel wird zurück gesetzt. 
                        
        
#         if st.session_state['selected_answer'] is not None:  
#             if st.session_state['selected_answer'] == correct_answer:
#                 st.write("Correct Answer! Congrats!")

#             else:
#                 st.write("Wrong, GAME OVER!")

