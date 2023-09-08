import smtplib
from email.mime.text import MIMEText

EMAIL = "nubcoder420@gmail.com"
PASSWORD = "jubfnlbhyvtirtym"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self, email_message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)

            msg = MIMEText(email_message, 'plain', 'utf-8')
            msg['From'] = EMAIL
            msg['To'] = EMAIL
            msg['Subject'] = f"FLIGHT DEALS!"

            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=msg.as_string(),
            )