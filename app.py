import streamlit as st
import pandas as pd
import json
import helper
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
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
        st.write(f"new table #{idx}:{json.dumps(table_new, indent=2)}")
        runner.combine_tables(table_new)

    st.write("combined table:", json.dumps(runner.combined_table, indent=2))
