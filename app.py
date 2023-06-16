# @@ -0,0 +1,63 @@
# app.py, main.py, streamlit_app.py, home.py ...
# 리팩토링 -> 코드를 깔끔하고 간명하게 만드는 작업...

# streamlit
import streamlit as st # streamlit 기능묶음(패키지) -> import 불러오고, as ~한 변수명으로 쓰겠다.
# 짧은 별칭(별명) -> 길다보니까 사용성이 낮아져서...
# from gamecompany_list import get_gamecompany_list
# from gamecompany_detail import get_gamecompany_detail

st.title("내가 좋아하는 게임 회사")
# streamlit run app.py
# -> 프로젝트 생성 -> 가상환경 (파이썬 관련 설치를 매번 독립적)
# 새로운 프로젝트를 만들면 -> 새롭게 설치
# pip install streamlit

# https://crop-circle.imageonline.co/
# store1 = {
#     "name": "T1",
#     "img": "img/T1.png",
#     "star": 5,
#     "desc": "**T1**은 정릉역에 위치한 아주 유명 유명한 게임 회사"
# }
def gamecompany(name, img, star, desc, map, link):
    return dict(name=name, img=img, star=star, desc=desc, map=map, link=link)

game1 = gamecompany(
    "T1", "img/T1.png", 5,
    "**T1**은 신정릉역에 위치한 아주 유명한 게임 회사,"\
    "세계 챔피언십에서 3번의 우승을 차지한 전설적인 팀이다."\
    "T1은 오랜 역사와 전통을 가진 팀으로, 오랜 기간 동안 꾸준한 성과와 팬들의 지지를 받아왔습니다."\
    "T1은 열정적인 팬들의 큰 사랑을 받고 있습니다. 팬들은 팀을 지지하고 응원하며,"\
    "이는 팀의 자신감을 높이고 경기에 긍정적인 영향을 줍니다."\
    "T1에는 e스포츠를 모르더라도 한번쯤은 들어봤을 페이커라는 선수가 있습니다"\
    "img/T1.png",
    "https://naver.me/Fn2W2qM1",
)
game2 = gamecompany(
    "Drx", "img/DRX.png", 2,
    "**Drx**은 합정역 5분거리에 위치한 게임 회사이다,"\
    "창의적인 전략과 플레이 스타일: DRX는 독특하고 창의적인 전략을 통해 경기에 접근합니다."\
    "그들의 플레이 스타일은 예측할 수 없는 요소와 다양한 전술적 선택으로 인해 상대 팀에게 어려움을 주는 특징이 있습니다."\
    "그들의 플레이를 보먄 처음 접하는 사람들도 흥미가 생길 수 밖에 없습니다"\
    "img/DRX.png",
    "https://naver.me/xM24LsAu",
)
game3 = gamecompany(
    "Live SandBox", "img/live.png", 4,
    "**Live SandBox**은 가양역 바로 앞에 있습니다"\
    "예측 불가능한 플레이로 보는 이들의 눈을 즉겁게 해줍니다"\
    "리브 샌드박스의 장점으로는 단합력인데요,"\
    "많이 힘듬 게임도 엄청난 집중력으로 여러번의 역전을 성공시켰습니다"\
    "그리고 이번 시즌에는 Teddy선수가 영입되면서 더 큰 기대를 가지고 있는 팀입니다"\
    "img/live.png",
    "https://naver.me/59et16mN",
)
game4 = gamecompany(
    "Kdf", "img/kdf.png", 3,
    "**Kdf**은 봉은사역 주변에 위치해 있습니다"\
    "Kdf는 거의 신입인 선수들로 구성이 되어 있지만 그 구성이 사람의 감성을 자극합니다"\
    "Kdf에는 아주 유명한 감독인 CvMax가 있습니다,"\
    "야구에 한화가 있다면 e스포츠에는 Kdf가 있습니다"\
    "그리고 이번 시즌에는 Kdf의 여름은 다르다고 선전 포고를 하여는데요 지켜보시면 좋을꺼 같습니다"\
    "img/kdf.png",
    "https://naver.me/Fyx48iUO",
)

games = [game1, game2, game3, game4]

# 일종의 딕셔너리 (페이지가 모두 공유하는 딕셔너리)
if 'detail' not in st.session_state:  # key를 확인해서
    st.session_state['detail'] = ""  # 초기값
    st.session_state['map'] = ""  # 초기값
    st.session_state['link'] = ""  # 초기값

# 게임회사 리스트
get_gamecompany(games)

# 게임 상세 알아보기
if st.session_state['detail']:  # 초기값의 빈 문자열
    get_gamecompany_detail()  # 처음에는 실행하지 않고... 클릭했을 때 반응해서 그려지게