import os
import openai
import streamlit as st
import logging
import sys

from llama_index import QuestionAnswerPrompt, VectorStoreIndex, SimpleDirectoryReader

# openai_api_key = os.getenv("OPENAI_API_KEY")

st.title("プロンプトテスト用")

# with st.form("chat_input", clear_on_submit=True):
#     a, b = st.columns([5, 1])
#     user_input = a.text_area(
#         label="Your message:",
#         placeholder="質問を入力してください",
#         label_visibility="collapsed",
#         height=300,
#     )
#     b.form_submit_button("送信", use_container_width=True)


# documents = SimpleDirectoryReader(input_dir="./data").load_data()
# index = VectorStoreIndex.from_documents(documents)

# if user_input and openai_api_key:
#     openai.api_key = openai_api_key
#     with st.spinner('考え中...'):
#         query_engine = index.as_query_engine()
#         response = query_engine.query(user_input)
#     for i in response.response.split("。"):
#         st.write(i)
