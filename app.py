import streamlit as st
from streamlit_searchbox import st_searchbox
import os, yaml, re, base64

def get_base64_of_file(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ==============================
# CSS
# ==============================
bg_file = "images/background.png"
bg_ext = "png"
bg_base64 = get_base64_of_file(bg_file)

st.markdown(
    f"""
    <style>
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}

    .stApp {{
        background: url("data:image/{bg_ext};base64,{bg_base64}") no-repeat center center fixed;
        background-size: cover;
    }}

    /* ép container searchbox cố định */
    div[data-testid="stVerticalBlock"]:has(div[data-baseweb="select"]) {{
        position: fixed !important;
        top: 20% !important;   /* searchbox */
        left: 50% !important;
        transform: translateX(-50%) !important;
        z-index: 9999 !important;
        width: 600px;
        text-align: center;
    }}

    /* Câu trả lời chiếm hết từ dưới searchbox đến đáy màn hình */
    #answer-fixed {{
        position: fixed;
        top: 40%;                 /* bắt đầu ngay dưới searchbox */
        bottom: 0;                 /* kéo dài xuống hết màn hình */
        left: 50%;
        transform: translateX(-50%);
        width: 70%;
        overflow-y: auto;
        background: rgba(255,255,255,0.95);
        border: 2px solid #1a73e8;
        border-radius: 12px 12px 0 0;
        padding: 15px;
        z-index: 9998;
        box-shadow: 0 -4px 12px rgba(0,0,0,0.2);
    }}

    /* Highlight box cho phần nội dung trả lời */
    .answer-box {{
        background: #fff8dc;
        border: 2px solid #f4c542;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        line-height: 1.6;
        color: #000;
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
        white-space: pre-wrap;
    }}
    .answer-box img {{
        max-width: 100%;
        height: auto;
        margin: 10px 0;
        border-radius: 6px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.2);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# Load dữ liệu
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

# Convert Markdown → HTML (xử lý ảnh local thành base64)
def convert_markdown_to_html(md_text, base_folder="faqs"):
    def replace_img(match):
        alt_text, path = match.groups()
        if os.path.isabs(path):
            full_path = path
        else:
            full_path = os.path.join(base_folder, path)
            if not os.path.exists(full_path):
                full_path = path

        if os.path.exists(full_path):
            ext = os.path.splitext(full_path)[1][1:].lower() or "png"
            img_base64 = get_base64_of_file(full_path)
            return f'<img src="data:image/{ext};base64,{img_base64}" alt="{alt_text}">'
        else:
            return f'<div style="color:red;">⚠️ Không tìm thấy ảnh: {path}</div>'

    pattern = r'!\[(.*?)\]\((.*?)\)'
    html = re.sub(pattern, replace_img, md_text)
    html = html.replace("\n", "<br>")
    return html

# ==============================
# App
# ==============================
faq_data = load_markdown_files()

def search_function(query: str):
    results = []
    if query:
        for item in faq_data:
            text = item["question"].lower() + " " + " ".join(item["keywords"]).lower()
            if query.lower() in text:
                results.append(item["question"])
    return results

# Searchbox
st.markdown("<h2 style='color:white; text-shadow:1px 1px 4px black;'>Thông tin tìm kiếm</h2>", unsafe_allow_html=True)

selected_question = st_searchbox(
    search_function,
    key="faq_search",
    placeholder="🔍 Nhập câu hỏi/từ khóa (ví dụ: mã số thuế)"
)

# Auto-select khi focus vào searchbox
st.markdown(
    """
    <script>
    const observer = new MutationObserver(() => {
        const input = window.parent.document.querySelector('input[data-baseweb="input"]');
        if (input) {
            input.onfocus = function() { this.select(); };
        }
    });
    observer.observe(window.parent.document, {childList: true, subtree: true});
    </script>
    """,
    unsafe_allow_html=True
)

# Answer highlight
if selected_question and isinstance(selected_question, str):
    matched = [r for r in faq_data if r["question"].strip() == selected_question.strip()]
    if matched:
        answer = matched[0]["answer"]

        answer_html = convert_markdown_to_html(answer)

        st.markdown(
            f"""
            <div id="answer-fixed">
                <h3 style="margin-top:0; color:#1a73e8;">✨ Câu trả lời:</h3>
                <div class="answer-box">{answer_html}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning(f"❌ Không tìm thấy câu hỏi: {selected_question}")
