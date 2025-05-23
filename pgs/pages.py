import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🧭", layout="centered")

# 제목
st.title("🔍 나에게 맞는 직업은?")
st.subheader("MBTI 기반 진로 추천 사이트 💼")

# MBTI 리스트
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 사용자 MBTI 선택
selected_mbti = st.selectbox("🧬 당신의 MBTI를 선택하세요!", mbti_types)

# 추천 직업 딕셔너리
career_dict = {
    "ISTJ": ["📊 회계사", "🔍 감사관", "👮 경찰관"],
    "ISFJ": ["🏥 간호사", "👩‍🏫 교사", "📚 사서"],
    "INFJ": ["🎨 예술가", "🧠 심리상담사", "✍️ 작가"],
    "INTJ": ["💻 데이터 과학자", "🔬 연구원", "📈 전략기획가"],
    "ISTP": ["🛠️ 기술자", "🚗 자동차 정비사", "🕵️ 범죄 수사관"],
    "ISFP": ["🎵 음악가", "🎨 디자이너", "🌿 원예사"],
    "INFP": ["📖 작가", "🎭 배우", "🧘‍♂️ 명상 코치"],
    "INTP": ["🧪 과학자", "👨‍💻 개발자", "🔍 분석가"],
    "ESTP": ["🚓 경찰관", "📢 이벤트 기획자", "🏃 운동선수"],
    "ESFP": ["🎤 연예인", "💃 무용가", "🎉 파티플래너"],
    "ENFP": ["🎨 크리에이터", "🧑‍🏫 교육자", "🌍 사회운동가"],
    "ENTP": ["🚀 스타트업 창업가", "🎙️ 방송인", "🧠 컨설턴트"],
    "ESTJ": ["📋 관리자", "🏢 공무원", "📦 물류 전문가"],
    "ESFJ": ["🧑‍⚕️ 의료 서비스직", "🎓 교사", "🎁 고객 지원"],
    "ENFJ": ["🧑‍🏫 교육 컨설턴트", "🌱 사회복지사", "🗣️ 커뮤니케이터"],
    "ENTJ": ["💼 CEO", "📊 경영 컨설턴트", "🏛️ 정치가"]
}

# 결과 출력
st.markdown("---")
st.header(f"🎯 {selected_mbti} 유형에게 어울리는 직업은?")
if selected_mbti in career_dict:
    for job in career_dict[selected_mbti]:
        st.markdown(f"- {job}")
else:
    st.warning("MBTI를 선택해주세요!")

# 푸터
st.markdown("---")
st.markdown("🧭 **당신의 성향에 맞는 진로를 찾아보세요!**\nMade with ❤️ by Streamlit")
