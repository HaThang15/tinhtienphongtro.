# =========================================================
# 🤖 CHATBOT PHÒNG TRỌ TÂM AN - KHÔNG CẦN AI
# =========================================================

def chatbot_phong_tro(question):

    q = question.lower().strip()

    # -----------------------------------------
    # CHÀO HỎI
    # -----------------------------------------

    if any(x in q for x in [
        "xin chào",
        "chào",
        "hello",
        "hi"
    ]):

        return """
🤖 Xin chào! Tôi là Chatbot TÂM AN.

Tôi có thể giúp bạn:
• Tra cứu phòng
• Tra cứu người thuê
• Kiểm tra tiền phòng
• Kiểm tra tiền điện
• Kiểm tra tiền nước
• Kiểm tra thanh toán
• Xem tổng doanh thu
• Thống kê phòng

Bạn hãy đặt câu hỏi nhé!
"""

    # -----------------------------------------
    # SỐ LƯỢNG PHÒNG
    # -----------------------------------------

    if (
        "bao nhiêu phòng" in q
        or "số phòng" in q
        or "có mấy phòng" in q
    ):

        return f"""
🏠 TÂM AN hiện có {len(PHONG_LIST)} phòng:

{", ".join(PHONG_LIST)}
"""

    # -----------------------------------------
    # TÌM MÃ PHÒNG
    # -----------------------------------------

    phong_tim_thay = None

    for phong in PHONG_LIST:

        if phong.lower() in q:

            phong_tim_thay = phong
            break

    # -----------------------------------------
    # THÔNG TIN MỘT PHÒNG
    # -----------------------------------------

    if phong_tim_thay:

        phong = phong_tim_thay

        ten = st.session_state.nguoi_thue.get(
            phong,
            "Chưa có người thuê"
        )

        # Nếu phòng chưa có hóa đơn
        if phong not in st.session_state.hoa_don_phong:

            return f"""
🏠 THÔNG TIN PHÒNG {phong}

👤 Người thuê:
{ten}

🧾 Hóa đơn:
Chưa có hóa đơn được tạo.

💡 Bạn có thể vào "🏠 Tính tiền phòng"
để tạo hóa đơn.
"""

        hd = st.session_state.hoa_don_phong[phong]

        # -------------------------------------
        # HỎI NGƯỜI THUÊ
        # -------------------------------------

        if (
            "ai thuê" in q
            or "người thuê" in q
            or "tên" in q
        ):

            return f"""
🏠 Phòng {phong}

👤 Người thuê:
**{ten}**
"""

        # -------------------------------------
        # HỎI TRẠNG THÁI THANH TOÁN
        # -------------------------------------

        if (
            "thanh toán" in q
            or "đóng tiền" in q
            or "đã đóng" in q
            or "chưa đóng" in q
        ):

            return f"""
🏠 Phòng {phong}

👤 Người thuê:
{ten}

💳 Trạng thái:
{hd["trang_thai"]}

💰 Tổng tiền:
{format_money(hd["tong"])}
"""

        # -------------------------------------
        # HỎI TIỀN ĐIỆN
        # -------------------------------------

        if "điện" in q:

            return f"""
⚡ TIỀN ĐIỆN PHÒNG {phong}

Chỉ số cũ:
{hd["dien_cu"]} kWh

Chỉ số mới:
{hd["dien_moi"]} kWh

Số điện sử dụng:
{hd["so_dien"]} kWh

Giá điện:
{format_money(hd["gia_dien"])}/kWh

💰 Tiền điện:
**{format_money(hd["tien_dien"])}**
"""

        # -------------------------------------
        # HỎI TIỀN NƯỚC
        # -------------------------------------

        if "nước" in q:

            return f"""
💧 TIỀN NƯỚC PHÒNG {phong}

Chỉ số cũ:
{hd["nuoc_cu"]} m³

Chỉ số mới:
{hd["nuoc_moi"]} m³

Số nước sử dụng:
{hd["so_nuoc"]} m³

Giá nước:
{format_money(hd["gia_nuoc"])}/m³

💰 Tiền nước:
**{format_money(hd["tien_nuoc"])}**
"""

        # -------------------------------------
        # HỎI TIỀN PHÒNG
        # -------------------------------------

        if (
            "tiền phòng" in q
            or "giá phòng" in q
            or "phòng bao nhiêu" in q
        ):

            return f"""
🏠 PHÒNG {phong}

👤 Người thuê:
{ten}

💵 Tiền phòng:
**{format_money(hd["tien_phong"])}**
"""

        # -------------------------------------
        # HỎI WIFI
        # -------------------------------------

        if (
            "wifi" in q
            or "internet" in q
        ):

            return f"""
📶 WIFI PHÒNG {phong}

💰 Tiền WiFi:
**{format_money(hd["wifi"])}**
"""

        # -------------------------------------
        # HỎI TỔNG TIỀN
        # -------------------------------------

        if (
            "tổng tiền" in q
            or "hết bao nhiêu" in q
            or "bao nhiêu tiền" in q
            or "hóa đơn" in q
        ):

            return f"""
🧾 HÓA ĐƠN PHÒNG {phong}

👤 Người thuê:
{ten}

💵 Tiền phòng:
{format_money(hd["tien_phong"])}

⚡ Tiền điện:
{format_money(hd["tien_dien"])}

💧 Tiền nước:
{format_money(hd["tien_nuoc"])}

📶 WiFi:
{format_money(hd["wifi"])}

🗑️ Phí rác:
{format_money(hd["phi_khac"])}

━━━━━━━━━━━━━━━━

💰 TỔNG:
**{format_money(hd["tong"])}**

💳 Trạng thái:
{hd["trang_thai"]}
"""

        # -------------------------------------
        # CÂU HỎI CHUNG VỀ PHÒNG
        # -------------------------------------

        return f"""
🏠 THÔNG TIN PHÒNG {phong}

👤 Người thuê:
{ten}

💵 Tiền phòng:
{format_money(hd["tien_phong"])}

⚡ Tiền điện:
{format_money(hd["tien_dien"])}

💧 Tiền nước:
{format_money(hd["tien_nuoc"])}

📶 WiFi:
{format_money(hd["wifi"])}

🗑️ Phí rác:
{format_money(hd["phi_khac"])}

💰 Tổng tiền:
**{format_money(hd["tong"])}**

💳 Trạng thái:
{hd["trang_thai"]}
"""

    # =====================================================
    # TỔNG DOANH THU
    # =====================================================

    if (
        "doanh thu" in q
        or "tổng doanh thu" in q
        or "thu được bao nhiêu" in q
    ):

        tong = 0

        for hd in st.session_state.hoa_don_phong.values():

            tong += hd["tong"]

        return f"""
💰 TỔNG DOANH THU

Hiện tại TÂM AN có:

🏠 Số phòng đã tính tiền:
{len(st.session_state.hoa_don_phong)} phòng

💵 Tổng doanh thu:
**{format_money(tong)}**
"""

    # =====================================================
    # PHÒNG CHƯA THANH TOÁN
    # =====================================================

    if (
        "chưa thanh toán" in q
        or "chưa đóng tiền" in q
        or "chưa đóng" in q
    ):

        danh_sach = []

        for phong, hd in st.session_state.hoa_don_phong.items():

            if hd["trang_thai"] == "❌ Chưa thanh toán":

                danh_sach.append(
                    f"🏠 {phong} - "
                    f"{hd['nguoi_thue']} - "
                    f"{format_money(hd['tong'])}"
                )

        if not danh_sach:

            return """
✅ Hiện tại không có phòng nào
chưa thanh toán.
"""

        return """
❌ CÁC PHÒNG CHƯA THANH TOÁN:

""" + "\n".join(danh_sach)

    # =====================================================
    # PHÒNG ĐÃ THANH TOÁN
    # =====================================================

    if (
        "đã thanh toán" in q
        or "đã đóng tiền" in q
        or "đã đóng" in q
    ):

        danh_sach = []

        for phong, hd in st.session_state.hoa_don_phong.items():

            if hd["trang_thai"] == "✅ Đã thanh toán":

                danh_sach.append(
                    f"🏠 {phong} - "
                    f"{hd['nguoi_thue']} - "
                    f"{format_money(hd['tong'])}"
                )

        if not danh_sach:

            return """
ℹ️ Chưa có phòng nào được
đánh dấu đã thanh toán.
"""

        return """
✅ CÁC PHÒNG ĐÃ THANH TOÁN:

""" + "\n".join(danh_sach)

    # =====================================================
    # TỔNG TIỀN ĐIỆN
    # =====================================================

    if (
        "tổng tiền điện" in q
        or "tổng điện" in q
    ):

        tong = sum(
            hd["tien_dien"]
            for hd in st.session_state.hoa_don_phong.values()
        )

        return f"""
⚡ TỔNG TIỀN ĐIỆN

💰 Tổng tiền điện:
**{format_money(tong)}**
"""

    # =====================================================
    # TỔNG TIỀN NƯỚC
    # =====================================================

    if (
        "tổng tiền nước" in q
        or "tổng nước" in q
    ):

        tong = sum(
            hd["tien_nuoc"]
            for hd in st.session_state.hoa_don_phong.values()
        )

        return f"""
💧 TỔNG TIỀN NƯỚC

💰 Tổng tiền nước:
**{format_money(tong)}**
"""

    # =====================================================
    # CÁCH TÍNH TIỀN
    # =====================================================

    if (
        "cách tính" in q
        or "tính tiền như thế nào" in q
        or "tính tiền ra sao" in q
    ):

        return """
🧮 CÁCH TÍNH TIỀN PHÒNG TÂM AN

⚡ Tiền điện:

Số điện sử dụng =
Chỉ số mới - Chỉ số cũ

Tiền điện =
Số điện sử dụng × Giá điện

💧 Tiền nước:

Số nước sử dụng =
Chỉ số mới - Chỉ số cũ

Tiền nước =
Số nước sử dụng × Giá nước

💰 Tổng tiền:

Tiền phòng
+ Tiền điện
+ Tiền nước
+ WiFi
+ Phí rác
= Tổng tiền phải thanh toán.
"""

    # =====================================================
    # GIÁ ĐIỆN
    # =====================================================

    if (
        "giá điện" in q
        or "điện bao nhiêu" in q
    ):

        if st.session_state.hoa_don_phong:

            hd = list(
                st.session_state.hoa_don_phong.values()
            )[0]

            return f"""
⚡ GIÁ ĐIỆN

Giá điện hiện đang được tính:

**{format_money(hd["gia_dien"])}/kWh**
"""

        return """
⚡ Chưa có hóa đơn để xác định
giá điện hiện tại.
"""

    # =====================================================
    # GIÁ NƯỚC
    # =====================================================

    if (
        "giá nước" in q
        or "nước bao nhiêu" in q
    ):

        if st.session_state.hoa_don_phong:

            hd = list(
                st.session_state.hoa_don_phong.values()
            )[0]

            return f"""
💧 GIÁ NƯỚC

Giá nước hiện đang được tính:

**{format_money(hd["gia_nuoc"])}/m³**
"""

        return """
💧 Chưa có hóa đơn để xác định
giá nước hiện tại.
"""

    # =====================================================
    # THỐNG KÊ
    # =====================================================

    if (
        "thống kê" in q
        or "tình hình phòng" in q
        or "tình trạng phòng" in q
    ):

        tong_phong = len(
            st.session_state.hoa_don_phong
        )

        da_thanh_toan = 0
        chua_thanh_toan = 0

        for hd in st.session_state.hoa_don_phong.values():

            if hd["trang_thai"] == "✅ Đã thanh toán":

                da_thanh_toan += 1

            else:

                chua_thanh_toan += 1

        return f"""
📊 THỐNG KÊ PHÒNG TÂM AN

🏠 Đã tính tiền:
{tong_phong} phòng

✅ Đã thanh toán:
{da_thanh_toan} phòng

❌ Chưa thanh toán:
{chua_thanh_toan} phòng

🏠 Tổng số phòng:
{len(PHONG_LIST)} phòng
"""

    # =====================================================
    # NGOÀI PHẠM VI
    # =====================================================

    return """
🤖 Xin lỗi!

Tôi là Chatbot của **PHÒNG TRỌ TÂM AN**.

Tôi chỉ hỗ trợ các câu hỏi liên quan đến:

🏠 Phòng trọ
👤 Người thuê
💵 Tiền phòng
⚡ Tiền điện
💧 Tiền nước
📶 WiFi
🧾 Hóa đơn
💳 Thanh toán
📊 Doanh thu
📋 Thống kê phòng

Bạn hãy hỏi lại về phòng trọ nhé!
"""
