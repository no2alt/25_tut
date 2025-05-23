import streamlit as st

# 페이지 설정
st.set_page_config(page_title="나의 소개 페이지", page_icon="📘", layout="centered")

# 제목
st.title("👋 안녕하세요! 반갑습니다.")

# 사이드바 - 사진 업로드
st.sidebar.header("📷 프로필 사진 업로드")
uploaded_file = st.sidebar.file_uploader("이미지를 업로드하세요 (jpg, png)", type=["jpg", "png"])
if uploaded_file:
    st.sidebar.image(uploaded_file, width=200, caption="나의 사진")

# 소개 섹션
st.header("🙋 나에 대해 소개합니다")

name = st.text_input("이름을 입력하세요", placeholder="예: 홍길동")
school = st.text_input("학교를 입력하세요", placeholder="예: OO대학교")
hobby = st.text_area("취미를 입력하세요", placeholder="예: 독서, 여행, 코딩")
email = st.text_input("이메일을 입력하세요", placeholder="예: example@email.com")

if st.button("프로필 저장하기"):
    if name and school and email:
        st.success("✅ 프로필이 저장되었습니다!")
        st.write(f"### 📝 내 소개")
        st.write(f"- **이름**: {name}")
        st.write(f"- **학교**: {school}")
        st.write(f"- **취미**: {hobby if hobby else '취미 정보 없음'}")
        st.write(f"- **이메일**: {email}")
    else:
        st.warning("⚠️ 이름, 학교, 이메일은 필수 입력 항목입니다.")

# 하단 정보
st.markdown("---")
st.markdown("Made with ❤️ by Streamlit")
