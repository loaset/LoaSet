import streamlit as st

st.set_page_config(
    page_title="LoaSet - 로스트아크 세팅 연구소",
    page_icon="💎",
    layout="centered"
)

st.title("💎 LoaSet")
st.subheader("나만의 최적 세팅을 찾는 가장 스마트한 방법")
st.divider()
st.info("🚧 현재 서비스 오픈 준비 중입니다. 🚧")

st.markdown("""
### Coming Soon
**LoaSet(로아셋)**은 로스트아크 모험가님들을 위한 **차세대 세팅 시뮬레이터**입니다.
더 정확하고, 더 편리한 계산기로 찾아뵙겠습니다.

* **문의:** loaset.official@gmail.com
""")

with st.expander("💌 개발자에게 한마디 남기기"):
    user_msg = st.text_input("원하는 기능이나 응원의 메시지를 적어주세요!")
    if st.button("전송"):
        st.success("소중한 의견 감사합니다! 개발에 반영하겠습니다.")
