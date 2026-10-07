import streamlit as st
from datetime import datetime

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
    margin-top: 10px;
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
    margin-top: 20px;
}

.total-money {
    font-size: 36px;
    font-weight: bold;
    margin-top: 10px;
}

.room-card {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #ddd;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)




st.image(
    "anh_tam_an.jpg",
    use_container_width=True
)





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
# NGƯỜI THUÊ
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
# HÀM ĐỊNH DẠNG TIỀN
# =========================================================

def format_money(number):

    return f"{number:,.0f} VNĐ".replace(",", ".")


# =========================================================
# MENU
# =========================================================

menu = st.sidebar.radio(
    "📌 MENU",
    [
        "🏠 Tính tiền phòng",
        "📋 Quản lý toàn bộ phòng",
        "ℹ️ Thông tin TÂM AN"
    ]
)


# =========================================================
# TRANG 1: TÍNH TIỀN PHÒNG
# =========================================================

if menu == "🏠 Tính tiền phòng":

    st.header("🧾 TÍNH TIỀN PHÒNG")

    # -----------------------------------------------------
    # CHỌN PHÒNG
    # -----------------------------------------------------

    st.markdown(
        '<div class="box">',
        unsafe_allow_html=True
    )

    st.subheader("🏠 Thông tin phòng")

    phong = st.selectbox(
        "Chọn phòng",
        PHONG_LIST
    )

    ten_khach = st.session_state.nguoi_thue.get(
        phong,
        "Chưa cập nhật"
    )

    st.info(
        f"👤 Người thuê: **{ten_khach}**"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # NHẬP THÔNG TIN
    # -----------------------------------------------------

    col1, col2 = st.columns(2)


    # =====================================================
    # CỘT TRÁI
    # =====================================================

    with col1:

        st.markdown(
            '<div class="box">',
            unsafe_allow_html=True
        )

        st.subheader("🏠 Các khoản phí")

        tien_phong = st.number_input(
            "💰 Tiền phòng / tháng",
            min_value=0,
            value=3000000,
            step=100000,
            key=f"tien_phong_{phong}"
        )

        tien_wifi = st.number_input(
            "📶 Tiền WiFi / tháng",
            min_value=0,
            value=100000,
            step=10000,
            key=f"wifi_{phong}"
        )

        tien_rac = st.number_input(
            "🗑️ Phí rác / dịch vụ",
            min_value=0,
            value=50000,
            step=10000,
            key=f"rac_{phong}"
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


    # =====================================================
    # CỘT PHẢI
    # =====================================================

    with col2:

        st.markdown(
            '<div class="box">',
            unsafe_allow_html=True
        )

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
            "💡 Đơn giá điện / kWh",
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
            "🚰 Đơn giá nước / m³",
            min_value=0,
            value=20000,
            step=1000,
            key=f"gia_nuoc_{phong}"
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


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
        "🧮 TÍNH TIỀN",
        use_container_width=True
    ):

        # -------------------------------------------------
        # TÍNH ĐIỆN
        # -------------------------------------------------

        so_dien = dien_moi - dien_cu


        # -------------------------------------------------
        # TÍNH NƯỚC
        # -------------------------------------------------

        so_nuoc = nuoc_moi - nuoc_cu


        # -------------------------------------------------
        # KIỂM TRA
        # -------------------------------------------------

        if so_dien < 0:

            st.error(
                "⚠️ Chỉ số điện tháng này không được nhỏ hơn tháng trước."
            )

            st.stop()


        if so_nuoc < 0:

            st.error(
                "⚠️ Chỉ số nước tháng này không được nhỏ hơn tháng trước."
            )

            st.stop()


        # -------------------------------------------------
        # TÍNH TIỀN
        # -------------------------------------------------

        tien_dien = so_dien * gia_dien

        tien_nuoc = so_nuoc * gia_nuoc

        tong_tien = (
            tien_phong
            + tien_dien
            + tien_nuoc
            + tien_wifi
            + tien_rac
        )


        # -------------------------------------------------
        # LƯU DỮ LIỆU
        # -------------------------------------------------

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
            f"✅ Đã tính tiền phòng {phong}"
        )


        # =================================================
        # HIỂN THỊ TỔNG
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


        # =================================================
        # CHI TIẾT
        # =================================================

        st.subheader("📋 Chi tiết hóa đơn")

        st.table({

            "Khoản phí": [
                "🏠 Tiền phòng",
                "⚡ Tiền điện",
                "💧 Tiền nước",
                "📶 WiFi",
                "🗑️ Phí dịch vụ"
            ],

            "Số lượng": [
                "1 tháng",
                f"{so_dien:.0f} kWh",
                f"{so_nuoc:.0f} m³",
                "1 tháng",
                "1 tháng"
            ],

            "Thành tiền": [

                format_money(tien_phong),

                format_money(tien_dien),

                format_money(tien_nuoc),

                format_money(tien_wifi),

                format_money(tien_rac)
            ]
        })


        # =================================================
        # TRẠNG THÁI
        # =================================================

        if trang_thai == "✅ Đã thanh toán":

            st.success(
                "💚 Phòng đã thanh toán."
            )

        else:

            st.warning(
                "🔴 Phòng chưa thanh toán."
            )


# =========================================================
# TRANG 2: QUẢN LÝ TOÀN BỘ PHÒNG
# =========================================================

elif menu == "📋 Quản lý toàn bộ phòng":

    st.header("📋 QUẢN LÝ TOÀN BỘ DÃY PHÒNG")

    if len(st.session_state.hoa_don_phong) == 0:

        st.info(
            "ℹ️ Chưa có dữ liệu. "
            "Hãy tính tiền cho các phòng trước."
        )

    else:

        data = []

        tong_phong = 0

        tong_dien = 0

        tong_nuoc = 0

        tong_phi = 0

        tong_all = 0

        so_da_thanh_toan = 0

        so_chua_thanh_toan = 0


        # -------------------------------------------------
        # DUYỆT TỪNG PHÒNG
        # -------------------------------------------------

        for phong, hd in st.session_state.hoa_don_phong.items():

            phi_khac = (
                hd["wifi"]
                + hd["phi_khac"]
            )

            data.append({

                "STT":
                    len(data) + 1,

                "Phòng":
                    phong,

                "Người thuê":
                    hd["nguoi_thue"],

                "Tiền phòng":
                    format_money(
                        hd["tien_phong"]
                    ),

                "Tiền điện":
                    format_money(
                        hd["tien_dien"]
                    ),

                "Tiền nước":
                    format_money(
                        hd["tien_nuoc"]
                    ),

                "Phí khác":
                    format_money(
                        phi_khac
                    ),

                "Tổng tiền":
                    format_money(
                        hd["tong"]
                    ),

                "Trạng thái":
                    hd["trang_thai"]
            })


            # ------------------------------------------------
            # CỘNG TỔNG
            # ------------------------------------------------

            tong_phong += hd["tien_phong"]

            tong_dien += hd["tien_dien"]

            tong_nuoc += hd["tien_nuoc"]

            tong_phi += phi_khac

            tong_all += hd["tong"]


            if hd["trang_thai"] == "✅ Đã thanh toán":

                so_da_thanh_toan += 1

            else:

                so_chua_thanh_toan += 1


        # -------------------------------------------------
        # BẢNG
        # -------------------------------------------------

        st.dataframe(
            data,
            use_container_width=True,
            hide_index=True
        )


        # =================================================
        # THỐNG KÊ
        # =================================================

        st.subheader("📊 TỔNG HỢP")


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


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "📶🗑️ Phí khác",
                format_money(tong_phi)
            )


        with col2:

            st.metric(
                "💰 TỔNG DOANH THU",
                format_money(tong_all)
            )


        with col3:

            st.metric(
                "🔴 Chưa thanh toán",
                f"{so_chua_thanh_toan} phòng"
            )


        st.divider()


        # =================================================
        # TRẠNG THÁI
        # =================================================

        col1, col2 = st.columns(2)


        with col1:

            st.success(
                f"✅ Đã thanh toán: "
                f"{so_da_thanh_toan} phòng"
            )


        with col2:

            st.error(
                f"❌ Chưa thanh toán: "
                f"{so_chua_thanh_toan} phòng"
            )


# =========================================================
# TRANG 3: THÔNG TIN
# =========================================================

elif menu == "ℹ️ Thông tin TÂM AN":

    st.header("🏠 PHÒNG TRỌ TÂM AN")

    st.markdown("""
### 🏡 GIỚI THIỆU

**TÂM AN** là hệ thống hỗ trợ quản lý phòng trọ,
giúp chủ trọ theo dõi tiền phòng và các khoản chi phí
hàng tháng một cách nhanh chóng, rõ ràng.

### ⚡ Các khoản quản lý

- 🏠 Tiền phòng
- ⚡ Tiền điện
- 💧 Tiền nước
- 📶 Tiền WiFi
- 🗑️ Phí rác / dịch vụ
- 💳 Trạng thái thanh toán

### 📊 Quản lý

Hệ thống cho phép:

- Chọn phòng nhanh chóng.
- Theo dõi người thuê.
- Tính tiền điện theo kWh.
- Tính tiền nước theo m³.
- Tổng hợp tiền phải thu.
- Kiểm tra phòng đã thanh toán.
- Kiểm tra phòng chưa thanh toán.
- Theo dõi tổng doanh thu.

---

### ❤️ TÂM AN

**An tâm khi ở – Minh bạch khi thanh toán.**
""")
