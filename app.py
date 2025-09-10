import streamlit as st
from streamlit_searchbox import st_searchbox
import os, yaml, re
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ==============================
# CSS cho background + searchbox giữa màn hình
# ==============================
bg_file = "images/background.jpg"
bg_ext = "jpg"  # hoặc "png" tùy file của bạn
bg_base64 = get_base64_of_bin_file(bg_file)

st.markdown(
    f"""
    <style>
    /* Ẩn header và footer */
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}

    /* Background chiếm full màn hình */
    .stApp {{
        background: url("data:image/{bg_ext};base64,{bg_base64}") no-repeat center center fixed;
        background-size: cover;
        height: 100vh; /* chiếm toàn bộ chiều cao cửa sổ */
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    /* Container căn giữa */
    .centered-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }}

    /* Style cho searchbox */
    div[data-baseweb="select"] > div {{
        background-color: #ffffff !important;
        border: 1px solid #dfe1e5 !important;
        border-radius: 999px !important;
        box-shadow: none !important;
        min-height: 44px !important;
        font-size: 16px !important;
        width: 500px !important;
    }}

    div[data-baseweb="select"] > div:focus-within {{
        border: 1px solid #4285f4 !important;
        box-shadow: 0 1px 6px rgba(32,33,36,0.28) !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# ==============================
# Load dữ liệu từ Markdown
# ==============================
def load_markdown_files(folder="faqs"):
    data = []
    for file in os.listdir(folder):
        if file.endswith(".md"):
            path = os.path.join(folder, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            parts = content.split("---")
            parts = [p.strip() for p in parts if p.strip()]
            for i in range(0, len(parts), 2):
                if i + 1 < len(parts):
                    meta = yaml.safe_load(parts[i])
                    body = parts[i+1]
                    data.append({
                        "question": meta["question"].strip(),
                        "keywords": meta.get("keywords", []),
                        "answer": body
                    })
    return data

# ==============================
# Render markdown + ảnh
# ==============================
def render_markdown_with_images(md_text):
    pattern = r'!\[.*?\]\((.*?)\)'  # tìm ảnh ![alt](path)
    parts = re.split(pattern, md_text)

    for i, part in enumerate(parts):
        if i % 2 == 0:
            st.markdown(part, unsafe_allow_html=True)
        else:
            img_path = os.path.join(part)
            if os.path.exists(img_path):
                st.image(img_path, width="stretch")   # ✅ thay vì use_container_width
            else:
                st.warning(f"⚠️ Không tìm thấy ảnh: {img_path}")

# ==============================
# Khởi chạy app
# ==============================
faq_data = load_markdown_files()

def search_function(query: str):
    """Hàm gợi ý câu hỏi theo từ khóa."""
    results = []
    if query:
        for item in faq_data:
            text = item["question"].lower() + " " + " ".join(item["keywords"]).lower()
            if query.lower() in text:
                results.append(item["question"])
    return results

# ==============================
# Nội dung giữa màn hình
# ==============================
st.markdown('<div class="centered-container">', unsafe_allow_html=True)

st.markdown("<h1 style='color:white; text-shadow:1px 1px 4px black;'>📘 Thông tin tìm kiếm</h1>", unsafe_allow_html=True)

selected_question = st_searchbox(
    search_function,
    key="faq_search",
    placeholder="🔍 Nhập từ khóa (ví dụ: mã số thuế)"
)

st.markdown('</div>', unsafe_allow_html=True)


# ==============================
# Hiển thị câu trả lời nếu chọn câu hỏi
# ==============================
if selected_question and isinstance(selected_question, str):
    selected_question = selected_question.strip()
    matched = [r for r in faq_data if r["question"].strip() == selected_question]

    if matched:
        answer = matched[0]["answer"]
        st.markdown("### ✨ Câu trả lời:")
        render_markdown_with_images(answer)
    else:
        st.warning(f"❌ Không tìm thấy câu hỏi: {selected_question}")
