import streamlit as st
from datetime import datetime
import os
import json

# =========================================================
# OPENAI - CHATBOT AI
# =========================================================

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


# Lấy API Key từ biến môi trường
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Model có thể thay đổi bằng biến môi trường OPENAI_MODEL
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-6-luna")

if OPENAI_API_KEY and OpenAI:
    client = OpenAI(api_key=OPENAI_API_KEY)
else:
    client = None


# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Phòng trọ TÂM AN",
    page_icon="🏠",
    layout="wide"
)


# =========================================================
# CSS GIAO DIỆN
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    color: #1f4e79;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666666;
    font-size: 18px;
    margin-bottom: 25px;
}

.box {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.total {
    background: linear-gradient(135deg, #1f4e79, #3498db);
    padding: 25px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-top: 20px;
}

.total-money {
    font-size: 36px;
    font-weight: bold;
}

.room-card {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    box-shadow: 0px 3px 8px rgba(0,0,0,0.08);
}

.chat-user {
    background-color: #dbeafe;
    padding: 12px;
    border-radius: 12px;
    margin: 8px 0;
}

.chat-ai {
    background-color: #f1f5f9;
    padding: 12px;
    border-radius: 12px;
    margin: 8px 0;
}

.chat-title {
    color: #1f4e79;
    font-size: 28px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# ẢNH TRANG CHỦ
# =========================================================

st.image("anh_tam_an.jpg", use_container_width=True)


# =========================================================
# TIÊU ĐỀ
# =========================================================

st.markdown(
    '<div class="title">🏠 PHÒNG TRỌ TÂM AN</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Hệ thống quản lý và tính tiền phòng trọ</div>',
    unsafe_allow_html=True
)


# =========================================================
# DANH SÁCH PHÒNG
# =========================================================

PHONG_LIST = [
    "P101", "P102", "P103", "P104", "P105",
    "P201", "P202", "P203", "P204", "P205"
]


# =========================================================
# THÔNG TIN NGƯỜI THUÊ
# =========================================================

if "nguoi_thue" not in st.session_state:

    st.session_state.nguoi_thue = {

        "P101": "Nguyễn Văn An",
        "P102": "Trần Văn Bình",
        "P103": "Lê Minh Cường",
        "P104": "Phạm Văn Dũng",
        "P105": "Nguyễn Thị Hoa",

        "P201": "Trần Minh Khang",
        "P202": "Lê Văn Nam",
        "P203": "Phạm Thị Lan",
        "P204": "Nguyễn Văn Hùng",
        "P205": "Trần Thị Mai"

    }


# =========================================================
# LƯU HÓA ĐƠN
# =========================================================

if "hoa_don_phong" not in st.session_state:
    st.session_state.hoa_don_phong = {}


# =========================================================
# LƯU LỊCH SỬ CHAT
# =========================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# =========================================================
# FORMAT TIỀN
# =========================================================

def format_money(number):
    return f"{number:,.0f} VNĐ".replace(",", ".")


# =========================================================
# HÀM TẠO DỮ LIỆU CHO CHATBOT
# =========================================================

def tao_du_lieu_chatbot():

    hoa_don = st.session_state.hoa_don_phong

    if not hoa_don:
        return {
            "so_phong_da_tinh": 0,
            "hoa_don": {},
            "thong_ke": {
                "tong_doanh_thu": 0,
                "tong_tien_phong": 0,
                "tong_tien_dien": 0,
                "tong_tien_nuoc": 0,
                "tong_phi_khac": 0,
                "so_phong_da_thanh_toan": 0,
                "so_phong_chua_thanh_toan": 0
            }
        }

    tong_doanh_thu = 0
    tong_tien_phong = 0
    tong_tien_dien = 0
    tong_tien_nuoc = 0
    tong_phi_khac = 0

    da_thanh_toan = 0
    chua_thanh_toan = 0

    for phong, hd in hoa_don.items():

        tong_doanh_thu += hd.get("tong", 0)
        tong_tien_phong += hd.get("tien_phong", 0)
        tong_tien_dien += hd.get("tien_dien", 0)
        tong_tien_nuoc += hd.get("tien_nuoc", 0)

        tong_phi_khac += (
            hd.get("wifi", 0)
            + hd.get("phi_khac", 0)
        )

        if hd.get("trang_thai") == "✅ Đã thanh toán":
            da_thanh_toan += 1
        else:
            chua_thanh_toan += 1

    return {

        "so_phong_da_tinh": len(hoa_don),

        "hoa_don": hoa_don,

        "thong_ke": {

            "tong_doanh_thu": tong_doanh_thu,

            "tong_tien_phong": tong_tien_phong,

            "tong_tien_dien": tong_tien_dien,

            "tong_tien_nuoc": tong_tien_nuoc,

            "tong_phi_khac": tong_phi_khac,

            "so_phong_da_thanh_toan": da_thanh_toan,

            "so_phong_chua_thanh_toan": chua_thanh_toan

        }
    }


# =========================================================
# HÀM GỌI CHATBOT AI
# =========================================================

def hoi_chatbot(question):

    if client is None:

        return """
⚠️ **Chatbot AI chưa được kết nối.**

Bạn cần cài thư viện OpenAI và cấu hình `OPENAI_API_KEY`.

Sau khi cấu hình API Key, chatbot có thể trả lời câu hỏi tự do.
"""

    du_lieu = tao_du_lieu_chatbot()

    system_prompt = f"""
Bạn là AI Chatbot của hệ thống quản lý phòng trọ TÂM AN.

Nhiệm vụ của bạn:

1. Trả lời bằng tiếng Việt.
2. Có thể trả lời câu hỏi về:
   - Phòng trọ TÂM AN
   - Tiền phòng
   - Tiền điện
   - Tiền nước
   - WiFi
   - Phí rác
   - Hóa đơn
   - Thanh toán
   - Doanh thu
   - Thống kê
   - Cách tính tiền
   - Quản lý phòng
3. Ngoài ra, bạn có thể trả lời các câu hỏi kiến thức chung ở nhiều lĩnh vực.
4. Nếu câu hỏi liên quan đến dữ liệu phòng trọ thì PHẢI ưu tiên dữ liệu được cung cấp bên dưới.
5. Không được tự bịa dữ liệu phòng trọ.
6. Nếu dữ liệu chưa có thì nói rõ "Hiện hệ thống chưa có dữ liệu này".
7. Khi tính toán tiền, hãy giải thích phép tính rõ ràng.
8. Trả lời dễ hiểu, ngắn gọn nhưng đầy đủ.
9. Có thể sử dụng emoji phù hợp.
10. Nếu người dùng hỏi một phòng cụ thể, hãy tìm đúng mã phòng.
11. Nếu người dùng hỏi tổng doanh thu, hãy tính dựa trên dữ liệu hiện tại.
12. Nếu người dùng hỏi phòng chưa thanh toán, hãy liệt kê chính xác.
13. Nếu người dùng hỏi tổng tiền điện hoặc nước, hãy sử dụng dữ liệu hiện tại.

DỮ LIỆU PHÒNG TRỌ HIỆN TẠI:

{json.dumps(du_lieu, ensure_ascii=False, indent=2)}

Danh sách tất cả phòng:

{json.dumps(PHONG_LIST, ensure_ascii=False)}

Người thuê:

{json.dumps(st.session_state.nguoi_thue, ensure_ascii=False, indent=2)}
"""

    try:

        response = client.responses.create(

            model=OPENAI_MODEL,

            instructions=system_prompt,

            input=question

        )

        return response.output_text

    except Exception as e:

        return f"""
❌ Không thể kết nối Chatbot AI.

Chi tiết lỗi:

`{str(e)}`
"""


# =========================================================
# MENU
# =========================================================

menu = st.sidebar.radio(

    "📌 MENU",

    [

        "🏠 Tính tiền phòng",

        "📋 Quản lý toàn bộ phòng",

        "🤖 Chatbot TÂM AN",

        "ℹ️ Thông tin TÂM AN"

    ]

)


# =========================================================
# TRANG 1 - TÍNH TIỀN PHÒNG
# =========================================================

if menu == "🏠 Tính tiền phòng":

    st.markdown(
        '<div class="box">',
        unsafe_allow_html=True
    )

    st.subheader("🏠 Tính tiền phòng")

    phong = st.selectbox(
        "Chọn phòng",
        PHONG_LIST
    )

    ten_khach = st.session_state.nguoi_thue[phong]

    st.info(
        f"👤 Người thuê: **{ten_khach}**"
    )

    col1, col2 = st.columns(2)

    with col1:

        tien_phong = st.number_input(
            "💵 Tiền phòng",
            min_value=0,
            value=3000000,
            step=100000
        )

        tien_wifi = st.number_input(
            "📶 Tiền WiFi",
            min_value=0,
            value=100000,
            step=10000
        )

        tien_rac = st.number_input(
            "🗑️ Phí rác",
            min_value=0,
            value=50000,
            step=10000
        )

        trang_thai = st.selectbox(
            "💳 Trạng thái thanh toán",
            [
                "❌ Chưa thanh toán",
                "✅ Đã thanh toán"
            ]
        )

    with col2:

        st.markdown("### ⚡ Điện")

        dien_cu = st.number_input(
            "Số điện cũ (kWh)",
            min_value=0,
            value=120
        )

        dien_moi = st.number_input(
            "Số điện mới (kWh)",
            min_value=0,
            value=155
        )

        gia_dien = st.number_input(
            "Giá điện (VNĐ/kWh)",
            min_value=0,
            value=3500,
            step=100
        )

        st.markdown("### 💧 Nước")

        nuoc_cu = st.number_input(
            "Số nước cũ (m³)",
            min_value=0,
            value=10
        )

        nuoc_moi = st.number_input(
            "Số nước mới (m³)",
            min_value=0,
            value=13
        )

        gia_nuoc = st.number_input(
            "Giá nước (VNĐ/m³)",
            min_value=0,
            value=20000,
            step=1000
        )

    st.markdown("</div>", unsafe_allow_html=True)


    if st.button(
        "🧮 TÍNH TIỀN",
        use_container_width=True
    ):

        so_dien = dien_moi - dien_cu

        so_nuoc = nuoc_moi - nuoc_cu

        if so_dien < 0:

            st.error(
                "❌ Số điện mới không được nhỏ hơn số điện cũ."
            )

        elif so_nuoc < 0:

            st.error(
                "❌ Số nước mới không được nhỏ hơn số nước cũ."
            )

        else:

            tien_dien = so_dien * gia_dien

            tien_nuoc = so_nuoc * gia_nuoc

            tong_tien = (

                tien_phong
                + tien_dien
                + tien_nuoc
                + tien_wifi
                + tien_rac

            )

            # LƯU HÓA ĐƠN

            st.session_state.hoa_don_phong[phong] = {

                "phong": phong,

                "nguoi_thue": ten_khach,

                "tien_phong": tien_phong,

                "dien_cu": dien_cu,

                "dien_moi": dien_moi,

                "so_dien": so_dien,

                "gia_dien": gia_dien,

                "tien_dien": tien_dien,

                "nuoc_cu": nuoc_cu,

                "nuoc_moi": nuoc_moi,

                "so_nuoc": so_nuoc,

                "gia_nuoc": gia_nuoc,

                "tien_nuoc": tien_nuoc,

                "wifi": tien_wifi,

                "phi_khac": tien_rac,

                "tong": tong_tien,

                "trang_thai": trang_thai,

                "ngay_tao": datetime.now().strftime(
                    "%d/%m/%Y %H:%M"
                )

            }

            st.success(
                f"✅ Đã tính tiền cho phòng {phong}"
            )

            st.markdown(
                f"""
                <div class="total">

                    <div>TỔNG TIỀN PHÒNG {phong}</div>

                    <div class="total-money">
                        {format_money(tong_tien)}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            # BẢNG CHI TIẾT

            st.subheader("🧾 Chi tiết hóa đơn")

            chi_tiet = {

                "Khoản tiền": [

                    "Tiền phòng",

                    "Tiền điện",

                    "Tiền nước",

                    "WiFi",

                    "Phí rác",

                    "TỔNG CỘNG"

                ],

                "Số tiền": [

                    format_money(tien_phong),

                    format_money(tien_dien),

                    format_money(tien_nuoc),

                    format_money(tien_wifi),

                    format_money(tien_rac),

                    format_money(tong_tien)

                ]

            }

            st.table(chi_tiet)


# =========================================================
# TRANG 2 - QUẢN LÝ TOÀN BỘ PHÒNG
# =========================================================

elif menu == "📋 Quản lý toàn bộ phòng":

    st.subheader("📋 Quản lý toàn bộ phòng")

    if not st.session_state.hoa_don_phong:

        st.info(
            "ℹ️ Chưa có hóa đơn nào được tạo."
        )

    else:

        data = []

        tong_phong = 0
        tong_dien = 0
        tong_nuoc = 0
        tong_phi = 0
        tong_all = 0

        da_thanh_toan = 0
        chua_thanh_toan = 0

        for phong, hd in st.session_state.hoa_don_phong.items():

            phi_khac = (
                hd["wifi"]
                + hd["phi_khac"]
            )

            data.append({

                "STT": len(data) + 1,

                "Phòng": phong,

                "Người thuê": hd["nguoi_thue"],

                "Tiền phòng":
                    format_money(hd["tien_phong"]),

                "Tiền điện":
                    format_money(hd["tien_dien"]),

                "Tiền nước":
                    format_money(hd["tien_nuoc"]),

                "Phí khác":
                    format_money(phi_khac),

                "Tổng tiền":
                    format_money(hd["tong"]),

                "Trạng thái":
                    hd["trang_thai"]

            })

            tong_phong += hd["tien_phong"]

            tong_dien += hd["tien_dien"]

            tong_nuoc += hd["tien_nuoc"]

            tong_phi += phi_khac

            tong_all += hd["tong"]

            if hd["trang_thai"] == "✅ Đã thanh toán":

                da_thanh_toan += 1

            else:

                chua_thanh_toan += 1


        st.dataframe(
            data,
            use_container_width=True,
            hide_index=True
        )


        # =================================================
        # THỐNG KÊ
        # =================================================

        st.subheader("📊 Thống kê doanh thu")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "💵 Tiền phòng",
                format_money(tong_phong)
            )

        with col2:

            st.metric(
                "⚡ Tiền điện",
                format_money(tong_dien)
            )

        with col3:

            st.metric(
                "💧 Tiền nước",
                format_money(tong_nuoc)
            )


        col4, col5, col6 = st.columns(3)

        with col4:

            st.metric(
                "📌 Phí khác",
                format_money(tong_phi)
            )

        with col5:

            st.metric(
                "🏠 Tổng doanh thu",
                format_money(tong_all)
            )

        with col6:

            st.metric(
                "❌ Chưa thanh toán",
                chua_thanh_toan
            )


        col7, col8 = st.columns(2)

        with col7:

            st.success(
                f"✅ Đã thanh toán: {da_thanh_toan} phòng"
            )

        with col8:

            st.warning(
                f"❌ Chưa thanh toán: {chua_thanh_toan} phòng"
            )


# =========================================================
# TRANG 3 - CHATBOT
# =========================================================

elif menu == "🤖 Chatbot TÂM AN":

    st.markdown(
        '<div class="chat-title">🤖 CHATBOT AI TÂM AN</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Trợ lý AI hỗ trợ quản lý phòng trọ và trả lời câu hỏi."
    )


    # =====================================================
    # TRẠNG THÁI API
    # =====================================================

    if client:

        st.success(
            "🟢 Chatbot AI đã được kết nối."
        )

    else:

        st.warning(
            "🟡 Chatbot chưa có API Key. "
            "Bạn vẫn có thể xem giao diện nhưng chưa hỏi AI được."
        )


    # =====================================================
    # THỐNG KÊ NHANH
    # =====================================================

    du_lieu = tao_du_lieu_chatbot()

    thong_ke = du_lieu["thong_ke"]


    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🏠 Phòng đã tính",
            du_lieu["so_phong_da_tinh"]
        )

    with col2:

        st.metric(
            "💰 Doanh thu",
            format_money(
                thong_ke["tong_doanh_thu"]
            )
        )

    with col3:

        st.metric(
            "✅ Đã thanh toán",
            thong_ke["so_phong_da_thanh_toan"]
        )

    with col4:

        st.metric(
            "❌ Chưa thanh toán",
            thong_ke["so_phong_chua_thanh_toan"]
        )


    st.divider()


    # =====================================================
    # CÂU HỎI NHANH
    # =====================================================

    st.subheader("💡 Câu hỏi nhanh")

    col1, col2, col3 = st.columns(3)


    with col1:

        if st.button(
            "💰 Tổng doanh thu",
            use_container_width=True
        ):

            question = (
                "Hãy cho tôi biết tổng doanh thu hiện tại "
                "của tất cả các phòng."
            )

            answer = hoi_chatbot(question)

            st.session_state.chat_history.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            st.session_state.chat_history.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.rerun()


        if st.button(
            "⚡ Tổng tiền điện",
            use_container_width=True
        ):

            question = (
                "Hãy cho tôi biết tổng tiền điện "
                "của tất cả phòng hiện tại."
            )

            answer = hoi_chatbot(question)

            st.session_state.chat_history.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            st.session_state.chat_history.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.rerun()


    with col2:

        if st.button(
            "🏠 Phòng chưa thanh toán",
            use_container_width=True
        ):

            question = (
                "Hãy liệt kê tất cả phòng chưa thanh toán "
                "và số tiền mỗi phòng."
            )

            answer = hoi_chatbot(question)

            st.session_state.chat_history.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            st.session_state.chat_history.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.rerun()


        if st.button(
            "💧 Tổng tiền nước",
            use_container_width=True
        ):

            question = (
                "Hãy cho tôi biết tổng tiền nước "
                "của tất cả phòng hiện tại."
            )

            answer = hoi_chatbot(question)

            st.session_state.chat_history.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            st.session_state.chat_history.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.rerun()


    with col3:

        if st.button(
            "📊 Thống kê phòng",
            use_container_width=True
        ):

            question = (
                "Hãy thống kê tình trạng các phòng hiện tại, "
                "bao gồm số phòng đã tính tiền, "
                "đã thanh toán và chưa thanh toán."
            )

            answer = hoi_chatbot(question)

            st.session_state.chat_history.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            st.session_state.chat_history.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.rerun()


        if st.button(
            "🧮 Cách tính tiền",
            use_container_width=True
        ):

            question = (
                "Hãy giải thích cách hệ thống TÂM AN "
                "tính tổng tiền phòng."
            )

            answer = hoi_chatbot(question)

            st.session_state.chat_history.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            st.session_state.chat_history.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            st.rerun()


    st.divider()


    # =====================================================
    # LỊCH SỬ CHAT
    # =====================================================

    st.subheader("💬 Trò chuyện với AI")

    for message in st.session_state.chat_history:

        if message["role"] == "user":

            st.markdown(
                f"""
                <div class="chat-user">
                    👤 <b>Bạn:</b><br>
                    {message["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="chat-ai">
                    🤖 <b>AI TÂM AN:</b><br>
                    {message["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )


    # =====================================================
    # Ô NHẬP CÂU HỎI
    # =====================================================

    question = st.chat_input(
        "💬 Nhập câu hỏi của bạn..."
    )


    if question:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.spinner("🤖 AI đang suy nghĩ..."):

            answer = hoi_chatbot(question)

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()


    # =====================================================
    # XÓA LỊCH SỬ
    # =====================================================

    if st.button(
        "🗑️ Xóa lịch sử trò chuyện"
    ):

        st.session_state.chat_history = []

        st.rerun()


# =========================================================
# TRANG 4 - THÔNG TIN TÂM AN
# =========================================================

elif menu == "ℹ️ Thông tin TÂM AN":

    st.subheader("ℹ️ Thông tin TÂM AN")

    st.markdown(
        """
        ### 🏠 PHÒNG TRỌ TÂM AN

        TÂM AN là hệ thống quản lý phòng trọ
        giúp chủ nhà theo dõi tiền phòng,
        tiền điện, tiền nước và các khoản phí khác.

        ### 📌 Các khoản được quản lý

        - 💵 Tiền phòng
        - ⚡ Tiền điện
        - 💧 Tiền nước
        - 📶 Tiền WiFi
        - 🗑️ Phí rác
        - 💳 Trạng thái thanh toán

        ### 🤖 Chatbot AI

        Chatbot AI TÂM AN hỗ trợ:

        - Tra cứu doanh thu
        - Kiểm tra phòng chưa thanh toán
        - Tra cứu tiền điện
        - Tra cứu tiền nước
        - Thống kê phòng
        - Giải thích cách tính hóa đơn
        - Trả lời câu hỏi tự do

        ### ❤️ Thông điệp

        **TÂM AN — An tâm khi ở – Minh bạch khi thanh toán.**
        """
    )
