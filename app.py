
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="GLASS//FIT | AR 안경 가상 피팅",
    page_icon="👓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 실제 안경 가상 피팅 엔진
# static/GlassFit.html 파일이 필요합니다.
app_file = (
    Path(__file__).parent
    / "static"
    / "GlassFit.html"
)

st.markdown("""
<style>
.block-container {
    padding-top: .6rem;
    padding-bottom: 1rem;
    max-width: 100%;
}
h1 {
    font-size: 1.4rem !important;
}
.small-note {
    color: #beb5e0;
    font-size: 13px;
}
@media (max-width: 700px) {
    .block-container {
        padding: .5rem .45rem 1.5rem;
    }
    h1 {
        font-size: 1.15rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

st.title("👓 GLASS//FIT · AR 안경 가상 피팅")

if not app_file.is_file():
    st.error(
        "static/GlassFit.html 파일이 없습니다. "
        "GitHub에 이 파일도 함께 업로드해 주세요."
    )
    st.stop()

# Streamlit 공식 정적 파일 제공 경로
static_url = "/app/static/GlassFit.html"

st.markdown(
    '<a href="' + static_url + '" '
    'target="_blank" rel="noopener" '
    'style="display:block;'
    'text-decoration:none;'
    'text-align:center;'
    'padding:12px 16px;'
    'border-radius:12px;'
    'background:linear-gradient('
    '90deg,#ff2bd6,#7f4dff,#19e3ff);'
    'color:#ffffff;'
    'font-weight:800;'
    'font-size:16px;">'
    '👓 전체 화면으로 가상 피팅 열기'
    ' (스마트폰 권장)</a>',
    unsafe_allow_html=True,
)

st.caption(
    "전체 화면에서 카메라 또는 갤러리를 "
    "선택하세요. 실시간 피팅에는 카메라 "
    "접근 권한이 필요합니다."
)

with st.expander(
    "Streamlit 페이지 안에서 미리보기",
    expanded=False,
):
    st.info(
        "내장 화면에서는 카메라 접근이 "
        "제한될 수 있습니다. "
        "전체 화면 링크를 사용하세요."
    )

    components.iframe(
        static_url,
        height=760,
        scrolling=True,
    )

st.markdown("""
<div class="small-note">
<strong>지원 기기:</strong>
Windows PC, Android 스마트폰,
iPhone, iPad 및 태블릿<br>

<strong>사용 방법:</strong>
별도 앱 설치 없이 웹 주소로 실행<br>

<strong>인터넷:</strong>
Streamlit 공유 주소에 접속하려면
인터넷 연결이 필요합니다.<br>

<strong>AI:</strong>
자동 얼굴 인식은 모델 로딩과
브라우저 권한에 따라 달라집니다.
</div>
""", unsafe_allow_html=True)
