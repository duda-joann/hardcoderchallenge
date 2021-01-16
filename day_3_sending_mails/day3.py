import os
import csv
import smtplib
import ssl
from typing import Dict
from pathlib import Path
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from jinja2 import Environment, PackageLoader


class SendingMails:

    def __init__(self, sender, password, path):
        self.sender = sender
        self.password = password
        self.path = path

    def read_contacts(self) -> Dict:
        """
        :param path: path for csv file containing contacts
        :return: dictionary with mail and names
        """
        mail_lists = {}
        with open(self.path, 'r') as file:
            contacts = csv.DictReader(file, delimiter=',', fieldnames=['email', 'names'])
            for row in contacts:
                mail = row['email']
                name = (row['names'].replace(' ', '_'))
                mail_lists[mail] = name

        return mail_lists

    def change_photo_name(self, name:str)-> str:
        """ change name of photo for according to receiver name"""
        base_dir = Path(__file__).parent
        for file in os.listdir(base_dir):
            if file.endswith('.png'):
                os.rename(file, f'{name}.png')
                return os.path.join(base_dir, file)

    def create_html(self, name: str):
        """
        create personalize document for user
        """
        path = os.getcwd()
        env = Environment(loader=PackageLoader(package_name='day_3_sending_mails'))
        template = env.get_template('mail.html')
        return template.render(name=name, image=path)

    def render_message(self, receiver: str, name: str):
        """
        creating message to send
        :param receiver:  person who received
        :param filename: photo to send
        :param html: html to send
        :return:
        """
        message = MIMEMultipart()
        message['From'] = self.sender
        message['To'] = receiver
        message['Subject'] ='Your image'

        filename = self.change_photo_name(name)
        with open(filename, "rb") as attachment:
            part = MIMEImage("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        message.attach(part)
        html = self.create_html(name)
        message.attach(html)

        return message

    def send_mail(self) -> None:
        """sending mails"""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender, self.password)
            contacts = self.read_contacts()
            for receiver, name in contacts.items():
                message = self.render_message(receiver, name)
                server.sendmail(self.sender, receiver, message)


def main():
    mail = input('Please provide mail:')
    password = input('Please provide password')
    path = os.path.join(os.getcwd(), 'contacts.csv')
    SendingMails(mail, password, path).send_mail()


if __name__ == '__main__':
    main()
