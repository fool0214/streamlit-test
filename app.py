import streamlit as st

st.set_page_config(
    page_title="임준혁 — 자기소개",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.stApp { background: #f4f1ec; }
* { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --bg: #f4f1ec; --paper: #ffffff; --ink: #1d1c1a;
  --muted: #6e6a64; --accent: #b34a2a; --line: #e5dfd4;
}
.resume-page {
  max-width: 980px; margin: 40px auto; background: var(--paper);
  display: grid; grid-template-columns: 280px 1fr;
  box-shadow: 0 10px 40px rgba(0,0,0,.08);
  font-family: 'Pretendard', system-ui, sans-serif;
  line-height: 1.55; color: var(--ink);
}
.sidebar { background: #1d1c1a; color: #f4f1ec; padding: 40px 28px; }
.avatar {
  width: 88px; height: 88px; border-radius: 50%;
  background: var(--accent); color: #fff;
  display: grid; place-items: center;
  font-size: 38px; font-weight: 700; margin-bottom: 18px;
}
.s-name { font-size: 26px; letter-spacing: -.5px; }
.s-role { color: #c8c1b6; margin-top: 2px; margin-bottom: 22px; font-size: 14px; }
.contact { list-style: none; font-size: 13px; color: #d3ccc1; }
.contact li { padding: 5px 0; }
.contact span { display: inline-block; width: 22px; }
.side-title { margin: 26px 0 10px; font-size: 11px; letter-spacing: 2px; color: var(--accent); text-transform: uppercase; }
.skills-list { list-style: none; font-size: 13px; }
.skills-list li { margin-bottom: 8px; color: #ece6da; }
.bar { display: block; height: 5px; background: #333; border-radius: 3px; margin-top: 4px; overflow: hidden; }
.bar i { display: block; height: 100%; background: var(--accent); border-radius: 3px; transition: width 1.2s ease; }
.lang-list { list-style: none; font-size: 13px; color: #ece6da; }
.lang-list li { padding: 4px 0; display: flex; justify-content: space-between; }
.lang-list em { color: #9d978a; font-style: normal; font-size: 12px; }
.print-btn {
  margin-top: 30px; width: 100%; padding: 10px 12px;
  background: var(--accent); color: #fff; border: 0; border-radius: 8px;
  font-size: 13px; cursor: pointer; transition: filter .2s;
}
.print-btn:hover { filter: brightness(1.15); }
.content { padding: 44px 40px; background: var(--paper); }
.c-block { margin-top: 32px; }
.block-title {
  font-size: 18px; border-bottom: 2px solid var(--ink);
  display: inline-block; padding-bottom: 4px; margin-bottom: 16px;
}
.intro-p { color: var(--muted); font-size: 15px; line-height: 1.8; }
.timeline { list-style: none; }
.timeline-row { display: grid; grid-template-columns: 140px 1fr; gap: 16px; margin-bottom: 18px; }
.t-date { color: var(--accent); font-size: 13px; font-weight: 600; padding-top: 2px; }
.t-card h3 { font-size: 15px; margin-bottom: 6px; }
.t-card ul { padding-left: 18px; color: var(--muted); font-size: 14px; }
.t-card li { margin-bottom: 3px; }
.projects { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
.proj { border: 1px solid var(--line); padding: 14px; border-radius: 8px; }
.proj h3 { font-size: 14px; margin-bottom: 6px; }
.proj p { font-size: 13px; color: var(--muted); margin-bottom: 8px; }
.tag { display: inline-block; font-size: 11px; padding: 2px 8px; background: #f4f1ec; color: var(--accent); border-radius: 999px; margin-right: 4px; }
.edu-list { list-style: none; }
.edu-list li { padding: 8px 0; border-bottom: 1px dashed var(--line); font-size: 14px; }
.edu-list em { display: block; color: var(--muted); font-style: normal; font-size: 13px; margin-top: 2px; }
@media (max-width: 760px) {
  .resume-page { grid-template-columns: 1fr; margin: 0; box-shadow: none; }
  .timeline-row { grid-template-columns: 1fr; gap: 4px; }
}
@media print {
  body { background: #fff; }
  .resume-page { box-shadow: none; margin: 0; max-width: 100%; }
  .print-btn { display: none; }
}
</style>
""", unsafe_allow_html=True)

sidebar_html = """
<div class="resume-page">
<div class="sidebar">
<div class="avatar">준</div>
<div class="s-name">임준혁</div>
<div class="s-role">Full Stack Developer · AI Enthusiast</div>
<ul class="contact">
<li><span>📧</span> lim.junhyeok@email.com</li>
<li><span>📱</span> 010-1234-5678</li>
<li><span>📍</span> 서울특별시</li>
<li><span>🔗</span> github.com/fool0214</li>
</ul>
<h2 class="side-title">스킬</h2>
<ul class="skills-list">
<li>Python <span class="bar"><i style="width:95%"></i></span></li>
<li>JavaScript <span class="bar"><i style="width:78%"></i></span></li>
<li>FastAPI <span class="bar"><i style="width:85%"></i></span></li>
<li>Streamlit <span class="bar"><i style="width:90%"></i></span></li>
<li>SQL <span class="bar"><i style="width:75%"></i></span></li>
</ul>
<h2 class="side-title">언어</h2>
<ul class="lang-list">
<li>한국어 <em>모국어</em></li>
<li>영어 <em>업무 가능</em></li>
</ul>
<button class="print-btn" onclick="window.print()">📄 PDF로 저장</button>
</div>
<div class="content">
<div>
<h2 class="block-title">소개</h2>
<p class="intro-p">안녕하세요! 사용자 경험을 중심으로 생각하는 개발자입니다. Python, FastAPI, Streamlit을 주력으로 사용하며, 데이터 분석과 AI에 관심이 많습니다. 새로운 기술을 배우고 문제를 해결하는 것을 즐기며, 협업을 통해 더 나은 제품을 만들어가는 과정을 좋아합니다.</p>
</div>
<div class="c-block">
<h2 class="block-title">경력</h2>
<ol class="timeline">
<li class="timeline-row">
<div class="t-date">2023.03 — 현재</div>
<div class="t-card"><h3>ABC 테크 · 시니어 개발자</h3><ul><li>백엔드 서비스 설계 및 AI 기능 개발</li><li>FastAPI 기반 RESTful API 설계 및 운영</li><li>LLM 기반 챗봇 서비스 개발</li></ul></div>
</li>
<li class="timeline-row">
<div class="t-date">2021.01 — 2023.02</div>
<div class="t-card"><h3>XYZ 스타트업 · 풀스택 개발자</h3><ul><li>웹 서비스 전반 개발 및 운영</li><li>React + FastAPI 기반 SaaS 플랫폼 구축</li></ul></div>
</li>
<li class="timeline-row">
<div class="t-date">2019.07 — 2020.12</div>
<div class="t-card"><h3>퍼스트 소프트 · 주니어 개발자</h3><ul><li>사내 관리 시스템 유지보수 및 기능 추가</li></ul></div>
</li>
</ol>
</div>
<div class="c-block">
<h2 class="block-title">대표 프로젝트</h2>
<div class="projects">
<div class="proj"><h3>AI 챗봇 서비스</h3><p>LangChain + OpenAI API 기반 문서 Q&A 챗봇. 사내 지식베이스 검색 자동화.</p><span class="tag">AI</span><span class="tag">LangChain</span></div>
<div class="proj"><h3>데이터 대시보드</h3><p>Streamlit 기반 실시간 데이터 시각화 대시보드. KPI 모니터링 자동화.</p><span class="tag">Streamlit</span><span class="tag">Pandas</span></div>
<div class="proj"><h3>FastAPI 백엔드</h3><p>마이크로서비스 아키텍처 기반 RESTful API 설계 및 Docker 배포.</p><span class="tag">FastAPI</span><span class="tag">Docker</span></div>
</div>
</div>
<div class="c-block">
<h2 class="block-title">학력</h2>
<ul class="edu-list">
<li><strong>한국대학교</strong> 컴퓨터공학과 · 2015–2019<em>전공 학점 4.1 / 4.5 · 졸업 우수상</em></li>
</ul>
</div>
</div>
</div>
<script>
(function(){
var btn=document.querySelector('.print-btn');
if(btn) btn.addEventListener('click',function(){window.print();});
document.querySelectorAll('.bar i').forEach(function(el){
var w=el.style.width; el.style.width='0';
requestAnimationFrame(function(){el.style.width=w;});
});
})();
</script>
"""

st.markdown(sidebar_html, unsafe_allow_html=True)
