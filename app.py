import re
import streamlit as st
import pandas as pd

st.title("💊 AI Medical Prescription Extraction")

prescription_text = st.text_area(
    "Paste complete prescription text here:",
    height=300
)

if st.button("Extract Details"):

    if prescription_text.strip() == "":
        st.warning("Please paste the prescription text!")

    else:
        st.success("Prescription received successfully!")
        st.code(prescription_text)