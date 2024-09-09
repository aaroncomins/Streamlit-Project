import streamlit as st

import gensim
# from gensim.summarization import summarize
import gensim_sum_ext
import sumy.parsers
# from sumy.parsers.plantext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# EDA Package
import pandas as pd

# Data Visualization
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')

import seaborn as sns

def main():
    st.title("Summarizer App")
    menu = ['Home', 'About']
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Summarization")
        raw_text = st.text_area("Enter Text Here")
        if st.button("Summarization"):
            with st.expander("Original Text"):
                st.write(raw_text)

            c1, c2 = st.columns(2)

            with c1:
                with st.expander("LexRank Summary"):
                    st.write("LexRank Summary")
            
            with c2:
                with st.expander("TextRank Summary"):
                    st.write("TextRank Summary")

    else:
        st.subheader("About")


if __name__ == "__main__":
    main()