import os
os.chdir("/Users/ayush/Desktop/python self")
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Google Sheet CSV link
sheet_url = "https://docs.google.com/spreadsheets/d/1k25FS3048Ovae_WrycxCScvuSfwkrekN/export?format=csv"

# Load data
df = pd.read_csv(sheet_url)

# Pick one HR daily (rotation)
index = datetime.now().day % len(df)
row = df.iloc[index]

# Extract details (make sure column names match your sheet)
name = row['First Name']
email = row['Email']
company = row['Company Name']

# Email body (your template filled)
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

Looking forward to hearing from you.

Warm regards,  
Ayush Kumar
"""

# Email setup
msg = MIMEText(body)
msg['Subject'] = f"Internship Inquiry - Data Analyst / Python Developer at {company}"
msg['From'] = "ayush22kumar2004@gmail.com"
msg['To'] = email

# Send email
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("ayush22kumar2004@gmail.com", "@Ayush#6390")
server.send_message(msg)
server.quit()

print(f"Email sent to {name} at {company}")