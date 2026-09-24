import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Cấu hình trang Streamlit mở rộng full màn hình
st.set_page_config(
    page_title="TQG-Dashboard Quản Lý Triển Khai",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Xóa margin/padding mặc định của Streamlit để HTML tràn viền đẹp mắt
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Đọc nội dung file index.html
@st.cache_data
def load_html():
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

html_content = load_html()

# 4. Hiển thị HTML trong Streamlit với chiều cao full giao diện
components.html(html_content, height=1200, scrolling=True)
