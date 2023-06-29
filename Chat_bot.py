import os
import openai
import streamlit as st
from streamlit_chat import message
from llama_index import VectorStoreIndex, SimpleDirectoryReader


openai_api_key = os.getenv("OPENAI_API_KEY")
documents = SimpleDirectoryReader(input_dir="./data").load_data()
index = VectorStoreIndex.from_documents(documents)

st.title("💬 にゃんぽんりんGPT")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "どんな御用でしょうか"}]

with st.form("chat_input", clear_on_submit=True):
    a, b = st.columns([4, 1])
    user_input = a.text_input(
        label="Your message:",
        placeholder="聞きたいことを入力してください",
        label_visibility="collapsed",
    )
    b.form_submit_button("送信", use_container_width=True)

for msg in st.session_state.messages:
    message(msg["content"], is_user=msg["role"] == "user")
    
if user_input and openai_api_key:
    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": user_input})
    message(user_input, is_user=True)
    query_engine = index.as_query_engine()
    print(st.session_state.messages)
    response = query_engine.query(user_input)
    # response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    # msg = response.choices[0].message
    # st.session_state.messages.append(msg)
    st.session_state.messages.append({"role": "assistant", "content": response.response})
    message(response.response)
