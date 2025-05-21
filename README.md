# 🏋️‍♂️ Be Fit!

**Be Fit!** is a web-based gym client management system built with **Python** and **Flask**. It provides a full-featured CRUD interface to manage client information such as name, surname, and membership. This app demonstrates clean separation of concerns using DAO, MySQL pooling, Flask-WTF forms, and Bootstrap 5 UI.


---

## 📋 Features

- 🧾 List all gym clients
- ➕ Add new client records
- 📝 Edit existing clients
- ❌ Delete clients
- 🧹 Reset form fields
- ✅ CSRF-protected form handling with Flask-WTF
- 🗃️ MySQL connection pooling with custom pool manager

---

## 🛠️ Tech Stack

| Layer      | Technology               |
|------------|--------------------------|
| Backend    | Flask, Python            |
| Forms      | Flask-WTF, WTForms       |
| Frontend   | HTML5, Bootstrap 5       |
| Database   | MySQL                    |
| DB Access  | Raw SQL via DAO pattern  |

---
## ⚙️ Getting Started
1. Clone the Repository:
git clone https://github.com/Belensanchez1989

2. Create a Virtual Environment:
 python -m venv venv 
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:
pip install flask flask-wtf mysql-connector-python

4. Configure Database:
 DATABASE = 'your_db'
USERNAME = 'your_username'
PASSWORD = 'your_password'

5. Run the App:
 python app.py

Then open your browser at:
http://localhost:5000
---
##  👨‍💻 Author
Built with ❤️ by Belén Sanchez


