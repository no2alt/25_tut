import streamlit as st

# 페이지 설정
st.set_page_config(page_title="김재경 소개 페이지", page_icon="🧑", layout="centered")

# 제목
st.title("👋 안녕하세요! 저는 김재경입니다.")

# 소개 정보
st.header("📌 기본 정보")

st.markdown("""
- **이름**: 김재경  
- **학교**: 영동일고등학교  
- **취미**: 🎧 힙합 감상 & 랩 쓰기  
- **이메일**: [23s003@ydi.hs.kr](mailto:23s003@ydi.hs.kr)
""")

# 추가 설명이나 인삿말
st.markdown("---")
st.subheader("🙌 한 마디")
st.markdown("""
힙합을 사랑하는 고등학생 김재경입니다!  
저를 소개하는 이 페이지를 봐주셔서 감사합니다 😊
""")

# 푸터
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
