import streamlit as st

def set_detail(name):
    st.session_state['detail'] = name

def get_gamecompany(games):
    # 회사 리스트
    # 4개 열 -> 4개 열마다 사진, 가게명, 간단한 설명.
    # for col in st.columns(4):
    for idx, col in enumerate(st.columns(len(games))):
        # st.columns(4) -> 4개의 열이 묶인 리스트
        # 해당 열들을 순서대로 col이라는 변수로 사용
        # ...
        game = games[idx]  # <- 외부에서 데이터를 받아서...
        # col.header("맛집이름")
        col.header(game["name"])
        # col.image("https://cdn.pixabay.com/photo/2017/02/10/08/38/pasta-2054656_640.jpg")
        col.image(game["img"])
        # star_count = 5
        star_count = game["star"]
        col.write("".join(["⭐"] * star_count))
        # col.write("설명 설명...")
        col.write(game['desc'])
        # There are multiple identical st.button widgets with the same generated key.
        # st.button -> bool => 눌리면 해당 button => True
        if col.button("자세히보기", key=f"button{idx}", use_container_width=True):
            # 눌렀을 때 실행되는 코드...
            # col.write(game["name"])
            st.session_state['detail'] = game["name"]
            st.session_state['map'] = game["map"]
            st.session_state['link'] = game["link"]
        # 버튼마다 다른 key가 있어야함.