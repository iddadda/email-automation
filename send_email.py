import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv


# 메일 전송 함수
def send_email (subject, message):
    load_dotenv()  # .env 파일 로드
    sender_email = os.getenv('SECRET_ID')  # sender email
    password = os.getenv('SECRET_PWD')  # sender email password
    
    recipient_email = "iddadda241@gmail.com"

    # 이메일 메시지 설정
    msg = MIMEMultipart()
    
    msg['From'] = sender_email   # 송신자 이메일
    msg['To'] = recipient_email  # 수신자 이메일
    msg['Subject'] = subject     # 이메일 제목
    
    msg.attach(MIMEText(message, 'plain'))
    
    try:
        # 서버 접속
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # 로그인
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("이메일 전송 성공!")
    
    except Exception as e:
        print(f"이메일 전송 실패: {e}")

send_email("Test 메일 제목", "This is a test 메일 내용")