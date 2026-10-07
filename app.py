import streamlit as st
from datetime import datetime

# =========================================================
# 1. CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Phòng trọ TÂM AN",
    page_icon="🏠",
    layout="wide"
)

# =========================================================
# 2. CSS GIAO DIỆN
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
    margin-bottom: 20px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
}

.total {
    background: linear-gradient(135deg, #1f4e79, #3b82f6);
    color: white;
    padding: 25px;
    border-radius: 15px;
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
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
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

.chat-title {
    color: #1f4e79;
    font-size: 30px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. ẢNH + TIÊU ĐỀ
# =========================================================

try:
    st.image("anh_tam_an.jpg", use_container_width=True)
except:
    st.warning("⚠️ Không tìm thấy ảnh anh_tam_an.jpg. Bạn hãy đặt ảnh cùng thư mục với app.py.")

st.markdown(
    '<div class="title">🏠 PHÒNG TRỌ TÂM AN</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Hệ thống quản lý và tính tiền phòng trọ</div>',
    unsafe_allow_html=True
)


# =========================================================
# 4. DANH SÁCH PHÒNG
# =========================================================

PHONG_LIST = [
    "P101", "P102", "P103", "P104", "P105",
    "P201", "P202", "P203", "P204", "P205"
]


# =========================================================
# 5. DANH SÁCH NGƯỜI THUÊ
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
# 6. LƯU HÓA ĐƠN
# =========================================================

if "hoa_don_phong" not in st.session_state:
    st.session_state.hoa_don_phong = {}


# =========================================================
# 7. LƯU LỊCH SỬ CHAT
# =========================================================

if "lich_su_chat" not in st.session_state:
    st.session_state.lich_su_chat = []


# =========================================================
# 8. HÀM ĐỊNH DẠNG TIỀN
# =========================================================

def format_money(number):
    return f"{number:,.0f} VNĐ".replace(",", ".")


# =========================================================
# 9. HÀM CHATBOT
# =========================================================

def chatbot_phong_tro(question):

    q = question.lower().strip()

    # -----------------------------------------------------
    # CÂU CHÀO
    # -----------------------------------------------------

    if q in ["xin chào", "chào", "hello", "hi", "alo"]:
        return (
            "🤖 Xin chào! Tôi là Chatbot của PHÒNG TRỌ TÂM AN.<br><br>"
            "Tôi có thể giúp bạn tra cứu thông tin phòng, "
            "người thuê, tiền phòng, tiền điện, tiền nước, "
            "hóa đơn và tình trạng thanh toán."
        )

    # -----------------------------------------------------
    # TÌM PHÒNG CỤ THỂ
    # -----------------------------------------------------

    phong_duoc_hoi = None

    for phong in PHONG_LIST:

        if phong.lower() in q:
            phong_duoc_hoi = phong
            break

    # -----------------------------------------------------
    # XỬ LÝ PHÒNG CỤ THỂ
    # -----------------------------------------------------

    if phong_duoc_hoi:

        phong = phong_duoc_hoi
        ten = st.session_state.nguoi_thue.get(
            phong,
            "Chưa có thông tin"
        )

        # Hỏi người thuê
        if (
            "người thuê" in q
            or "ai thuê" in q
            or "khách" in q
            or "tên" in q
        ):
            return (
                f"🏠 <b>{phong}</b><br>"
                f"👤 Người thuê: <b>{ten}</b>"
            )

        # Nếu chưa có hóa đơn
        if phong not in st.session_state.hoa_don_phong:

            if (
                "thanh toán" in q
                or "đóng tiền" in q
                or "đã đóng" in q
                or "chưa đóng" in q
                or "hóa đơn" in q
                or "tiền" in q
            ):
                return (
                    f"🏠 Phòng <b>{phong}</b><br>"
                    f"👤 Người thuê: {ten}<br><br>"
                    f"⚠️ Phòng này chưa có hóa đơn được lập."
                )

        # Có hóa đơn
        else:

            hd = st.session_state.hoa_don_phong[phong]

            # Trạng thái thanh toán
            if (
                "thanh toán" in q
                or "đóng tiền" in q
                or "đã đóng" in q
                or "chưa đóng" in q
            ):

                return (
                    f"🏠 Phòng: <b>{phong}</b><br>"
                    f"👤 Người thuê: {ten}<br>"
                    f"💰 Tổng tiền: <b>{format_money(hd['tong'])}</b><br>"
                    f"📌 Trạng thái: <b>{hd['trang_thai']}</b>"
                )

            # Hỏi tiền phòng
            if (
                "tiền phòng" in q
                or "giá phòng" in q
                or "phòng bao nhiêu" in q
            ):

                return (
                    f"🏠 Phòng <b>{phong}</b><br>"
                    f"💰 Tiền phòng: "
                    f"<b>{format_money(hd['tien_phong'])}</b>"
                )

            # Hỏi tiền điện
            if "điện" in q:

                return (
                    f"🏠 Phòng <b>{phong}</b><br>"
                    f"⚡ Chỉ số cũ: {hd['dien_cu']} kWh<br>"
                    f"⚡ Chỉ số mới: {hd['dien_moi']} kWh<br>"
                    f"⚡ Số điện sử dụng: {hd['so_dien']} kWh<br>"
                    f"💰 Tiền điện: <b>{format_money(hd['tien_dien'])}</b>"
                )

            # Hỏi tiền nước
            if "nước" in q:

                return (
                    f"🏠 Phòng <b>{phong}</b><br>"
                    f"💧 Chỉ số cũ: {hd['nuoc_cu']} m³<br>"
                    f"💧 Chỉ số mới: {hd['nuoc_moi']} m³<br>"
                    f"💧 Số nước sử dụng: {hd['so_nuoc']} m³<br>"
                    f"💰 Tiền nước: <b>{format_money(hd['tien_nuoc'])}</b>"
                )

            # Hỏi tổng tiền
            if (
                "tổng tiền" in q
                or "hóa đơn" in q
                or "bao nhiêu tiền" in q
                or "phải trả" in q
            ):

                return (
                    f"🏠 <b>HÓA ĐƠN {phong}</b><br><br>"
                    f"👤 Người thuê: {hd['nguoi_thue']}<br>"
                    f"🏠 Tiền phòng: {format_money(hd['tien_phong'])}<br>"
                    f"⚡ Tiền điện: {format_money(hd['tien_dien'])}<br>"
                    f"💧 Tiền nước: {format_money(hd['tien_nuoc'])}<br>"
                    f"📶 WiFi: {format_money(hd['wifi'])}<br>"
                    f"🗑️ Phí khác: {format_money(hd['phi_khac'])}<br>"
                    f"💰 <b>TỔNG: {format_money(hd['tong'])}</b><br>"
                    f"📌 {hd['trang_thai']}"
                )

            # Nếu chỉ hỏi tên phòng
            return (
                f"🏠 Phòng <b>{phong}</b><br>"
                f"👤 Người thuê: {ten}<br>"
                f"ℹ️ Bạn có thể hỏi thêm về tiền phòng, "
                f"điện, nước, hóa đơn hoặc thanh toán."
            )

    # -----------------------------------------------------
    # TỔNG SỐ PHÒNG
    # -----------------------------------------------------

    if (
        "bao nhiêu phòng" in q
        or "số phòng" in q
        or "có mấy phòng" in q
    ):

        return (
            f"🏠 PHÒNG TRỌ TÂM AN hiện có "
            f"<b>{len(PHONG_LIST)} phòng</b>.<br><br>"
            f"📋 Danh sách: {', '.join(PHONG_LIST)}"
        )

    # -----------------------------------------------------
    # PHÒNG ĐÃ THANH TOÁN
    # -----------------------------------------------------

    if (
        "đã thanh toán" in q
        or "đã đóng tiền" in q
        or "phòng đã đóng" in q
    ):

        danh_sach = []

        for phong, hd in st.session_state.hoa_don_phong.items():

            if "Đã thanh toán" in hd["trang_thai"]:
                danh_sach.append(phong)

        if danh_sach:

            return (
                "✅ Các phòng đã thanh toán:<br><br>"
                + ", ".join(danh_sach)
            )

        return "ℹ️ Hiện chưa có phòng nào được ghi nhận là đã thanh toán."

    # -----------------------------------------------------
    # PHÒNG CHƯA THANH TOÁN
    # -----------------------------------------------------

    if (
        "chưa thanh toán" in q
        or "chưa đóng tiền" in q
        or "phòng chưa đóng" in q
    ):

        danh_sach = []

        for phong, hd in st.session_state.hoa_don_phong.items():

            if "Chưa thanh toán" in hd["trang_thai"]:
                danh_sach.append(phong)

        if danh_sach:

            return (
                "❌ Các phòng chưa thanh toán:<br><br>"
                + ", ".join(danh_sach)
            )

        return "🎉 Hiện không có phòng nào được ghi nhận là chưa thanh toán."

    # -----------------------------------------------------
    # TỔNG DOANH THU
    # -----------------------------------------------------

    if (
        "tổng doanh thu" in q
        or "doanh thu" in q
        or "tổng tiền thu" in q
    ):

        tong = 0

        for hd in st.session_state.hoa_don_phong.values():
            tong += hd["tong"]

        return (
            f"💰 Tổng doanh thu hiện tại là:<br><br>"
            f"<div style='font-size:28px; font-weight:bold;'>"
            f"{format_money(tong)}"
            f"</div>"
        )

    # -----------------------------------------------------
    # TỔNG TIỀN ĐIỆN
    # -----------------------------------------------------

    if (
        "tổng tiền điện" in q
        or "doanh thu điện" in q
    ):

        tong_dien = 0

        for hd in st.session_state.hoa_don_phong.values():
            tong_dien += hd["tien_dien"]

        return (
            f"⚡ Tổng tiền điện của tất cả phòng là:<br>"
            f"<b>{format_money(tong_dien)}</b>"
        )

    # -----------------------------------------------------
    # TỔNG TIỀN NƯỚC
    # -----------------------------------------------------

    if (
        "tổng tiền nước" in q
        or "doanh thu nước" in q
    ):

        tong_nuoc = 0

        for hd in st.session_state.hoa_don_phong.values():
            tong_nuoc += hd["tien_nuoc"]

        return (
            f"💧 Tổng tiền nước của tất cả phòng là:<br>"
            f"<b>{format_money(tong_nuoc)}</b>"
        )

    # -----------------------------------------------------
    # THỐNG KÊ
    # -----------------------------------------------------

    if (
        "thống kê" in q
        or "tình hình phòng" in q
        or "tổng quan" in q
    ):

        tong_phong = len(PHONG_LIST)
        co_hoa_don = len(st.session_state.hoa_don_phong)

        da_thanh_toan = 0
        chua_thanh_toan = 0

        for hd in st.session_state.hoa_don_phong.values():

            if "Đã thanh toán" in hd["trang_thai"]:
                da_thanh_toan += 1
            else:
                chua_thanh_toan += 1

        return (
            f"📊 <b>THỐNG KÊ PHÒNG TRỌ TÂM AN</b><br><br>"
            f"🏠 Tổng số phòng: <b>{tong_phong}</b><br>"
            f"🧾 Phòng đã lập hóa đơn: <b>{co_hoa_don}</b><br>"
            f"✅ Đã thanh toán: <b>{da_thanh_toan}</b><br>"
            f"❌ Chưa thanh toán: <b>{chua_thanh_toan}</b>"
        )

    # -----------------------------------------------------
    # CÁCH TÍNH TIỀN
    # -----------------------------------------------------

    if (
        "tính tiền" in q
        or "cách tính" in q
        or "tính như thế nào" in q
    ):

        return (
            "🧮 <b>Cách tính tiền phòng:</b><br><br>"
            "🏠 Tiền phòng = Giá phòng<br>"
            "⚡ Tiền điện = Số điện sử dụng × Giá điện<br>"
            "💧 Tiền nước = Số nước sử dụng × Giá nước<br>"
            "💰 Tổng tiền = Tiền phòng + Tiền điện + "
            "Tiền nước + WiFi + Phí khác"
        )

    # -----------------------------------------------------
    # GIÁ ĐIỆN
    # -----------------------------------------------------

    if (
        "giá điện" in q
        or "điện bao nhiêu" in q
    ):

        if st.session_state.hoa_don_phong:

            hd = next(
                iter(st.session_state.hoa_don_phong.values())
            )

            return (
                f"⚡ Giá điện đang sử dụng trong hóa đơn là "
                f"<b>{format_money(hd['gia_dien'])}/kWh</b>."
            )

        return (
            "⚡ Hiện chưa có hóa đơn để xác định giá điện."
        )

    # -----------------------------------------------------
    # GIÁ NƯỚC
    # -----------------------------------------------------

    if (
        "giá nước" in q
        or "nước bao nhiêu" in q
    ):

        if st.session_state.hoa_don_phong:

            hd = next(
                iter(st.session_state.hoa_don_phong.values())
            )

            return (
                f"💧 Giá nước đang sử dụng trong hóa đơn là "
                f"<b>{format_money(hd['gia_nuoc'])}/m³</b>."
            )

        return (
            "💧 Hiện chưa có hóa đơn để xác định giá nước."
        )

    # -----------------------------------------------------
    # CÂU HỎI VỀ DANH SÁCH PHÒNG
    # -----------------------------------------------------

    if (
        "danh sách phòng" in q
        or "các phòng" in q
        or "phòng gồm" in q
    ):

        return (
            "🏠 Danh sách phòng:<br><br>"
            + " • ".join(PHONG_LIST)
        )

    # -----------------------------------------------------
    # CÂU HỎI NGOÀI PHẠM VI
    # -----------------------------------------------------

    return (
        "🤖 Xin lỗi! Tôi là Chatbot của "
        "<b>PHÒNG TRỌ TÂM AN</b>.<br><br>"
        "Tôi chỉ hỗ trợ các câu hỏi liên quan đến phòng trọ như:<br>"
        "🏠 Danh sách phòng<br>"
        "👤 Người thuê<br>"
        "💰 Tiền phòng<br>"
        "⚡ Tiền điện<br>"
        "💧 Tiền nước<br>"
        "🧾 Hóa đơn<br>"
        "✅ Tình trạng thanh toán<br>"
        "📊 Doanh thu và thống kê"
    )


# =========================================================
# 10. MENU
# =========================================================

menu = st.sidebar.radio(
    "📌 MENU",
    [
        "🏠 Tính tiền phòng",
        "📋 Quản lý toàn bộ phòng",
        "🤖 Chatbot phòng trọ",
        "ℹ️ Thông tin TÂM AN"
    ]
)


# =========================================================
# 11. TRANG TÍNH TIỀN PHÒNG
# =========================================================

if menu == "🏠 Tính tiền phòng":

    st.subheader("🧮 TÍNH TIỀN PHÒNG")

    st.markdown('<div class="box">', unsafe_allow_html=True)

    phong = st.selectbox(
        "🏠 Chọn phòng",
        PHONG_LIST
    )

    ten_khach = st.session_state.nguoi_thue.get(
        phong,
        "Chưa có thông tin"
    )

    st.info(f"👤 Người thuê: **{ten_khach}**")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 🏠 TIỀN PHÒNG")

        tien_phong = st.number_input(
            "Tiền phòng (VNĐ)",
            min_value=0,
            value=3000000,
            step=100000
        )

        tien_wifi = st.number_input(
            "Tiền WiFi (VNĐ)",
            min_value=0,
            value=100000,
            step=10000
        )

        tien_rac = st.number_input(
            "Phí rác / phí khác (VNĐ)",
            min_value=0,
            value=50000,
            step=10000
        )

    with col2:

        st.markdown("### ⚡ TIỀN ĐIỆN")

        dien_cu = st.number_input(
            "Chỉ số điện cũ (kWh)",
            min_value=0,
            value=120
        )

        dien_moi = st.number_input(
            "Chỉ số điện mới (kWh)",
            min_value=0,
            value=155
        )

        gia_dien = st.number_input(
            "Giá điện (VNĐ/kWh)",
            min_value=0,
            value=3500,
            step=100
        )

    col3, col4 = st.columns(2)

    with col3:

        st.markdown("### 💧 TIỀN NƯỚC")

        nuoc_cu = st.number_input(
            "Chỉ số nước cũ (m³)",
            min_value=0,
            value=10
        )

        nuoc_moi = st.number_input(
            "Chỉ số nước mới (m³)",
            min_value=0,
            value=13
        )

        gia_nuoc = st.number_input(
            "Giá nước (VNĐ/m³)",
            min_value=0,
            value=20000,
            step=1000
        )

    with col4:

        st.markdown("### 📌 THANH TOÁN")

        trang_thai = st.selectbox(
            "Trạng thái",
            [
                "❌ Chưa thanh toán",
                "✅ Đã thanh toán"
            ]
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
                "❌ Chỉ số điện mới không được nhỏ hơn chỉ số điện cũ."
            )

        elif so_nuoc < 0:

            st.error(
                "❌ Chỉ số nước mới không được nhỏ hơn chỉ số nước cũ."
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

            # Lưu hóa đơn
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
                f"✅ Đã tạo hóa đơn cho phòng {phong}"
            )

            # Hiển thị tổng tiền
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

            st.markdown("### 🧾 CHI TIẾT HÓA ĐƠN")

            du_lieu = {

                "Nội dung": [
                    "Tiền phòng",
                    "Tiền điện",
                    "Tiền nước",
                    "WiFi",
                    "Phí khác",
                    "TỔNG TIỀN"
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

            st.table(du_lieu)

            st.info(
                f"📌 Trạng thái: {trang_thai}"
            )


# =========================================================
# 12. TRANG QUẢN LÝ TOÀN BỘ PHÒNG
# =========================================================

elif menu == "📋 Quản lý toàn bộ phòng":

    st.subheader("📋 QUẢN LÝ TOÀN BỘ PHÒNG")

    if not st.session_state.hoa_don_phong:

        st.info(
            "ℹ️ Chưa có hóa đơn nào được tạo."
        )

    else:

        danh_sach = []

        tong_phong = 0
        tong_dien = 0
        tong_nuoc = 0
        tong_phi = 0
        tong_all = 0

        so_da_thanh_toan = 0
        so_chua_thanh_toan = 0

        for phong, hd in st.session_state.hoa_don_phong.items():

            phi_khac = (
                hd["wifi"] + hd["phi_khac"]
            )

            danh_sach.append({

                "STT": len(danh_sach) + 1,

                "Phòng": phong,

                "Người thuê": hd["nguoi_thue"],

                "Tiền phòng": format_money(
                    hd["tien_phong"]
                ),

                "Tiền điện": format_money(
                    hd["tien_dien"]
                ),

                "Tiền nước": format_money(
                    hd["tien_nuoc"]
                ),

                "Phí khác": format_money(
                    phi_khac
                ),

                "Tổng tiền": format_money(
                    hd["tong"]
                ),

                "Trạng thái": hd["trang_thai"]
            })

            tong_phong += hd["tien_phong"]

            tong_dien += hd["tien_dien"]

            tong_nuoc += hd["tien_nuoc"]

            tong_phi += phi_khac

            tong_all += hd["tong"]

            if "Đã thanh toán" in hd["trang_thai"]:

                so_da_thanh_toan += 1

            else:

                so_chua_thanh_toan += 1

        st.dataframe(
            danh_sach,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### 💰 TỔNG HỢP")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "🏠 Tiền phòng",
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
                "📋 Phí khác",
                format_money(tong_phi)
            )

        with col5:

            st.metric(
                "💰 TỔNG DOANH THU",
                format_money(tong_all)
            )

        with col6:

            st.metric(
                "❌ Chưa thanh toán",
                so_chua_thanh_toan
            )

        st.success(
            f"✅ Đã thanh toán: {so_da_thanh_toan} phòng"
        )


# =========================================================
# 13. CHATBOT PHÒNG TRỌ
# =========================================================

elif menu == "🤖 Chatbot phòng trọ":

    st.markdown(
        '<div class="chat-title">🤖 CHATBOT PHÒNG TRỌ TÂM AN</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Chatbot này hoạt động bằng các câu trả lời được lập trình sẵn "
        "và **chỉ hỗ trợ các câu hỏi liên quan đến phòng trọ TÂM AN**."
    )

    st.markdown("---")

    # -----------------------------------------------------
    # CÂU HỎI NHANH
    # -----------------------------------------------------

    st.markdown("### 💡 Câu hỏi nhanh")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "🏠 Có bao nhiêu phòng?",
            use_container_width=True
        ):

            answer = chatbot_phong_tro(
                "Có bao nhiêu phòng?"
            )

            st.session_state.lich_su_chat.append(
                ("Bạn", "Có bao nhiêu phòng?")
            )

            st.session_state.lich_su_chat.append(
                ("Bot", answer)
            )

    with col2:

        if st.button(
            "💰 Tổng doanh thu",
            use_container_width=True
        ):

            answer = chatbot_phong_tro(
                "Tổng doanh thu là bao nhiêu?"
            )

            st.session_state.lich_su_chat.append(
                ("Bạn", "Tổng doanh thu là bao nhiêu?")
            )

            st.session_state.lich_su_chat.append(
                ("Bot", answer)
            )

    with col3:

        if st.button(
            "❌ Phòng chưa thanh toán",
            use_container_width=True
        ):

            answer = chatbot_phong_tro(
                "Phòng chưa thanh toán"
            )

            st.session_state.lich_su_chat.append(
                ("Bạn", "Phòng chưa thanh toán")
            )

            st.session_state.lich_su_chat.append(
                ("Bot", answer)
            )

    # -----------------------------------------------------
    # Ô NHẬP CHAT
    # -----------------------------------------------------

    question = st.chat_input(
        "💬 Nhập câu hỏi về phòng trọ..."
    )

    if question:

        answer = chatbot_phong_tro(question)

        st.session_state.lich_su_chat.append(
            ("Bạn", question)
        )

        st.session_state.lich_su_chat.append(
            ("Bot", answer)
        )

    # -----------------------------------------------------
    # HIỂN THỊ LỊCH SỬ
    # -----------------------------------------------------

    if st.session_state.lich_su_chat:

        st.markdown("### 💬 Lịch sử trò chuyện")

        for sender, message in st.session_state.lich_su_chat:

            if sender == "Bạn":

                st.markdown(
                    f"""
                    <div class="chat-user">
                        👤 <b>Bạn:</b><br>
                        {message}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div class="chat-bot">
                        🤖 <b>Bot:</b><br>
                        {message}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # -----------------------------------------------------
    # XÓA LỊCH SỬ
    # -----------------------------------------------------

    if st.button(
        "🗑️ Xóa lịch sử trò chuyện"
    ):

        st.session_state.lich_su_chat = []

        st.rerun()


# =========================================================
# 14. THÔNG TIN TÂM AN
# =========================================================

elif menu == "ℹ️ Thông tin TÂM AN":

    st.subheader("ℹ️ THÔNG TIN PHÒNG TRỌ TÂM AN")

    st.markdown(
        """
        <div class="box">

        ### 🏠 PHÒNG TRỌ TÂM AN

        Hệ thống hỗ trợ quản lý phòng trọ và tính tiền
        hàng tháng cho người thuê.

        ### 📋 Các khoản được quản lý

        - 🏠 Tiền phòng
        - ⚡ Tiền điện
        - 💧 Tiền nước
        - 📶 Tiền WiFi
        - 🗑️ Phí rác / phí khác
        - 🧾 Hóa đơn
        - ✅ Trạng thái thanh toán

        ### 🤖 Chatbot

        Chatbot hỗ trợ tra cứu:

        - Danh sách phòng
        - Người thuê
        - Tiền phòng
        - Tiền điện
        - Tiền nước
        - Tổng tiền hóa đơn
        - Phòng đã thanh toán
        - Phòng chưa thanh toán
        - Tổng doanh thu
        - Thống kê phòng

        Chatbot **không sử dụng OpenAI hoặc API AI**.
        Các câu trả lời được lập trình sẵn trong ứng dụng.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="total">

            <div style="font-size:25px; font-weight:bold;">
                ❤️ TÂM AN
            </div>

            <div style="font-size:18px; margin-top:10px;">
                An tâm khi ở – Minh bạch khi thanh toán.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )
