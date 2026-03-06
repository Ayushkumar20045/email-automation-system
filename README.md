🚀 Automated Email Outreach System

An intelligent Python-based automation system that sends personalized emails to HRs daily using dynamic data and scheduling via cron.

Designed to scale job outreach efficiently while maintaining personalization.

⸻

📌 Features

	•	📧 Sends automated personalized emails daily
	
	•	🔄 Dynamic data fetching from Google Sheets / CSV
	
	•	⏰ Scheduled execution using cron (macOS)
	
	•	🧠 Template-based email customization
	
	•	🚫 Prevents repetitive manual work
	
	•	📈 Scalable for large HR datasets

⸻

🛠 Tech Stack
	•	Python
	•	Pandas
	•	SMTP (Gmail)
	•	Cron Jobs (macOS Scheduler)
	•	Google Sheets (CSV Integration)

⸻

⚙️ How It Works
	1.	📊 Fetch HR data (Name, Email, Company) from CSV/Google Sheets
	2.	🔁 Select one HR daily using rotation logic
	3.	✍️ Generate personalized email using template
	4.	📤 Send email using SMTP
	5.	⏰ Cron job triggers script automatically every day
  email-automation-system/
│
├── email_script.py
├── requirements.txt
├── README.md
├── .gitignore
└── sample_data.csv
Setup Instructions

1️⃣ Clone Repository

git clone https://github.com/Ayushkumar20045/email-automation-system.git

cd email-automation-system

2️⃣ Install Dependencies

 pip install -r requirements.txt

3️⃣ Configure Email Credentials

⚠️ Use Gmail App Password  

server.login("your_email@gmail.com", "your_app_password")

4️⃣ Run Script Manually

python3 email_script.py

5️⃣ Automate Using Cron (Mac)

crontab -e

0 10 * * * /opt/homebrew/bin/python3 /path/to/email_script.py



💡 Real-World Use Case

This system automates job applications by sending consistent, personalized outreach emails to HRs daily — increasing visibility and response chances.

⸻

🚀 Future Improvements

	
	•	📊 Email tracking system (logs/dashboard)
	
	•	⏱ Randomized sending time (human-like behavior)
	
	•	🤖 AI-based personalization (LLM integration)
	
	•	🌐 Web dashboard (Streamlit)

⸻

**👨‍💻 Author
Ayush Kumar**

 


