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

# 2. CSS tùy chỉnh
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 1rem !important;
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

# 3. Thư mục lưu trữ dữ liệu bền vững
DATA_DIR = "uploaded_data"
os.makedirs(DATA_DIR, exist_ok=True)

# Widget upload file ở Sidebar của Streamlit
with st.sidebar:
    st.title("Quản lý dữ liệu")
    uploaded_file = st.file_uploader("Upload file dữ liệu mới (Excel/CSV/JSON)", type=["xlsx", "csv", "json"])
    
    if uploaded_file is not None:
        # Đường dẫn cố định để lưu file dữ liệu mới nhất
        file_path = os.path.join(DATA_DIR, "latest_data" + os.path.splitext(uploaded_file.name)[1])
        
        # Ghi đè file mới lên ổ đĩa
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("Đã cập nhật file dữ liệu mới nhất!")

# 4. Đọc nội dung file index.html
def load_html():
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

html_content = load_html()

# 5. Hiển thị HTML
components.html(html_content, height=1200, scrolling=True)
