import os
import time
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

log_file = "sent_log.txt"

sheet_url = "https://docs.google.com/spreadsheets/d/1k25FS3048Ovae_WrycxCScvuSfwkrekN/export?format=csv"

df = pd.read_csv(sheet_url)

start_index = (datetime.now().day * 5) % len(df)
rows_to_send = df.iloc[start_index:start_index+5]

resume_path = "/Users/ayushkumar/Desktop/personal documets/ayush kumar data science.pdf"

for _, row in rows_to_send.iterrows():

    name = row['Name']
    email = row['Email']
    company = row['Company']

    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            if email in f.read():
                print(f"Already sent to {email}")
                continue

    body = f"""
Hi {name},

I hope you’re doing well. I’ve been meaning to reach out because I’ve been following {company} for a while now, and the way you’re building your work genuinely stands out to me. It feels intentional, thoughtful, and founder-led — which is exactly the kind of environment I want to learn in.

I want to be upfront and honest: I don’t come with traditional work experience yet.
What I do bring is strong potential, deep curiosity, and a serious willingness to learn, contribute, and take ownership.

I’m actively looking for an internship opportunity where I can:
• Learn directly from real execution
• Support the team meaningfully
• Grow fast by doing real work (not just observing)

I’m especially interested in Data Analytics / Python Development, and I’ve been independently building skills in this space through self-learning, hands-on practice, and constant experimentation.

I don’t expect hand-holding — I value feedback, responsibility, and high standards. Even if it starts small , I’d love the chance to prove my value through effort and consistency.

If there’s any scope to collaborate, intern, or even just receive guidance, I’d be extremely grateful. Either way, thank you for building something inspiring — it motivates people like me more than you might realize.

I have attached my resume for your reference.

Looking forward to hearing from you.

Warm regards,  
Ayush Kumar
"""

    msg = MIMEMultipart()
    msg['Subject'] = f"Internship Inquiry - Data Analyst / Python Developer at {company}"
    msg['From'] = "ayush22kumar2004@gmail.com"
    msg['To'] = email

    msg.attach(MIMEText(body, 'plain'))

    part = MIMEBase('application', 'octet-stream')
    with open(resume_path, 'rb') as file:
        part.set_payload(file.read())

    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="Ayush_Kumar_Resume.pdf"')
    msg.attach(part)

    for i in range(5):
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login("ayush22kumar2004@gmail.com", "my password here ")

            server.send_message(msg)
            server.quit()

            print(f"Sent to {name} at {company}")

            with open(log_file, "a") as f:
                f.write(email + "\n")

            break

        except Exception as e:
            print(f"Attempt {i+1} failed for {email}: {e}")

            if i < 4:
                print("Retrying in 5 minutes...")
                time.sleep(300)
            else:
                print("All attempts failed.")

    time.sleep(60)
