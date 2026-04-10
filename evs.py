import streamlit as st


def add_vertical_space(lines: int = 1):
    for _ in range(lines):
        st.write("")
