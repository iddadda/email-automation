import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os


# 메일 전송 함수
def send_email ():
    load_dotenv()
    sender_email = os.getenv('SECRET_ID') 
    password = os.getenv('SECRET_PWD')
    recipient_email = "iddadda241@gmail.com"
    subject = "HTML 이메일 테스트"

    msg = MIMEMultipart()
    # 헤더
    msg['From'] = sender_email   
    msg['To'] = recipient_email  
    msg['Subject'] = subject  
    # 본문  
    html_content = f"""\
        
        Hello,<br>
        This is a test email with HTML content!<br>
        <b>Bold Text</b><br>
        <i>Italic Text</i><br>
        <a href="https://www.example.com">Example Link</a><br>
        Regards,<br>
        dadda
        """ 
    
    msg.attach(MIMEText(html_content, 'html'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        print("이메일 전송 성공!")
    
    except Exception as e:
        print(f"이메일 전송 실패: {e}")

    finally:
        server.quit()
        
send_email()