import streamlit as st
import pandas as pd
import numpy as np


def main():
    st.title("Show Plot")

    between = st.sidebar.slider('範囲設定', 1, 100, 50)

    button = st.button('show plot')
    if button:
        df = pd.DataFrame(np.arange(between))
        st.dataframe(df, use_container_width=True)


if __name__ == "__main__":
    main()
