from textblob import TextBlob
import streamlit as st

def correct_spelling(text):
    word=TextBlob(text)
    return word.correct()


st.title("Automatic Spelling Correction")
input=st.text_input("enter your text here...")
button=st.button("click here to correct your words")
if button:
    correct_word=correct_spelling(input)
    st.subheader(str(correct_word))