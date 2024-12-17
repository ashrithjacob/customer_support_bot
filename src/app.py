import streamlit as st
import pandas as pd
import json
import helper
#from streamlit_autorefresh import st_autorefresh
from io import StringIO

CHUNK_SIZE = 4
st.session_state["status"] = True
st.session_state["message"] = ""
uploaded_file = st.file_uploader("Choose a file (only .txt or .csv)" , type={"csv", "txt"})


st.warning('switching to the next page while table is being generated will terminate the process', icon="⚠️")

message_holder= st.empty()
def run_message():
		with message_holder.container():
			if st.session_state["status"]:
				st.success(st.session_state["message"])
			else:
				st.error(st.session_state["message"])

table_placeholder = st.empty()
if uploaded_file is not None:
	st.session_state["message"] = "Reading all conversations and generating table...."
	run_message()
	if helper.PreProcess.is_csv(uploaded_file.name):
		df = pd.read_csv(uploaded_file)
		file_contents = helper.PreProcess.df_to_string(df)
	elif helper.PreProcess.is_txt(uploaded_file.name):
		stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
		file_contents = stringio.read()
	else:
		st.write("Please upload only a .txt or .csv file")

	runner = helper.CombineTables(chunk_size=CHUNK_SIZE, file_contents=file_contents)

	run_message()
	try:
		for idx, clump in enumerate(runner.clumps):
			print(f"Processing clump {idx}")
			table_new = runner.get_subtable(clump)
			runner.combine_tables(table_new)
			table_formatted = helper.Display.dict_to_df(runner.combined_table)
			with table_placeholder.container():
				st.table(table_formatted)
		st.session_state["message"] = "Table generated!"
	except Exception as e:
		st.session_state["status"] = False
		st.session_state["message"] = f"Error while generating table: {e}"
	run_message()
	st.session_state["table"] = table_formatted
