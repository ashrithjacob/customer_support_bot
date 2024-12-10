import streamlit as st
import pandas as pd
import helper 

def create_topics(row: dict) -> pd.DataFrame:
    article_row = {
        "no": None,
        "topic": None,
        "article": None,
    }
    if row["status"] == "No Article Found" and row["topic"].lower() != "unclear":
        article_row["no"]=row["no"]
        article_row["topic"]=row["topic"]
        article = helper.generate_article(row["description"], row["topic"])
        article_row["article"] = article
    return article_row



if st.button("Generate missing topics from previous table"):
    rows_new_table = []
    st.write("Creating topics....")
    table_placeholder = st.empty()
    for idx, row in st.session_state["table"].iterrows():
        rows_new_table.append(create_topics(row))
        table_formatted = pd.DataFrame(rows_new_table)
        with table_placeholder.container():
            st.table(table_formatted)

