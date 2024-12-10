import streamlit as st
import pandas as pd
import json
import helper
#from streamlit_autorefresh import st_autorefresh
from io import StringIO

CHUNK_SIZE = 4
st.session_state["status"] = None
uploaded_file = st.file_uploader("Choose a file (only .txt or .csv)" , type={"csv", "txt"})

#if st.table is not None:
#	generate_button = st.button("Generate", key="generate_topics_button")

st.warning('switching to the next page while table is being generated will terminate the process', icon="⚠️")
if st.session_state["status"] == "done":
	st.success("Table has been generated successfully")
else:
	st.subheader("Reading all conversations and generating table....")

table_placeholder = st.empty()
if uploaded_file is not None:
	if helper.PreProcess.is_csv(uploaded_file.name):
		df = pd.read_csv(uploaded_file)
		file_contents = helper.PreProcess.df_to_string(df)
	elif helper.PreProcess.is_txt(uploaded_file.name):
		stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
		file_contents = stringio.read()
	else:
		st.write("Please upload only a .txt or .csv file")

	runner = helper.CombineTables(chunk_size=CHUNK_SIZE, file_contents=file_contents)

	for idx, clump in enumerate(runner.clumps):
		print(f"Processing clump {idx}")
		table_new = runner.get_subtable(clump)
		runner.combine_tables(table_new)
		table_formatted = helper.Display.dict_to_df(runner.combined_table)
		with table_placeholder.container():
			st.table(table_formatted)
	st.session_state["status"] = "done"
	st.session_state["table"] = table_formatted
