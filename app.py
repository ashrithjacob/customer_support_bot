import streamlit as st
import pandas as pd
import json
import helper
from streamlit_autorefresh import st_autorefresh
from io import StringIO


uploaded_file = st.file_uploader("Choose a file")

table_placeholder = st.empty()
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    file_contents = stringio.read()

    runner = helper.CombineTables(chunk_size=2, file_contents=file_contents)

    for idx, clump in enumerate(runner.clumps):
        table_new = runner.get_subtable(clump)
        runner.combine_tables(table_new)
        table_formatted = helper.Display.dict_to_df(runner.combined_table)
        with table_placeholder.container():
          st.table(table_formatted)
 