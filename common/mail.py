import os, copy
import smtplib               # SMTP 라이브러리
from string import Template  # 문자열 템플릿 모듈
from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText
from email.mime.image     import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import sys
import json
from common import utils


class Host_info:
    def __init__(self):
        self.util = utils.Utills()
        try:
            with open(utils.resource_path('./conf/conf.json')) as json_file:
                json_info = json.load(json_file)["mail_info"]
            # 메일서버 계정정보
            print(json_info)
            self.mail_id = json_info['mail_id']
            self.passwd = json_info['passwd']
            # SMTP 정보
            self.str_host = json_info['str_host']
            self.num_port = json_info['num_port']  # SMTP Port
        except Exception as e:
            self.util.print_error_log(str(e))

class EmailHTMLContent:
    """e메일에 담길 컨텐츠"""
    def __init__(self, str_subject, template, template_params, attachments):
        """string template과 딕셔너리형 template_params받아 MIME 메시지를 만든다"""
        assert isinstance(template, Template)
        assert isinstance(template_params, dict)
        self.msg = MIMEMultipart()

        # e메일 제목을 설정한다
        self.msg['Subject'] = str_subject  # e메일 제목을 설정한다

        # e메일 본문을 설정한다
        str_msg = template.safe_substitute(**template_params)  # ${변수} 치환하며 문자열 만든다
        mime_msg = MIMEText(str_msg, 'html')  # MIME HTML 문자열을 만든다
        self.msg.attach(mime_msg)

        # 메일 콘텐츠 - 첨부파일
        for attachment in attachments:
            # 첨부파일을 아무것도 안넣었을때
            if len(attachments) == 1 and  attachment == os.path.join(os.getcwd(), 'test.text'):
                break;
            attach_binary = MIMEBase("application", "octect-stream")
            try:
                binary = open(attachment, "rb").read()  # read file to bytes
                attach_binary.set_payload(binary)
                encoders.encode_base64(attach_binary)  # Content-Transfer-Encoding: base64
                filename = os.path.basename(attachment)
                attach_binary.add_header("Content-Disposition", 'attachment', filename=('utf-8', '', filename))
                self.msg.attach(attach_binary)
            except Exception as e:
                print(e)
    def get_message(self, str_from_email_addr, str_to_eamil_addrs):
        """발신자, 수신자리스트를 이용하여 보낼메시지를 만든다 """
        mm = copy.deepcopy(self.msg)
        mm['From'] = str_from_email_addr  # 발신자
        mm['To'] = ",".join(str_to_eamil_addrs)  # 수신자리스트
        return mm


class EmailSender:
    """e메일 발송자"""
    def __init__(self):
        """호스트와 포트번호로 SMTP로 연결한다 """
        host_info = Host_info()
        self.str_host = host_info.str_host
        self.num_port = host_info.num_port
        self.ss = smtplib.SMTP_SSL(host=self.str_host, port=self.num_port)
        # SMTP인증이 필요하면 아래 주석을 해제하세요.
        # self.ss.starttls() # TLS(Transport Layer Security) 시작
        self.ss.login(host_info.mail_id, host_info.passwd) # 메일서버에 연결한 계정과 비밀번호

    def send_message(self, emailContent, str_from_email_addr, str_to_eamil_addrs):
        """e메일을 발송한다 """
        cc = emailContent.get_message(str_from_email_addr, str_to_eamil_addrs)
        self.ss.send_message(cc, from_addr=str_from_email_addr, to_addrs=str_to_eamil_addrs)
        del cc

class MailManager:
    def __init__(self):
        try:
            print('MailManager')
            self.util = utils.Utills()
            # 메일 객체 생성
            self.emailSender = EmailSender()
            self.str_from_email_addr = '' # 메일  발신자
            self.str_to_eamil_addrs = [] # 메일 수신대상
        except Exception as e:
            print(e)
            self.util.print_error_log(str(e))

    def setMailUserInfo(self,_sender_mail_address = 'nieah914@naver.com',_revicer_mail_address= ['jhyoon900522@naver.com', 'nieah914@naver.com']):
        print('setMailUserInfo')
        # 발신자
        self.str_from_email_addr = _sender_mail_address
        # 수신자
        self.str_to_eamil_addrs = _revicer_mail_address

    def setMailContests(self,_subject='제목',_template=Template("""<html>
                                    <head></head>
                                    <body>
                                        Hi ${NAME}.<br>
                                        안녕하세요 정해인입니다.
                                    </body>
                                </html>"""),_template_params={'NAME': 'Son'},_attachments = [os.path.join(os.getcwd(), 'test.text')]):
        print('setMailContests')
        # 메일 제목
        str_subject = _subject

        # 메일 내용
        template = _template

        # 메일 파라미터
        template_params = _template_params

        # 메일 첨부파일
        attachments = _attachments

        self.emailHTMLContent = EmailHTMLContent(str_subject, template, template_params, attachments)

    def sendMail(self):
        print('sendMail')
        try:
            # 메일 인코딩, 메일 전송
            self.emailSender.send_message(self.emailHTMLContent, self.str_from_email_addr, self.str_to_eamil_addrs)

        except Exception as e:
            self.setMailContests('에러가 발생했습니다.', Template("""<html>
                                                <head></head>
                                                <body>
                                                    Hi ${NAME}.<br>
                                                    에러가 발생했습니다.
                                                    해당 메일은 발신자에게만 발송됩니다.
                                                </body>
                                            </html>"""), {'NAME': 'Son'})
            self.emailSender.send_message(self.emailHTMLContent, 'nieah914@naver.com', self.str_from_email_addr)


# 실행 샘플
# MM = MailManager()
# MM.setMailUserInfo('nieah914@naver.com',['jhyoon900522@naver.com', 'nieah914@naver.com'])
# MM.setMailContests('테스트 제목입니다.',Template("""<html>
#                                     <head></head>
#                                     <body>
#                                         Hi ${NAME}.<br>
#                                         안녕하세요 정해인입니다.
#                                     </body>
#                                 </html>"""),{'NAME': 'Son'})
# MM.sendMail()