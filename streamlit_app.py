from importlib import import_module

import streamlit as st

rag = import_module("07_prompting")


st.title("Simple RAG Assistant")

question = st.text_area("Question")

if st.button("Answer") and question.strip():
    answer, sources = rag.answer_question(question)
    st.text_area("Answer", value=answer, height=220)

    with st.expander("Sources"):
        for source in sources:
            st.write(source["title"])
            st.write(source["chunk_text"])

