import os
import smtplib
import imghdr
from email.message import EmailMessage

password = os.getenv("Password")
sender = "prafulgulani555@gmail.com"
receiver = "prafulgulani555@gmail.com"

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New weirdo showed up"
    email_message.set_content("Hey, another sus person")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, receiver, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email(image_path="images/19.png")
