import streamlit as st

def give_recommendation(summary):
    avg_sleep = summary["avg_sleep"]
    avg_steps = summary["avg_steps"]
    
    if avg_sleep < 7:
        st.warning("You should sleep more for better health.")
    else:
        st.success("Great sleep schedule!")
    
    if avg_steps < 5000:
        st.warning("Increase daily walking for better fitness.")
    else:
        st.success("Good physical activity level!")
