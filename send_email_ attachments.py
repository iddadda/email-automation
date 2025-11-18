from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage # 이미지 파일의 base64 인코딩을 위한 모듈
from email import encoders


# 메일 전송 함수
def send_email ():
    load_dotenv()
    
    # 발신자 정보
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = os.getenv('SECRET_ID') 
    password = os.getenv('SECRET_PWD')
    
    # 수신자 이메일
    recipient_email = "iddadda241@gmail.com"
    
    # 이메일 제목과 본문
    subject = "이미지, 첨부파일 이메일 테스트"
    body = f"""\
        <img src="https://images.unsplash.com/photo-1761839262867-af53d08b0eb5?w=1600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDF8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwxfHx8ZW58MHx8fHx8" alt="Embedded Image" width="600"><br>
        Hello,<br>
        This is a test email with image and attachment!<br>
        <b>Bold Text</b><br>
        <i>Italic Text</i><br>
        <a href="https://www.example.com">Example Link</a><br>
        <img src="cid:image.jpeg" alt="이미지" width="400"><br>
        Regards,<br>
        dadda
        """ 
        

    
    # 이메일 메시지 구성
    msg = MIMEMultipart()
    msg['From'] = sender_email   
    msg['To'] = recipient_email  
    msg['Subject'] = subject  
    msg.attach(MIMEText(body, 'html'))
    
    
    # 이미지 경로
    img_path = "/Users/ida/til/til_python/img/003.jpeg"
    
    with open(img_path, 'rb') as img_file:
        img_data = img_file.read()    
        
    # 본문에 이미지 첨부
    image = MIMEImage(img_data, _subtype = 'jpeg', name=os.path.basename(img_path))
    image.add_header('Content-ID', '<image.jpeg>')
    msg.attach(image)
    
    
    # 첨부파일 경로 리스트
    attachments = list()
    attachments.append("/Users/ida/til/til_python/img/001.jpeg")
    attachments.append("/Users/ida/Documents/archive/sparta/frontend/main.py")
    
    for attachment in attachments: 
        with open(attachment, 'rb') as file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="%s"' % os.path.basename(file.name))
            msg.attach(part)
    
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        print("이메일 전송 성공!")
    
    except Exception as e:
        print(f"이메일 전송 실패: {e}")

    finally:
        server.quit()
        
send_email()