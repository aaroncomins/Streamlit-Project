import streamlit as st

import gensim
# from gensim.summarization import summarize  # Optional depending on gensim_sum_ext usage
import gensim_sum_ext
import sumy.parsers
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# EDA Package
import pandas as pd

# Data Visualization
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')

import seaborn as sns

import nltk


def sumy_summarizer(docx, num=2):
    # Assuming NLTK data path is within the virtual environment
    nltk.data.path.append("/Users/aaroncomins/Desktop/UW Jupyter Hub/Streamlit Project/venv/lib/python3.11/site-packages/nltk")  # Adjust path if needed

    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, num)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

# Evaluate Summary
from rouge import Rouge
def evaluate_summary(summary,reference):
    r = Rouge()
    eval_score = r.get_scores(summary,reference)
    eval_score_df = pd.DataFrame(eval_score[0])
    return eval_score_df

def main():
    st.title("Summarizer App")
    menu = ['Home', 'About']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Summarization")
        raw_text = st.text_area("Enter Text Here")
        if st.button("Summarization"):
            with st.expander("Original Text"):
                st.write(raw_text)

            c1, c2 = st.columns(2)

            with c1:
                with st.expander("LexRank Summary"):
                    my_summary = sumy_summarizer(raw_text)
                    st.write(my_summary)
                    st.info("Rouge Score")
                    score = evaluate_summary(my_summary,raw_text)
                    st.dataframe(score.T)
            
            with c2:
                with st.expander("TextRank Summary"):
                    my_summary = sumy_summarizer(raw_text) #this is suppose to be summarize instead of sumy_summarize but unable to get it to work
                    st.write(my_summary)
                    st.info("Rouge Score")
                    score = evaluate_summary(my_summary,raw_text)
                    st.dataframe(score)  

    else:
        st.subheader("About")


if __name__ == "__main__":
    main()

# Bret "The Hitman" Hart, a legendary figure in professional wrestling, carved a distinctive path in the industry with his technical prowess, charisma, and storytelling ability. Hailing from a wrestling family, Hart's career was shaped by a combination of family tradition and his own unique talents.

# Hart's in-ring style was renowned for its technical precision and his ability to tell captivating stories. His matches were often characterized by a slower, more methodical pace, focusing on grappling and submission holds rather than high-flying acrobatics. This style, coupled with his intense facial expressions and storytelling ability, drew fans in and made him a beloved figure in the wrestling world.

# Hart's career reached its pinnacle in the 1990s, during the Monday Night Wars between WWE (then WWF) and WCW. He became the face of WWE, leading the company to victory in the ratings war. His iconic matches, such as the "I Quit" match against Stone Cold Steve Austin at WrestleMania XIII and the controversial "Montreal Screwjob," solidified his legacy as one of the greatest wrestlers of all time.

# Beyond his in-ring accomplishments, Hart is also known for his sharp wit, storytelling ability, and his candid autobiography, "Hitman: My Real Life in the Wrestling Business." His contributions to the world of professional wrestling have earned him a place among the all-time greats, and his legacy continues to inspire fans and wrestlers alike.






