import streamlit as st
import pandas as pd
import numpy as np

pageId = ''


def main():
    st.title("Show Plot")
    global pageId

    between = st.sidebar.slider('範囲設定', 1, 100, 50)
    pageId = 'start'

    if pageId == 'start':
        st.title("Start")

        st.button('start', on_click=start)

    if pageId == 'process':
        st.title("Process")

        st.button('cansel', on_click=process)


def start():
    global pageId

    df = pd.DataFrame(np.arange(10))
    st.dataframe(df, use_container_width=True)
    pageId = 'process'


def process():
    global pageId
    df = pd.DataFrame(np.arange(2))
    st.dataframe(df, use_container_width=True)
    pageId = 'start'


if __name__ == "__main__":
    main()
