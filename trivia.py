import streamlit as st
import requests
from api import get_question


st.set_page_config(page_title="TRIVIA HERO", page_icon=":blue_heart:", layout="wide")

st.title("Welcome to TRIVIA HERO")
st.header ("A fun game to expand your knowledge")


st.session_state['category'] = st.selectbox("Pick a category:", ["9", "10", "11"], index=0, key='category_select')
st.session_state['difficulty'] = st.selectbox("Pick a difficulty:", ["easy", "medium", "hard"], index=0, key='difficulty_select')


start_game = st.button("CLICK HERE TO START THE GAME")

if start_game:
    category = st.session_state["category"]
    difficulty = st.session_state["difficulty"]

    api_result = get_question(category, difficulty)
    question = api_result[0]
    correct_answer = api_result[2]
    answers = api_result[1]
    answers.append(correct_answer)
