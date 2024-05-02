import streamlit as st


def main():
    st.title('Simple App')
    st.header('Simple App')
    st.radio("好きなマイケルは？", ('ジャクソン', 'ジョーダン', 'ホフマン'))


if __name__ == "__main__":
    main()
