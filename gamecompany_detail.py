import streamlit as st

def get_gamecompaney_detail():
    st.header(st.session_state['detail'])
    # 회사 상세보기
    # st.image("https://cdn.pixabay.com/photo/2018/05/17/16/03/compass-3408928_1280.jpg")
    st.image(st.session_state['map'], use_column_width=True)
    # link = "https://naver.com"
    link = st.session_state['link']
    st.write(f"[**🦇 네이버 플레이스 링크**]({link})")