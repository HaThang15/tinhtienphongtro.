import streamlit as st
from datetime import datetime

# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="TÂM AN - Tính tiền phòng trọ",
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
    color: #666;
    font-size: 18px;
    margin-bottom: 25px;
}

.box {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.total {
    background: linear-gradient(135deg, #1f4e79, #3b82b6);
    color: white;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
}

.total-money {
    font-size: 36px;
    font-weight: bold;
}

.chat-user {
    background-color: #dbeafe;
    padding: 12px;
    border-radius: 12px;
    margin: 8px 0;
}

.chat-bot {
    background-color: #f1f5f9;
    padding: 12px;
    border-radius: 12px;
    margin: 8px 0;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TIÊU ĐỀ
# =========================================================

st.markdown(
    '<div class="title">🏠 PHÒNG TRỌ TÂM AN</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ứng dụng tính tiền phòng trọ & trợ lý AI</div>',
    unsafe_allow_html=True
)

# =========================================================
# MENU
# =========================================================

menu = st.sidebar.radio(
    "📌 MENU",
    [
        "🏠 Tính tiền phòng",
        "🤖 Chat Bot AI",
        "ℹ️ Thông tin TÂM AN"
    ]
)

# =========================================================
# HÀM ĐỊNH DẠNG TIỀN
# =========================================================

def format_money(number):
    return f"{number:,.0f} VNĐ".replace(",", ".")


# =========================================================
# TRANG TÍNH TIỀN PHÒNG
# =========================================================

if menu == "🏠 Tính tiền phòng":

    st.subheader("🧾 TÍNH HÓA ĐƠN TIỀN PHÒNG")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown('<div class="box">', unsafe_allow_html=True)

        st.subheader("🏠 Thông tin phòng")

        phong = st.text_input(
            "Số phòng",
            placeholder="Ví dụ: P101"
        )

        ten_khach = st.text_input(
            "Tên người thuê",
            placeholder="Nhập họ và tên"
        )

        tien_phong = st.number_input(
            "💰 Tiền phòng / tháng",
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
            "🗑️ Phí rác / dịch vụ",
            min_value=0,
            value=50000,
            step=10000
        )

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:

        st.markdown('<div class="box">', unsafe_allow_html=True)

        st.subheader("⚡ Điện & 💧 Nước")

        dien_cu = st.number_input(
            "⚡ Chỉ số điện tháng trước",
            min_value=0.0,
            value=0.0,
            step=1.0
        )

        dien_moi = st.number_input(
            "⚡ Chỉ số điện tháng này",
            min_value=0.0,
            value=0.0,
            step=1.0
        )

        gia_dien = st.number_input(
            "💡 Giá điện / kWh",
            min_value=0,
            value=3500,
            step=100
        )

        nuoc_cu = st.number_input(
            "💧 Chỉ số nước tháng trước",
            min_value=0.0,
            value=0.0,
            step=1.0
        )

        nuoc_moi = st.number_input(
            "💧 Chỉ số nước tháng này",
            min_value=0.0,
            value=0.0,
            step=1.0
        )

        gia_nuoc = st.number_input(
            "🚰 Giá nước / m³",
            min_value=0,
            value=15000,
            step=1000
        )

        st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # TÍNH TOÁN
    # =====================================================

    if st.button("🧮 TÍNH TIỀN", use_container_width=True):

        so_dien = dien_moi - dien_cu
        so_nuoc = nuoc_moi - nuoc_cu

        if so_dien < 0:
            st.error("⚠️ Chỉ số điện mới không được nhỏ hơn chỉ số cũ.")
            st.stop()

        if so_nuoc < 0:
            st.error("⚠️ Chỉ số nước mới không được nhỏ hơn chỉ số cũ.")
            st.stop()

        tien_dien = so_dien * gia_dien
        tien_nuoc = so_nuoc * gia_nuoc

        tong_tien = (
            tien_phong
            + tien_dien
            + tien_nuoc
            + tien_wifi
            + tien_rac
        )

        # Lưu thông tin để Bot AI sử dụng
        st.session_state["hoa_don"] = {
            "phong": phong,
            "khach": ten_khach,
            "tien_phong": tien_phong,
            "so_dien": so_dien,
            "gia_dien": gia_dien,
            "tien_dien": tien_dien,
            "so_nuoc": so_nuoc,
            "gia_nuoc": gia_nuoc,
            "tien_nuoc": tien_nuoc,
            "wifi": tien_wifi,
            "rac": tien_rac,
            "tong": tong_tien
        }

        # =================================================
        # HIỂN THỊ HÓA ĐƠN
        # =================================================

        st.success("✅ Đã tính hóa đơn thành công!")

        st.markdown("## 🧾 HÓA ĐƠN PHÒNG TRỌ TÂM AN")

        if phong:
            st.write(f"**🏠 Phòng:** {phong}")

        if ten_khach:
            st.write(f"**👤 Người thuê:** {ten_khach}")

        st.write(
            f"**📅 Ngày lập hóa đơn:** "
            f"{datetime.now().strftime('%d/%m/%Y %H:%M')}"
        )

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🏠 Tiền phòng",
                format_money(tien_phong)
            )

        with col2:
            st.metric(
                "⚡ Tiền điện",
                format_money(tien_dien)
            )

        with col3:
            st.metric(
                "💧 Tiền nước",
                format_money(tien_nuoc)
            )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "📶 WiFi",
                format_money(tien_wifi)
            )

        with col2:
            st.metric(
                "🗑️ Phí dịch vụ",
                format_money(tien_rac)
            )

        st.markdown(
            f"""
            <div class="total">
                <div>TỔNG TIỀN PHẢI THANH TOÁN</div>
                <div class="total-money">
                    {format_money(tong_tien)}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        # =================================================
        # BẢNG CHI TIẾT
        # =================================================

        st.subheader("📋 Chi tiết hóa đơn")

        data = {
            "Khoản phí": [
                "Tiền phòng",
                "Tiền điện",
                "Tiền nước",
                "Tiền WiFi",
                "Phí rác / dịch vụ"
            ],
            "Số lượng": [
                "1 tháng",
                f"{so_dien:.0f} kWh",
                f"{so_nuoc:.0f} m³",
                "1 tháng",
                "1 tháng"
            ],
            "Đơn giá": [
                format_money(tien_phong),
                format_money(gia_dien) + "/kWh",
                format_money(gia_nuoc) + "/m³",
                format_money(tien_wifi),
                format_money(tien_rac)
            ],
            "Thành tiền": [
                format_money(tien_phong),
                format_money(tien_dien),
                format_money(tien_nuoc),
                format_money(tien_wifi),
                format_money(tien_rac)
            ]
        }

        st.table(data)


# =========================================================
# CHAT BOT AI
# =========================================================

elif menu == "🤖 Chat Bot AI":

    st.subheader("🤖 TRỢ LÝ AI - TÂM AN")

    st.info(
        "💬 Bạn có thể hỏi Bot về tiền phòng, điện, nước, WiFi "
        "hoặc các chủ đề khác."
    )

    # Khởi tạo lịch sử chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Hiển thị lịch sử
    for message in st.session_state.messages:

        if message["role"] == "user":

            st.markdown(
                f"""
                <div class="chat-user">
                    👤 <b>Bạn:</b> {message["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="chat-bot">
                    🤖 <b>TÂM AN AI:</b> {message["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

    # Nhập câu hỏi
    question = st.chat_input(
        "Nhập câu hỏi cho TÂM AN AI..."
    )

    if question:

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        q = question.lower()

        # =============================================
        # LẤY HÓA ĐƠN GẦN NHẤT
        # =============================================

        hoa_don = st.session_state.get("hoa_don", None)

        # =============================================
        # BOT XỬ LÝ CÂU HỎI VỀ TIỀN PHÒNG
        # =============================================

        if any(word in q for word in [
            "tổng tiền",
            "tổng",
            "thanh toán",
            "hóa đơn",
            "hoá đơn"
        ]) and hoa_don:

            answer = (
                f"Hóa đơn gần nhất của phòng "
                f"{hoa_don['phong'] or 'chưa nhập'} là "
                f"**{format_money(hoa_don['tong'])}**.\n\n"
                f"🏠 Tiền phòng: {format_money(hoa_don['tien_phong'])}\n\n"
                f"⚡ Tiền điện: {format_money(hoa_don['tien_dien'])}\n\n"
                f"💧 Tiền nước: {format_money(hoa_don['tien_nuoc'])}\n\n"
                f"📶 WiFi: {format_money(hoa_don['wifi'])}\n\n"
                f"🗑️ Phí dịch vụ: {format_money(hoa_don['rac'])}"
            )

        elif any(word in q for word in [
            "tiền điện",
            "tiền điện bao nhiêu",
            "điện"
        ]) and hoa_don:

            answer = (
                f"⚡ Phòng {hoa_don['phong'] or ''} sử dụng "
                f"**{hoa_don['so_dien']:.0f} kWh**.\n\n"
                f"Đơn giá: {format_money(hoa_don['gia_dien'])}/kWh.\n\n"
                f"Tiền điện là **{format_money(hoa_don['tien_dien'])}**."
            )

        elif any(word in q for word in [
            "tiền nước",
            "nước"
        ]) and hoa_don:

            answer = (
                f"💧 Phòng {hoa_don['phong'] or ''} sử dụng "
                f"**{hoa_don['so_nuoc']:.0f} m³** nước.\n\n"
                f"Đơn giá: {format_money(hoa_don['gia_nuoc'])}/m³.\n\n"
                f"Tiền nước là **{format_money(hoa_don['tien_nuoc'])}**."
            )

        elif "wifi" in q:

            if hoa_don:
                answer = (
                    f"📶 Tiền WiFi hiện đang được tính là "
                    f"**{format_money(hoa_don['wifi'])}/tháng**."
                )
            else:
                answer = (
                    "📶 Bạn chưa tạo hóa đơn. "
                    "Thông thường tiền WiFi được nhập tại phần "
                    "'Tính tiền phòng'."
                )

        elif any(word in q for word in [
            "cách tính tiền phòng",
            "tính tiền phòng",
            "tiền trọ"
        ]):

            answer = (
                "🏠 Cách tính tiền phòng TÂM AN:\n\n"
                "**Tổng tiền = Tiền phòng + Tiền điện + "
                "Tiền nước + WiFi + Phí dịch vụ.**\n\n"
                "⚡ Tiền điện = Số điện sử dụng × Đơn giá điện.\n\n"
                "💧 Tiền nước = Số nước sử dụng × Đơn giá nước."
            )

        # =============================================
        # CÂU HỎI CHÀO HỎI
        # =============================================

        elif any(word in q for word in [
            "xin chào",
            "chào",
            "hello",
            "hi"
        ]):

            answer = (
                "👋 Xin chào! Mình là **TÂM AN AI**.\n\n"
                "Mình có thể giúp bạn:\n"
                "🏠 Tính tiền phòng\n"
                "⚡ Tính tiền điện\n"
                "💧 Tính tiền nước\n"
                "📶 Tính tiền WiFi\n"
                "🧾 Kiểm tra hóa đơn\n"
                "💬 Và trả lời các câu hỏi thông thường."
            )

        elif any(word in q for word in [
            "bạn là ai",
            "ai vậy",
            "giới thiệu"
        ]):

            answer = (
                "🤖 Mình là **TÂM AN AI**, trợ lý ảo của "
                "phòng trọ TÂM AN.\n\n"
                "Mình được thiết kế để hỗ trợ người thuê "
                "tra cứu và hiểu các khoản tiền phòng, điện, "
                "nước, WiFi và nhiều vấn đề khác."
            )

        # =============================================
        # CÂU HỎI THỜI GIAN
        # =============================================

        elif "hôm nay" in q:

            answer = (
                f"📅 Hôm nay là "
                f"{datetime.now().strftime('%d/%m/%Y')}."
            )

        # =============================================
        # CÂU HỎI CHUNG
        # =============================================

        elif any(word in q for word in [
            "cảm ơn",
            "thanks"
        ]):

            answer = (
                "😊 Không có gì! TÂM AN AI luôn sẵn sàng "
                "hỗ trợ bạn."
            )

        else:

            answer = (
                "🤖 Mình có thể hỗ trợ nhiều chủ đề cơ bản. "
                "Bạn có thể hỏi mình về:\n\n"
                "🏠 Tiền phòng TÂM AN\n"
                "⚡ Tiền điện\n"
                "💧 Tiền nước\n"
                "📶 WiFi\n"
                "🧾 Hóa đơn\n"
                "💻 Công nghệ\n"
                "📚 Học tập\n"
                "🌎 Kiến thức đời sống\n"
                "💬 Hoặc đặt một câu hỏi bất kỳ."
            )

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.rerun()


# =========================================================
# THÔNG TIN TÂM AN
# =========================================================

elif menu == "ℹ️ Thông tin TÂM AN":

    st.subheader("🏠 GIỚI THIỆU PHÒNG TRỌ TÂM AN")

    st.markdown("""
    ### 🏡 PHÒNG TRỌ TÂM AN

    **TÂM AN** hướng đến xây dựng mô hình phòng trọ
    tiện nghi, minh bạch và thuận tiện cho người thuê.

    ### 💡 Tiện ích

    - 🏠 Phòng trọ
    - ⚡ Điện
    - 💧 Nước
    - 📶 WiFi
    - 🗑️ Dịch vụ vệ sinh
    - 🤖 Trợ lý AI

    ### 🤖 TÂM AN AI

    Trợ lý AI hỗ trợ người thuê:

    - Kiểm tra tiền phòng
    - Tính tiền điện
    - Tính tiền nước
    - Kiểm tra hóa đơn
    - Giải đáp các câu hỏi thường gặp
    - Hỗ trợ kiến thức và thông tin cơ bản

    ### ❤️ TÂM AN

    **An tâm khi ở – Minh bạch khi thanh toán.**
    """)

    st.success(
        "🏠 Cảm ơn bạn đã sử dụng ứng dụng quản lý phòng trọ TÂM AN!"
    )
