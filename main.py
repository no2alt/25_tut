import streamlit as st

# 페이지 설정
st.set_page_config(page_title="김재경 소개 페이지", page_icon="🧑", layout="centered")

# 제목
st.title("👋 안녕하세요! 저는 김재경입니다.")

# 프로필 사진
st.image("profile.jpg", width=200, caption="김재경", use_column_width=False)

# 소개 정보
st.header("📌 기본 정보")

st.markdown("""
- **이름**: 김재경  
- **학교**: 영동일고등학교  
- **취미**: 힙합  
- **이메일**: [23s003@ydi.hs.kr](mailto:23s003@ydi.hs.kr)
""")

# 추가 설명이나 인삿말
st.markdown("---")
st.subheader("🙌 한 마디")
st.markdown("""
힙합을 사랑하는 고등학생 김재경입니다!  
이 소개 페이지를 통해 저를 알아가 주세요. 감사합니다!
""")

# 푸터
st.markdown("---")
st.markdown("Made with ❤️ by Streamlit")
