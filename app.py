import streamlit as st
import pandas as pd
import json
import helper
from streamlit_autorefresh import st_autorefresh
from io import StringIO


uploaded_file = st.file_uploader("Choose a file (only .txt or .csv)" , type={"csv", "txt"})

table_placeholder = st.empty()
if uploaded_file is not None:
	if helper.PreProcess.is_csv(uploaded_file.name):
		df = pd.read_csv(uploaded_file)
		file_contents = helper.PreProcess.df_to_string(df)
	elif helper.PreProcess.is_txt(uploaded_file.name):
		stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
		file_contents = stringio.read()
		st.write(file_contents[:1000])
	else:
		st.write("Please upload only a .txt or .csv file")

	runner = helper.CombineTables(chunk_size=2, file_contents=file_contents)

	for idx, clump in enumerate(runner.clumps):
		table_new = runner.get_subtable(clump)
		runner.combine_tables(table_new)
		table_formatted = helper.Display.dict_to_df(runner.combined_table)
		with table_placeholder.container():
			st.table(table_formatted)
