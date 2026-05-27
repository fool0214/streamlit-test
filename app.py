import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="자기소개 | My Portfolio",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# CSS 스타일
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #f0f0f0;
    }
    .hero-section {
        text-align: center;
        padding: 60px 20px 40px;
    }
    .hero-avatar {
        width: 140px;
        height: 140px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea, #764ba2);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 64px;
        margin: 0 auto 24px;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.5);
        line-height: 140px;
    }
    .hero-name {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }
    .hero-title {
        font-size: 1.2rem;
        color: #a78bfa;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 20px;
    }
    .hero-desc {
        font-size: 1.05rem;
        color: #c4c4e0;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.8;
    }
    .card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 16px;
        padding: 28px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }
    .card-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #a78bfa;
        margin-bottom: 18px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .skill-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }
    .skill-badge {
        background: linear-gradient(135deg, rgba(102,126,234,0.3), rgba(118,75,162,0.3));
        border: 1px solid rgba(102, 126, 234, 0.4);
        border-radius: 20px;
        padding: 6px 16px;
        font-size: 0.9rem;
        color: #d4b8ff;
        font-weight: 500;
    }
    .timeline-item {
        border-left: 2px solid rgba(102, 126, 234, 0.5);
        padding-left: 20px;
        margin-bottom: 20px;
        position: relative;
    }
    .timeline-item::before {
        content: '';
        width: 10px;
        height: 10px;
        background: #667eea;
        border-radius: 50%;
        position: absolute;
        left: -6px;
        top: 4px;
    }
    .timeline-date {
        font-size: 0.82rem;
        color: #a78bfa;
        font-weight: 600;
        letter-spacing: 1px;
    }
    .timeline-title {
        font-size: 1rem;
        font-weight: 600;
        color: #f0f0f0;
        margin: 4px 0 2px;
    }
    .timeline-sub {
        font-size: 0.88rem;
        color: #9090b0;
    }
    .contact-item {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 12px 0;
        border-bottom: 1px solid rgba(102, 126, 234, 0.1);
        color: #c4c4e0;
        font-size: 0.95rem;
    }
    .contact-icon {
        font-size: 1.3rem;
        width: 36px;
        text-align: center;
    }
    .divider {
        border: none;
        border-top: 1px solid rgba(102, 126, 234, 0.15);
        margin: 40px 0;
    }
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 0 !important; max-width: 1000px;}
</style>
""", unsafe_allow_html=True)

# ─── 히어로 섹션 ───────────────────────────────────────────────
st.markdown("""
<div class="hero-section">
    <div class="hero-avatar">👤</div>
    <div class="hero-name">임 준 혁</div>
    <div class="hero-title">Full Stack Developer · AI Enthusiast</div>
    <div class="hero-desc">
        안녕하세요! 사용자 경험을 중심으로 생각하는 개발자입니다.<br>
        새로운 기술을 배우고 문제를 해결하는 것을 즐기며,<br>
        협업을 통해 더 나은 제품을 만들어가는 과정을 좋아합니다.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ─── 본문 레이아웃 (2컬럼) ──────────────────────────────────────
col1, col2 = st.columns([1.1, 1])

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">🙋 About Me</div>
        <p style="color:#c4c4e0; line-height:1.9; margin:0;">
            • 현재 <strong style="color:#a78bfa;">백엔드 / AI 개발</strong>에 집중하고 있습니다.<br>
            • Python, FastAPI, Streamlit을 주력으로 사용합니다.<br>
            • 데이터 분석과 머신러닝에 관심이 많습니다.<br>
            • 사이드 프로젝트로 다양한 아이디어를 실험합니다.<br>
            • 커피 한 잔과 함께하는 코딩을 즐깁니다 ☕
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-title">⚡ 기술 스택</div>
        <p style="color:#9090b0; font-size:0.85rem; margin-bottom:12px;">Languages</p>
        <div class="skill-grid">
            <span class="skill-badge">Python</span>
            <span class="skill-badge">JavaScript</span>
            <span class="skill-badge">TypeScript</span>
            <span class="skill-badge">SQL</span>
        </div>
        <p style="color:#9090b0; font-size:0.85rem; margin:16px 0 12px;">Frameworks & Tools</p>
        <div class="skill-grid">
            <span class="skill-badge">Streamlit</span>
            <span class="skill-badge">FastAPI</span>
            <span class="skill-badge">React</span>
            <span class="skill-badge">Docker</span>
            <span class="skill-badge">Git</span>
            <span class="skill-badge">AWS</span>
        </div>
        <p style="color:#9090b0; font-size:0.85rem; margin:16px 0 12px;">AI / Data</p>
        <div class="skill-grid">
            <span class="skill-badge">LangChain</span>
            <span class="skill-badge">OpenAI API</span>
            <span class="skill-badge">Pandas</span>
            <span class="skill-badge">Scikit-learn</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">💼 경력</div>
        <div class="timeline-item">
            <div class="timeline-date">2023.03 – 현재</div>
            <div class="timeline-title">시니어 개발자 · ABC 테크</div>
            <div class="timeline-sub">백엔드 서비스 설계 및 AI 기능 개발</div>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">2021.01 – 2023.02</div>
            <div class="timeline-title">풀스택 개발자 · XYZ 스타트업</div>
            <div class="timeline-sub">웹 서비스 전반 개발 및 운영</div>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">2019.07 – 2020.12</div>
            <div class="timeline-title">주니어 개발자 · 퍼스트 소프트</div>
            <div class="timeline-sub">사내 관리 시스템 유지보수 및 기능 추가</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-title">🎓 학력</div>
        <div class="timeline-item">
            <div class="timeline-date">2015 – 2019</div>
            <div class="timeline-title">컴퓨터공학 학사 · 한국대학교</div>
            <div class="timeline-sub">전공 학점 4.1 / 4.5 · 졸업 우수상</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-title">📬 연락처</div>
        <div class="contact-item">
            <span class="contact-icon">📧</span>
            <span>hong.gildong@email.com</span>
        </div>
        <div class="contact-item">
            <span class="contact-icon">🐙</span>
            <span>github.com/hong-gildong</span>
        </div>
        <div class="contact-item">
            <span class="contact-icon">💼</span>
            <span>linkedin.com/in/hong-gildong</span>
        </div>
        <div class="contact-item" style="border-bottom:none;">
            <span class="contact-icon">📍</span>
            <span>서울, 대한민국</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── 푸터 ────────────────────────────────────────────────────────
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; padding: 20px 0 40px;">
    <p style="color:#9090b0; font-size:0.9rem; letter-spacing:1px;">
        ✨ 이 페이지는 <strong style="color:#a78bfa;">Streamlit</strong>으로 제작되었습니다
    </p>
</div>
""", unsafe_allow_html=True)
