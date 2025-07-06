
import os
import yagmail
from dotenv import load_dotenv


load_dotenv()
yg = yagmail.SMTP(os.getenv('EMAIL'), os.getenv('PASSWORD'))

content = "Igho no really get sense"
recipients = ["abdulmalikojo2@gmail.com", "ighoe571@gmail.com"]
subject = "testing the code again"

for recipient in recipients:
    yg.send(to=recipient, subject=subject, contents=content)

print("email sent successfully")

