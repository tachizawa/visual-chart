import streamlit as st
import websockets

stream = st

def navigate_to_page(page_name):
    global stream
    stream.session_state.page = page_name
    websockets.websocket_entry()


# ホームページ
def render_home():
    global stream
    stream.title("ホームページ")
    stream.write("ここはホームページです。")
    if stream.button("製品ページに移動", on_click=navigate_to_page('products')):
        navigate_to_page('products')


# 製品ページ
def render_products():
    global stream
    stream.title("製品ページ")
    stream.write("ここは製品ページです。")
    if stream.button("ホームに戻る", on_click=navigate_to_page('home')):
        navigate_to_page('home')

def main():
    if 'page' not in stream.session_state:
        stream.session_state.page = 'home'

    # ページの内容を制御
    if stream.session_state.page == 'home':
        render_home()
    elif stream.session_state.page == 'products':
        render_products()

if __name__ == "__main__":
    main()
