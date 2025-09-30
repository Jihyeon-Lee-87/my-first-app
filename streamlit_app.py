import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# --- Streamlit 요소 예시 (각주 포함) ---

st.header("1. 텍스트 요소")  # 제목, 헤더, 일반 텍스트 등
st.subheader("1-1. Subheader 예시")  # 부제목
st.text("이것은 일반 텍스트입니다.")  # 일반 텍스트
st.markdown("**마크다운** _포맷_ 지원!")  # 마크다운 지원
st.code('print("Hello, Streamlit!")', language='python')  # 코드 블록
st.latex(r'\alpha^2 + \beta^2 = \gamma^2')  # LaTeX 수식

st.header("2. 데이터 표시 요소")  # 표, 데이터프레임, JSON 등
import pandas as pd
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
st.table(df)  # 정적 테이블
st.dataframe(df)  # 동적 데이터프레임
st.json({"key": "value", "list": [1, 2, 3]})  # JSON 표시

st.header("3. 입력 위젯")  # 사용자 입력을 받는 위젯
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이", min_value=0, max_value=120, value=25)  # 숫자 입력
agree = st.checkbox("동의합니다")  # 체크박스
selected = st.radio("성별", ["남성", "여성", "기타"])  # 라디오 버튼
options = st.selectbox("좋아하는 과일", ["사과", "바나나", "오렌지"])  # 셀렉트박스
multi = st.multiselect("좋아하는 색상", ["빨강", "파랑", "초록"])  # 다중 선택
date = st.date_input("날짜 선택")  # 날짜 입력
time = st.time_input("시간 선택")  # 시간 입력
uploaded_file = st.file_uploader("파일 업로드")  # 파일 업로더

st.header("4. 버튼 및 상호작용")  # 버튼, 슬라이더 등
if st.button("클릭하세요"):  # 버튼
    st.write("버튼이 클릭되었습니다!")
value = st.slider("슬라이더", 0, 100, 50)  # 슬라이더
progress = st.progress(0.5)  # 진행률 바 (0~1)

st.header("5. 미디어 요소")  # 이미지, 오디오, 비디오 등
from PIL import Image
import numpy as np
img = Image.fromarray(np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8))
st.image(img, caption="랜덤 이미지")  # 이미지 표시
st.audio(np.random.randn(44100), sample_rate=44100)  # 오디오 표시 (임의 데이터)
st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # 비디오 표시

st.header("6. 상태/알림/레이아웃")  # 상태 표시, 알림, 컬럼 등
st.success("성공 메시지!")  # 성공 알림
st.info("정보 메시지")  # 정보 알림
st.warning("경고 메시지")  # 경고 알림
st.error("에러 메시지")  # 에러 알림
st.exception(Exception("예외 메시지 예시"))  # 예외 메시지

col1, col2 = st.columns(2)  # 컬럼 레이아웃
col1.write("왼쪽 컬럼")
col2.write("오른쪽 컬럼")

with st.expander("더보기 (Expander)"):
    st.write("이곳에 추가 정보를 넣을 수 있습니다.")

# --- 각주 ---
st.markdown("""
---
**각주**  
1. 텍스트 요소: st.title, st.header, st.subheader, st.text, st.markdown, st.code, st.latex 등 다양한 텍스트 및 포맷 지원.  
2. 데이터 표시: st.table, st.dataframe, st.json 등 데이터 시각화.  
3. 입력 위젯: st.text_input, st.number_input, st.checkbox, st.radio, st.selectbox, st.multiselect, st.date_input, st.time_input, st.file_uploader 등.  
4. 버튼/상호작용: st.button, st.slider, st.progress 등.  
5. 미디어: st.image, st.audio, st.video 등.  
6. 상태/레이아웃: st.success, st.info, st.warning, st.error, st.exception, st.columns, st.expander 등.
""")
