<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phòng trọ TÂM AN</title>

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
            padding: 25px;
        }

        .header {
            max-width: 1100px;
            margin: auto;
            text-align: center;
            margin-bottom: 25px;
        }

        .header h1 {
            color: #1d4ed8;
            font-size: 36px;
            margin-bottom: 8px;
        }

        .header p {
            color: #555;
            font-size: 16px;
        }

        .room-image {
            max-width: 1100px;
            margin: 0 auto 25px;
            text-align: center;
        }

        .room-image img {
            width: 100%;
            max-width: 750px;
            height: 300px;
            object-fit: cover;
            border-radius: 18px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.18);
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
            padding: 25px;
            border-radius: 18px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
        }

        .card h2 {
            color: #2563eb;
            margin-bottom: 20px;
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
            margin: 10px 0;
        }

        .total {
            border-top: 2px solid #2563eb;
            padding-top: 12px;
            color: #dc2626;
            font-size: 20px;
            font-weight: bold;
        }

        .chat-box {
            height: 570px;
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
            padding: 11px 14px;
            border-radius: 12px;
            margin-bottom: 10px;
            line-height: 1.5;
            white-space: pre-wrap;
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
            padding: 0 20px;
        }

        .send-btn:hover {
            background: #15803d;
        }

        .footer {
            text-align: center;
            margin-top: 25px;
            color: #666;
            font-size: 14px;
        }

        @media (max-width: 800px) {
            body {
                padding: 15px;
            }

            .main {
                grid-template-columns: 1fr;
            }

            .room-image img {
                height: 220px;
            }

            .header h1 {
                font-size: 28px;
            }
        }
    </style>
</head>

<body>

    <div class="room-image">
        <img src="anh-tam-an.jpg" alt="Phòng trọ TÂM AN">
    </div>

    <div class="header">
        <h1>🏠 PHÒNG TRỌ TÂM AN</h1>
        <p>Quản lý tiền phòng và trợ lý AI thông minh</p>
    </div>

    <div class="main">

        <div class="card">
            <h2>💰 Tính tiền phòng</h2>

            <div class="input-group">
                <label>Tiền phòng (VNĐ)</label>
                <input type="number" id="tienPhong" placeholder="3000000">
            </div>

            <div class="input-group">
                <label>Số điện sử dụng (kWh)</label>
                <input type="number" id="soDien" placeholder="100">
            </div>

            <div class="input-group">
                <label>Đơn giá điện (VNĐ/kWh)</label>
                <input type="number" id="giaDien" placeholder="3500">
            </div>

            <div class="input-group">
                <label>Số nước sử dụng (m³)</label>
                <input type="number" id="soNuoc" placeholder="10">
            </div>

            <div class="input-group">
                <label>Đơn giá nước (VNĐ/m³)</label>
                <input type="number" id="giaNuoc" placeholder="15000">
            </div>

            <div class="input-group">
                <label>Tiền Wi-Fi (VNĐ)</label>
                <input type="number" id="tienWifi" placeholder="100000">
            </div>

            <button class="calculate-btn" onclick="tinhTien()">
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

        <div class="card chat-box">
            <h2>🤖 Trợ lý AI TÂM AN</h2>

            <div class="messages" id="messages">
                <div class="message bot">
                    👋 Xin chào! Tôi là trợ lý AI của phòng trọ TÂM AN.

Bạn có thể hỏi tôi về:
• Học tập
• Toán học
• Lập trình
• Tiếng Anh
• Công nghệ
• Kiến thức
• Viết nội dung
• Và nhiều lĩnh vực khác.
                </div>
            </div>

            <div class="chat-input">
                <input
                    type="text"
                    id="userInput"
                    placeholder="Nhập câu hỏi..."
                    onkeydown="if(event.key === 'Enter') guiTinNhan()"
                >

                <button class="send-btn" onclick="guiTinNhan()">
                    Gửi
                </button>
            </div>
        </div>

    </div>

    <div class="footer">
        © 2026 PHÒNG TRỌ TÂM AN
    </div>

    <script>
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

        function themTinNhan(noiDung, loai) {
            const messages = document.getElementById("messages");

            const message = document.createElement("div");

            message.className = "message " + loai;

            message.innerText = noiDung;

            messages.appendChild(message);

            messages.scrollTop = messages.scrollHeight;
        }

        async function guiTinNhan() {
            const input = document.getElementById("userInput");

            const cauHoi = input.value.trim();

            if (!cauHoi) {
                return;
            }

            themTinNhan(cauHoi, "user");

            input.value = "";

            const loading = document.createElement("div");

            loading.className = "message bot";

            loading.id = "loading";

            loading.innerText = "🤖 AI đang suy nghĩ...";

            document.getElementById("messages").appendChild(loading);

            try {
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
                    throw new Error("API Error");
                }

                const data = await response.json();

                document.getElementById("loading").remove();

                themTinNhan(data.reply, "bot");

            } catch (error) {
                document.getElementById("loading").remove();

                themTinNhan(
                    "⚠️ Chưa kết nối được với AI. Hãy kiểm tra máy chủ hoặc API AI.",
                    "bot"
                );
            }
        }
    </script>

</body>
</html>
