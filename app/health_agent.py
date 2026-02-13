import streamlit as st
import sys
import os

# Add agent folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'agent')))

from compressor import compress_health_data
from recommender import give_recommendation

st.title("🧠 Personal Health Coach AI")
st.write("Enter your daily health data")

sleep = st.slider("Sleep hours", 0, 10, 6)
steps = st.slider("Steps walked", 0, 10000, 3000)

if st.button("Get Health Advice"):
    data = {
        "sleep": [sleep],
        "steps": [steps]
    }
    
    summary = compress_health_data(data)
    
    st.subheader("Health Summary")
    st.write(summary)
    
    st.subheader("Recommendations")
    give_recommendation(summary)
