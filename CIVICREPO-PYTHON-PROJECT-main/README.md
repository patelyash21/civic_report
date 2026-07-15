# CIVICREPO-PYTHON-PROJECT

🏙 Civic Issue Reporting System

A web-based Civic Issue Reporting System built using Django that allows citizens to report public issues such as road damage, garbage problems, water leakage, and more.

This system helps bridge the gap between citizens and municipal authorities by enabling easy complaint submission and status tracking.

🚀 Features

🔐 User Registration & Login

📝 Submit Civic Issues

📷 Upload Images of Issues

📍 Add Location Details

📊 Track Complaint Status (Pending / In Progress / Resolved)

🛠 Admin Panel to Manage Reports

📂 Dashboard to View Submitted Complaints

🛠 Tech Stack

Backend: Python, Django

Frontend: HTML, CSS, Bootstrap (Optional)

Database: SQLite (Default Django DB)

Authentication: Django Built-in Auth System

Image Upload: Pillow

📁 Project Structure
civic_project/
│
├── civic_project/
│   ├── settings.py
│   ├── urls.py
│
├── reports/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│
├── media/
├── db.sqlite3
├── manage.py
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/sonu677/CIVICREPO-PYTHON-PROJECT.git
cd civic-issue-reporting
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt

If you don’t have requirements.txt:

pip install django pillow
4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser
python manage.py createsuperuser
6️⃣ Run Server
python manage.py runserver

Open browser:

http://127.0.0.1:8000/

Admin Panel:

http://127.0.0.1:8000/admin/
🗄 Database Model
Report Model Fields:

User (ForeignKey)

Title

Description

Category

Image

Location

Status

Created At

🔮 Future Enhancements

📍 Google Maps Integration

📧 Email Notifications

📊 Admin Analytics Dashboard

📱 Responsive UI Design

🔔 Real-time Status Updates

🌍 REST API Integration

🤖 AI-based Issue Detection from Images

🎯 Learning Outcomes

This project demonstrates:

Django Models & ORM

Authentication System

CRUD Operations

File Upload Handling

Admin Customization

URL Routing

Template Rendering

🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit pull requests.

📜 License

This project is open-source and available under the MIT License.


