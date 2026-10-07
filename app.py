import streamlit as st
from datetime import datetime

# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="TÂM AN - Quản lý phòng trọ",
    page_icon="🏠",
    layout="wide"
)

# =========================================================
# CSS
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
# DỮ LIỆU PHÒNG
# =========================================================

PHONG_LIST = [
    "P101",
    "P102",
    "P103",
    "P104",
    "P105",
    "P201",
    "P202",
    "P203",
    "P204",
    "P205"
]

# =========================================================
# DỮ LIỆU NGƯỜI THUÊ
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
# DỮ LIỆU HÓA ĐƠN
# =========================================================

if "hoa_don_phong" not in st.session_state:
    st.session_state.hoa_don_phong = {}

# =========================================================
# HÀM ĐỊNH DẠNG TIỀN
# =========================================================

def format_money(number):
    return f"{number:,.0f} VNĐ".replace(",", ".")


# =========================================================
# TIÊU ĐỀ
# =========================================================

st.markdown(
    '<div class="title">🏠 PHÒNG TRỌ TÂM AN</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Hệ thống quản lý phòng trọ & trợ lý AI</div>',
    unsafe_allow_html=True
)

# =========================================================
# MENU
# =========================================================

menu = st.sidebar.radio(
    "📌 MENU",
    [
        "🏠 Tính tiền phòng",
        "📋 Quản lý toàn bộ phòng",
        "🤖 BOT QUẢN LÝ TÂM AN",
        "ℹ️ Thông tin TÂM AN"
    ]
)


# =========================================================
# 1. TÍNH TIỀN PHÒNG
# =========================================================

if menu == "🏠 Tính tiền phòng":

    st.subheader("🧾 TÍNH TIỀN PHÒNG")

    st.markdown('<div class="box">', unsafe_allow_html=True)

    # =====================================================
    # CHỌN PHÒNG BẰNG DANH SÁCH
    # =====================================================

    phong = st.selectbox(
        "🏠 Chọn phòng",
        PHONG_LIST
    )

    ten_khach = st.session_state.nguoi_thue.get(
        phong,
        "Chưa cập nhật"
    )

    st.info(
        f"👤 Người thuê phòng {phong}: **{ten_khach}**"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # THÔNG TIN THANH TOÁN
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown('<div class="box">', unsafe_allow_html=True)

        st.subheader("🏠 Tiền phòng & dịch vụ")

        tien_phong = st.number_input(
            "💰 Tiền phòng / tháng",
            min_value=0,
            value=3000000,
            step=100000,
            key=f"tien_phong_{phong}"
        )

        tien_wifi = st.number_input(
            "📶 Tiền WiFi",
            min_value=0,
            value=100000,
            step=10000,
            key=f"wifi_{phong}"
        )

        tien_rac = st.number_input(
            "🗑️ Phí dịch vụ / rác",
            min_value=0,
            value=50000,
            step=10000,
            key=f"rac_{phong}"
        )

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:

        st.markdown('<div class="box">', unsafe_allow_html=True)

        st.subheader("⚡ Điện & 💧 Nước")

        dien_cu = st.number_input(
            "⚡ Điện tháng trước (kWh)",
            min_value=0.0,
            value=120.0,
            step=1.0,
            key=f"dien_cu_{phong}"
        )

        dien_moi = st.number_input(
            "⚡ Điện tháng này (kWh)",
            min_value=0.0,
            value=155.0,
            step=1.0,
            key=f"dien_moi_{phong}"
        )

        gia_dien = st.number_input(
            "💡 Giá điện / kWh",
            min_value=0,
            value=3500,
            step=100,
            key=f"gia_dien_{phong}"
        )

        nuoc_cu = st.number_input(
            "💧 Nước tháng trước (m³)",
            min_value=0.0,
            value=10.0,
            step=1.0,
            key=f"nuoc_cu_{phong}"
        )

        nuoc_moi = st.number_input(
            "💧 Nước tháng này (m³)",
            min_value=0.0,
            value=13.0,
            step=1.0,
            key=f"nuoc_moi_{phong}"
        )

        gia_nuoc = st.number_input(
            "🚰 Giá nước / m³",
            min_value=0,
            value=20000,
            step=1000,
            key=f"gia_nuoc_{phong}"
        )

        st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # TRẠNG THÁI THANH TOÁN
    # =====================================================

    trang_thai = st.selectbox(
        "💳 Trạng thái thanh toán",
        [
            "❌ Chưa thanh toán",
            "✅ Đã thanh toán"
        ],
        key=f"trang_thai_{phong}"
    )

    # =====================================================
    # NÚT TÍNH TIỀN
    # =====================================================

    if st.button(
        "🧮 TÍNH TIỀN PHÒNG",
        use_container_width=True
    ):

        so_dien = dien_moi - dien_cu
        so_nuoc = nuoc_moi - nuoc_cu

        if so_dien < 0:

            st.error(
                "⚠️ Điện tháng này không được nhỏ hơn tháng trước."
            )

        elif so_nuoc < 0:

            st.error(
                "⚠️ Nước tháng này không được nhỏ hơn tháng trước."
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

                "trang_thai": trang_thai
            }

            st.success(
                f"✅ Đã tính tiền cho phòng {phong}"
            )

            # =================================================
            # HÓA ĐƠN
            # =================================================

            st.markdown(
                f"""
                <div class="total">

                    <div>
                    TỔNG TIỀN PHÒNG {phong}
                    </div>

                    <div class="total-money">
                    {format_money(tong_tien)}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

            st.subheader("📋 Chi tiết hóa đơn")

            st.table({

                "Khoản phí": [
                    "Tiền phòng",
                    "Tiền điện",
                    "Tiền nước",
                    "WiFi",
                    "Phí khác"
                ],

                "Thành tiền": [
                    format_money(tien_phong),
                    format_money(tien_dien),
                    format_money(tien_nuoc),
                    format_money(tien_wifi),
                    format_money(tien_rac)
                ]
            })

            if trang_thai == "✅ Đã thanh toán":

                st.success(
                    "💚 Phòng này đã thanh toán."
                )

            else:

                st.warning(
                    "🔴 Phòng này chưa thanh toán."
                )


# =========================================================
# 2. QUẢN LÝ TOÀN BỘ PHÒNG
# =========================================================

elif menu == "📋 Quản lý toàn bộ phòng":

    st.subheader("📋 QUẢN LÝ TOÀN BỘ DÃY PHÒNG TÂM AN")

    if len(st.session_state.hoa_don_phong) == 0:

        st.info(
            "ℹ️ Chưa có dữ liệu hóa đơn. "
            "Hãy tính tiền từng phòng trước."
        )

    else:

        data = []

        tong_phong = 0
        tong_dien = 0
        tong_nuoc = 0
        tong_phi = 0
        tong_all = 0

        so_chua_thanh_toan = 0

        for phong, hd in st.session_state.hoa_don_phong.items():

            data.append({

                "STT":
                    len(data) + 1,

                "Phòng":
                    phong,

                "Người thuê":
                    hd["nguoi_thue"],

                "Tiền phòng":
                    format_money(hd["tien_phong"]),

                "Tiền điện":
                    format_money(hd["tien_dien"]),

                "Tiền nước":
                    format_money(hd["tien_nuoc"]),

                "Phí khác":
                    format_money(
                        hd["wifi"] + hd["phi_khac"]
                    ),

                "Tổng tiền":
                    format_money(hd["tong"]),

                "Trạng thái":
                    hd["trang_thai"]
            })

            tong_phong += hd["tien_phong"]
            tong_dien += hd["tien_dien"]
            tong_nuoc += hd["tien_nuoc"]

            tong_phi += (
                hd["wifi"]
                + hd["phi_khac"]
            )

            tong_all += hd["tong"]

            if hd["trang_thai"] == "❌ Chưa thanh toán":

                so_chua_thanh_toan += 1

        st.dataframe(
            data,
            use_container_width=True,
            hide_index=True
        )

        # =====================================================
        # TỔNG HỢP
        # =====================================================

        st.subheader("📊 TỔNG HỢP DOANH THU")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "🏠 Tổng tiền phòng",
                format_money(tong_phong)
            )

        with c2:

            st.metric(
                "⚡ Tổng tiền điện",
                format_money(tong_dien)
            )

        with c3:

            st.metric(
                "💧 Tổng tiền nước",
                format_money(tong_nuoc)
            )

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "📶 + 🗑️ Phí dịch vụ",
                format_money(tong_phi)
            )

        with c2:

            st.metric(
                "💰 TỔNG DOANH THU",
                format_money(tong_all)
            )

        with c3:

            st.metric(
                "🔴 Chưa thanh toán",
                f"{so_chua_thanh_toan} phòng"
            )


# =========================================================
# 3. BOT QUẢN LÝ TÂM AN
# =========================================================

elif menu == "🤖 BOT QUẢN LÝ TÂM AN":

    st.subheader("🤖 BOT QUẢN LÝ PHÒNG TRỌ TÂM AN")

    st.info(
        "💬 Bạn có thể hỏi Bot về phòng, người thuê, "
        "tiền điện, tiền nước, tổng tiền hoặc trạng thái thanh toán."
    )

    # =====================================================
    # HƯỚNG DẪN
    # =====================================================

    with st.expander("📖 Xem các câu lệnh Bot có thể hiểu"):

        st.markdown("""
### 🔹 Tra cứu phòng

- `Phòng 101`
- `Phòng P101`
- `Cho tôi xem phòng P102`

### 🔹 Tính tiền

- `Tính tiền phòng P101`
- `Phòng P101 hết bao nhiêu tiền?`
- `Tiền điện phòng P101 bao nhiêu?`
- `Tiền nước phòng P102 bao nhiêu?`

### 🔹 Tổng hợp

- `Tổng doanh thu`
- `Có bao nhiêu phòng chưa thanh toán?`
- `Tổng tiền điện tháng này`

### 🔹 Kiểm tra

- `Kiểm tra phòng P101`
- `Kiểm tra số liệu P102`

### 🔹 Nhắc thanh toán

- `Phòng nào chưa thanh toán?`
- `Nhắc tiền phòng P101`
        """)

    # =====================================================
    # LỊCH SỬ CHAT
    # =====================================================

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []

    for msg in st.session_state.chat_history:

        if msg["role"] == "user":

            st.markdown(
                f"""
                <div class="chat-user">
                👤 <b>Bạn:</b> {msg["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="chat-bot">
                🤖 <b>TÂM AN BOT:</b><br>
                {msg["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

    # =====================================================
    # NHẬP CÂU HỎI
    # =====================================================

    question = st.chat_input(
        "Nhập yêu cầu quản lý phòng trọ..."
    )

    if question:

        st.session_state.chat_history.append({

            "role": "user",

            "content": question
        })

        q = question.lower()

        # =================================================
        # TÌM PHÒNG
        # =================================================

        phong_tim = None

        for phong in PHONG_LIST:

            if phong.lower() in q:

                phong_tim = phong

                break

            # Cho phép nhập "phòng 101"
            if phong[1:] in q:

                phong_tim = phong

                break

        # =================================================
        # TRA CỨU PHÒNG
        # =================================================

        if phong_tim and phong_tim in st.session_state.hoa_don_phong:

            hd = st.session_state.hoa_don_phong[phong_tim]

            if any(x in q for x in [
                "phòng",
                "tra cứu",
                "thông tin",
                "kiểm tra"
            ]):

                answer = f"""
### 🏠 THÔNG TIN PHÒNG {phong_tim}

| Nội dung | Thông tin |
|---|---:|
| Người thuê | {hd['nguoi_thue']} |
| Tiền phòng | {format_money(hd['tien_phong'])} |
| Điện sử dụng | {hd['so_dien']:.0f} kWh |
| Tiền điện | {format_money(hd['tien_dien'])} |
| Nước sử dụng | {hd['so_nuoc']:.0f} m³ |
| Tiền nước | {format_money(hd['tien_nuoc'])} |
| Phí WiFi | {format_money(hd['wifi'])} |
| Phí khác | {format_money(hd['phi_khac'])} |
| **Tổng tiền** | **{format_money(hd['tong'])}** |
| Trạng thái | {hd['trang_thai']} |
"""

            else:

                answer = f"""
Phòng **{phong_tim}** có tổng tiền tháng này là:

💰 **{format_money(hd['tong'])}**

Trong đó:

🏠 Tiền phòng: {format_money(hd['tien_phong'])}

⚡ Tiền điện: {format_money(hd['tien_dien'])}

💧 Tiền nước: {format_money(hd['tien_nuoc'])}

📶 WiFi: {format_money(hd['wifi'])}

🗑️ Phí khác: {format_money(hd['phi_khac'])}

💳 Trạng thái: {hd['trang_thai']}
"""

        # =================================================
        # PHÒNG CHƯA CÓ HÓA ĐƠN
        # =================================================

        elif phong_tim:

            answer = f"""
⚠️ Phòng **{phong_tim}** hiện chưa có hóa đơn.

Vui lòng vào:

**🏠 Tính tiền phòng → Chọn phòng {phong_tim}**

Sau đó nhập chỉ số điện, nước và các khoản phí.
"""

        # =================================================
        # TỔNG DOANH THU
        # =================================================

        elif any(x in q for x in [
            "tổng doanh thu",
            "doanh thu",
            "tổng tiền toàn bộ",
            "tổng tiền dãy"
        ]):

            if not st.session_state.hoa_don_phong:

                answer = "⚠️ Hiện chưa có dữ liệu hóa đơn."

            else:

                tong = sum(
                    hd["tong"]
                    for hd in
                    st.session_state.hoa_don_phong.values()
                )

                answer = f"""
### 💰 TỔNG DOANH THU TÂM AN

Tổng số tiền phải thu của các phòng đã lập hóa đơn:

## **{format_money(tong)}**
"""

        # =================================================
        # PHÒNG CHƯA THANH TOÁN
        # =================================================

        elif any(x in q for x in [
            "chưa thanh toán",
            "chưa trả",
            "chưa đóng",
            "nợ"
        ]):

            ds = []

            for phong, hd in st.session_state.hoa_don_phong.items():

                if hd["trang_thai"] == "❌ Chưa thanh toán":

                    ds.append(
                        f"| {phong} | "
                        f"{hd['nguoi_thue']} | "
                        f"{format_money(hd['tong'])} |"
                    )

            if ds:

                answer = """
### 🔴 DANH SÁCH CHƯA THANH TOÁN

| Phòng | Người thuê | Tổng tiền |
|---|---|---:|
""" + "\n".join(ds)

            else:

                answer = "✅ Hiện tại không có phòng nào chưa thanh toán."

        # =================================================
        # NHẮC THANH TOÁN
        # =================================================

        elif any(x in q for x in [
            "nhắc tiền",
            "nhắc thanh toán",
            "nhắc phòng"
        ]) and phong_tim:

            if phong_tim in st.session_state.hoa_don_phong:

                hd = st.session_state.hoa_don_phong[phong_tim]

                answer = f"""
### 📢 TIN NHẮN NHẮC THANH TOÁN

"Phòng **{phong_tim}** thân mến, tiền phòng tháng này là
**{format_money(hd['tong'])}**.

Vui lòng thanh toán đúng hạn. Cảm ơn bạn! ❤️"
"""

            else:

                answer = f"⚠️ Phòng {phong_tim} chưa có hóa đơn."

        # =================================================
        # CHÀO HỎI
        # =================================================

        elif any(x in q for x in [
            "xin chào",
            "chào",
            "hello",
            "hi"
        ]):

            answer = """
👋 Xin chào!

Mình là **BOT QUẢN LÝ PHÒNG TRỌ TÂM AN**.

Mình có thể giúp bạn:

🏠 Tra cứu phòng

👤 Tra cứu người thuê

⚡ Tính tiền điện

💧 Tính tiền nước

💰 Tính tổng tiền

📊 Tổng hợp doanh thu

🔴 Kiểm tra phòng chưa thanh toán

📢 Tạo tin nhắn nhắc thanh toán
"""

        # =================================================
        # KHÔNG HIỂU
        # =================================================

        else:

            answer = """
🤖 Mình chưa hiểu yêu cầu.

Bạn có thể thử:

• `Phòng P101`

• `Tính tiền phòng P101`

• `Kiểm tra phòng P102`

• `Tổng doanh thu`

• `Phòng nào chưa thanh toán?`

• `Nhắc tiền phòng P101`
"""

        st.session_state.chat_history.append({

            "role": "assistant",

            "content": answer
        })

        st.rerun()


# =========================================================
# 4. THÔNG TIN TÂM AN
# =========================================================

elif menu == "ℹ️ Thông tin TÂM AN":

    st.subheader("🏠 PHÒNG TRỌ TÂM AN")

    st.markdown("""
### 🏡 TÂM AN

Hệ thống quản lý phòng trọ TÂM AN được xây dựng nhằm:

- Quản lý danh sách phòng.
- Quản lý người thuê.
- Tính tiền phòng.
- Tính tiền điện.
- Tính tiền nước.
- Quản lý WiFi và các khoản phí khác.
- Theo dõi tình trạng thanh toán.
- Tổng hợp doanh thu.
- Hỗ trợ bằng BOT quản lý AI.

### ❤️ TÂM AN

**An tâm khi ở – Minh bạch khi thanh toán.**
""")
