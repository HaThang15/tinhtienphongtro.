<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phòng trọ TÂM AN - AI Chatbot</title>
st. image("PHONGTRO.jpg",use_container_width=True)
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #dbeafe, #f0fdf4);
            min-height: 100vh;
            padding: 30px;
        }

        .header {
            text-align: center;
            margin-bottom: 25px;
        }

        .header h1 {
            color: #1d4ed8;
            font-size: 32px;
        }

        .header p {
            color: #555;
            margin-top: 8px;
        }

        .main {
            max-width: 1100px;
            margin: auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
        }

        .card {
            background: white;
            border-radius: 18px;
            padding: 25px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.12);
        }

        .card h2 {
            margin-bottom: 20px;
            color: #2563eb;
        }

        .input-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 6px;
            color: #333;
        }

        input {
            width: 100%;
            padding: 11px;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 16px;
        }

        input:focus {
            outline: none;
            border-color: #2563eb;
        }

        button {
            border: none;
            border-radius: 8px;
            padding: 12px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
        }

        .calculate-btn {
            width: 100%;
            background: #2563eb;
            color: white;
        }

        .calculate-btn:hover {
            background: #1d4ed8;
        }

        .result {
            margin-top: 20px;
            background: #eff6ff;
            padding: 15px;
            border-radius: 10px;
        }

        .result p {
            display: flex;
            justify-content: space-between;
            margin: 9px 0;
        }

        .total {
            border-top: 2px solid #2563eb;
            padding-top: 12px;
            color: #dc2626;
            font-size: 20px;
            font-weight: bold;
        }

        /* CHATBOT */

        .chat-box {
            height: 430px;
            display: flex;
            flex-direction: column;
        }

        .messages {
            flex: 1;
            overflow-y: auto;
            background: #f8fafc;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 12px;
        }

        .message {
            max-width: 85%;
            padding: 10px 13px;
            border-radius: 12px;
            margin-bottom: 10px;
            line-height: 1.5;
        }

        .bot {
            background: #e0f2fe;
            color: #075985;
        }

        .user {
            background: #2563eb;
            color: white;
            margin-left: auto;
        }

        .chat-input {
            display: flex;
            gap: 8px;
        }

        .chat-input input {
            flex: 1;
        }

        .send-btn {
            background: #16a34a;
            color: white;
            padding: 0 18px;
        }

        .send-btn:hover {
            background: #15803d;
        }

        .typing {
            color: #777;
            font-style: italic;
        }

        @media (max-width: 800px) {
            body {
                padding: 15px;
            }

            .main {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>

    <div class="header">
        <h1>🏠 PHÒNG TRỌ TÂM AN</h1>
        <p>Quản lý tiền phòng & trợ lý AI thông minh</p>
    </div>

    <div class="main">

        <!-- =========================
             PHẦN TÍNH TIỀN PHÒNG
        ========================== -->

        <div class="card">

            <h2>💰 Tính tiền phòng</h2>

            <div class="input-group">
                <label>Tiền phòng (VNĐ)</label>
                <input
                    type="number"
                    id="tienPhong"
                    placeholder="Ví dụ: 3000000">
            </div>

            <div class="input-group">
                <label>Số điện sử dụng (kWh)</label>
                <input
                    type="number"
                    id="soDien"
                    placeholder="Ví dụ: 100">
            </div>

            <div class="input-group">
                <label>Đơn giá điện (VNĐ/kWh)</label>
                <input
                    type="number"
                    id="giaDien"
                    placeholder="Ví dụ: 3500">
            </div>

            <div class="input-group">
                <label>Số nước sử dụng (m³)</label>
                <input
                    type="number"
                    id="soNuoc"
                    placeholder="Ví dụ: 10">
            </div>

            <div class="input-group">
                <label>Đơn giá nước (VNĐ/m³)</label>
                <input
                    type="number"
                    id="giaNuoc"
                    placeholder="Ví dụ: 15000">
            </div>

            <div class="input-group">
                <label>Tiền Wi-Fi (VNĐ)</label>
                <input
                    type="number"
                    id="tienWifi"
                    placeholder="Ví dụ: 100000">
            </div>

            <button
                class="calculate-btn"
                onclick="tinhTien()">
                🧮 TÍNH TIỀN
            </button>

            <div class="result">

                <p>
                    <span>Tiền phòng:</span>
                    <span id="kqPhong">0 VNĐ</span>
                </p>

                <p>
                    <span>Tiền điện:</span>
                    <span id="kqDien">0 VNĐ</span>
                </p>

                <p>
                    <span>Tiền nước:</span>
                    <span id="kqNuoc">0 VNĐ</span>
                </p>

                <p>
                    <span>Tiền Wi-Fi:</span>
                    <span id="kqWifi">0 VNĐ</span>
                </p>

                <p class="total">
                    <span>TỔNG:</span>
                    <span id="tongTien">0 VNĐ</span>
                </p>

            </div>

        </div>


        <!-- =========================
             PHẦN AI CHATBOT
        ========================== -->

        <div class="card chat-box">

            <h2>🤖 Trợ lý AI TÂM AN</h2>

            <div class="messages" id="messages">

                <div class="message bot">
                    👋 Xin chào! Tôi là trợ lý AI của phòng trọ
                    <b>TÂM AN</b>.<br><br>

                    Bạn có thể hỏi tôi về học tập, lập trình,
                    toán học, tiếng Anh, kiến thức, viết nội dung,
                    công nghệ... hoặc những chủ đề khác.
                </div>

            </div>

            <div class="chat-input">

                <input
                    type="text"
                    id="userInput"
                    placeholder="Bạn muốn hỏi gì?"
                    onkeydown="if(event.key === 'Enter') guiTinNhan()">

                <button
                    class="send-btn"
                    onclick="guiTinNhan()">
                    Gửi
                </button>

            </div>

        </div>

    </div>


<script>

/* =====================================
   TÍNH TIỀN PHÒNG
===================================== */

function tinhTien() {

    const tienPhong =
        Number(document.getElementById("tienPhong").value) || 0;

    const soDien =
        Number(document.getElementById("soDien").value) || 0;

    const giaDien =
        Number(document.getElementById("giaDien").value) || 0;

    const soNuoc =
        Number(document.getElementById("soNuoc").value) || 0;

    const giaNuoc =
        Number(document.getElementById("giaNuoc").value) || 0;

    const tienWifi =
        Number(document.getElementById("tienWifi").value) || 0;


    const tienDien = soDien * giaDien;

    const tienNuoc = soNuoc * giaNuoc;

    const tongTien =
        tienPhong +
        tienDien +
        tienNuoc +
        tienWifi;


    document.getElementById("kqPhong").innerText =
        tienPhong.toLocaleString("vi-VN") + " VNĐ";

    document.getElementById("kqDien").innerText =
        tienDien.toLocaleString("vi-VN") + " VNĐ";

    document.getElementById("kqNuoc").innerText =
        tienNuoc.toLocaleString("vi-VN") + " VNĐ";

    document.getElementById("kqWifi").innerText =
        tienWifi.toLocaleString("vi-VN") + " VNĐ";

    document.getElementById("tongTien").innerText =
        tongTien.toLocaleString("vi-VN") + " VNĐ";
}


/* =====================================
   CHATBOT
===================================== */

function themTinNhan(noiDung, loai) {

    const messages =
        document.getElementById("messages");

    const message =
        document.createElement("div");

    message.className =
        "message " + loai;

    message.innerText =
        noiDung;

    messages.appendChild(message);

    messages.scrollTop =
        messages.scrollHeight;
}


async function guiTinNhan() {

    const input =
        document.getElementById("userInput");

    const cauHoi =
        input.value.trim();

    if (!cauHoi) return;


    // Hiển thị câu hỏi của người dùng
    themTinNhan(cauHoi, "user");

    input.value = "";


    // Hiển thị trạng thái đang trả lời
    const messages =
        document.getElementById("messages");

    const typing =
        document.createElement("div");

    typing.className =
        "message bot typing";

    typing.id =
        "typing";

    typing.innerText =
        "🤖 AI đang suy nghĩ...";

    messages.appendChild(typing);

    messages.scrollTop =
        messages.scrollHeight;


    try {

        /*
         * QUAN TRỌNG:
         *
         * Đây là nơi gửi câu hỏi tới BACKEND AI.
         *
         * Không đặt API KEY trực tiếp ở đây.
         *
         * Backend của bạn sẽ nhận:
         *
         * {
         *     message: cauHoi
         * }
         *
         * rồi gọi API AI và trả về:
         *
         * {
         *     reply: "Câu trả lời..."
         * }
         */

        const response = await fetch("/api/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: cauHoi
            })

        });


        if (!response.ok) {
            throw new Error("Lỗi kết nối AI");
        }


        const data =
            await response.json();


        document
            .getElementById("typing")
            .remove();


        themTinNhan(
            data.reply,
            "bot"
        );


    } catch (error) {

        document
            .getElementById("typing")
            .remove();


        themTinNhan(
            "⚠️ Chưa kết nối được với máy chủ AI. Bạn cần cấu hình backend/API AI cho ứng dụng.",
            "bot"
        );
    }
}

</script>

</body>
</html>
