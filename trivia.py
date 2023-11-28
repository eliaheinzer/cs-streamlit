import streamlit as st
import requests
from api import get_question


st.set_page_config(page_title="TRIVIA HERO", page_icon=":blue_heart:", layout="wide")

st.title("Welcome to TRIVIA HERO")
st.header ("A fun game to expand your knowledge")


st.session_state['category'] = st.selectbox("Pick a category:", ["9", "10", "11"], index=0, key='category_select')
st.session_state['difficulty'] = st.selectbox("Pick a difficulty:", ["easy", "medium", "hard"], index=0, key='difficulty_select')


start_game = st.button("CLICK HERE TO START THE GAME")
game_over = #muss noch definiert werden

if start_game:
    category = st.session_state["category"]
    difficulty = st.session_state["difficulty"]
    lives = 3
    score = 0
    #setting the lives and score to the starting values
    
    api_result = get_question(category, difficulty)
    question = api_result[0]
    correct_answer = api_result[2]
    wrong_answer = #muss noch definiert werden
    answers = api_result[1]
    answers.append(correct_answer)


     st.subheader(question)
    
    random.shuffle(answers)

    if 'selected_answer' not in st.session_state:
        st.session_state['selected_answer'] = None

    for ans in answers:
        if st.button(ans, key=ans):
            st.session_state['selected_answer'] = ans
            break  # Break after a button is clicked

    #mehrere Probleme: streamlit führt die seite jeweils neu aus nachdem etwas geklickt wird. (machbar aber kompliziert mit session_state
                    #hauptproblem: sobald ein knopf gedrückt wird wird nicht wie geplant etwas angezeigt sondern das spiel wird zurück gesetzt. 
                    
    
    if st.session_state['selected_answer'] is not None:  
        if st.session_state['selected_answer'] == correct_answer:
            st.write("Correct Answer! Congrats!")
        else:
            st.write("Wrong, GAME OVER!")


if correct_answer:
    score += 1

if wrong_answer:
    lives -= 1

if lives = 0:
    game_over
