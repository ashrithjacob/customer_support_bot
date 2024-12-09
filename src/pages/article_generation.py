import streamlit as st
import pandas as pd
import helper 

def create_topics(table_formatted: pd.DataFrame) -> pd.DataFrame:
    topics = {
        "no": [],
        "topic": [],
        "article": [],
    }
    for idx, row in table_formatted.iterrows():
        if row["status"] == "No Article Found" and row["topic"].lower() != "unclear":
            topics["no"].append(row["no"])
            topics["topic"].append(row["topic"])
            article = helper.generate_article(row["description"], topics)
            topics["article"].append(article)
    topics_df = pd.DataFrame(topics)
    return topics_df


st.write("Creating topics....")
topics_df = create_topics(st.session_state["table"])
st.table(topics_df)

