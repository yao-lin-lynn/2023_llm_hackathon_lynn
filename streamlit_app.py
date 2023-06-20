import altair as alt
import pandas as pd
import streamlit as st

import openai
import os
import logging
import sys

from llama_index import VectorStoreIndex, SimpleDirectoryReader

openai.api_key = os.getenv("OPENAI_API_KEY")

"""
# ハッカソンやるぞ〜
"""
st.balloons()

documents = SimpleDirectoryReader(input_dir="./data").load_data()
list_index = VectorStoreIndex.from_documents(documents)

txt = st.text_area('質問を入力してください', '''
    今日の天気を教えてください
    ''', height=300)

if st.button('にゃんぽんりんGPTに聞く'):
    with st.spinner('考え中...'):
        query_engine = list_index.as_query_engine()
        response = query_engine.query(txt)
    for i in response.response.split("。"):
        st.write(i + "。")
        st.write('\n')


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))




