# 🎉 Auto Birthday Wisher (Python)

This script automatically checks today’s date, finds whose birthday it is in the CSV file, loads a letter template, replaces the [name] placeholder, and sends a birthday email via SMTP.

--- 

## 🚀 Features

- Auto detects birthdays based on today’s date

- Reads birthday data from CSV file

- Uses letter templates from .txt

- Secure authentication via .env

- Customizable SMTP server

--- 

## 🧰 Used Technologies

- Python 3.10+

- Pandas

- smtplib

- python-dotenv

- datetime

--- 

## 📦 Project Structure
```bash
auto-birthday-wisher/
├─ .venv/
├─ assets/
│  └─ images/
│     └─ received_email.jpg
├─ config/
│  ├─ .env              # REAL secrets (gitignored)
│  └─ .env.example      # fake template 
├─ data/
│  ├─ birthdays.csv     # recipients (name, email, year, month, day)
│  └─ letter_1.txt      # birthday letter template
├─ src/
│  └─ main.py           # main script (entry point)
├─ .gitignore
├─ LICENSE              # MIT license
├─ README.md
└─ requirements.txt

--- 

## 🔐 Environment Setup

- create and edit the .env file inside config:

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password

- use the .env.example as a template.

--- 

## 📝 CSV Example

data/birthdays.csv

name   | email	          | year | month	| day
Khaled |khaled@gmail.com  |2003  |  4       |  23
	
Sara   |sara@hotmail.com  |1999  |  8       |  10
	
--- 

## 👨‍💻 Author

Khaled Elsayed

## 📄 License © 2025

- This project is licensed under the MIT License.
- See LICENSE file for more details.