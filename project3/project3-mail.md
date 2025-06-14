# 🧠 Project 3: Mail – CS50W

This is my solution for **Project 3: Mail** from Harvard’s [CS50’s Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/). This project is a **single-page email client** built using **Django**, **JavaScript**, **HTML/CSS**, and the **Fetch API**, allowing users to send, receive, view, archive, and reply to emails.

---

## 🚀 Features

- ✅ User authentication (login, logout, register)
- ✅ Send email to one or more registered users
- ✅ View Inbox, Sent, and Archived mailboxes
- ✅ Mark emails as read/unread
- ✅ Archive and unarchive received emails
- ✅ View full email content
- ✅ Reply to emails with pre-filled form (To, Subject, and Quoted Body)
- ✅ SPA behavior — navigation handled with JavaScript and dynamic DOM manipulation

---

## 🛠️ Technologies Used

- **Python** with **Django** (backend + API)
- **JavaScript** for front-end logic and view switching
- **HTML/CSS** for page structure and styling
- **Bootstrap** for responsive layout
- **Fetch API** for asynchronous requests
- **SQLite** with Django ORM

---

## 📦 Getting Started

1. **Download starter files**  
   [`mail.zip`](https://cdn.cs50.net/web/2020/spring/projects/3/mail.zip)

2. **Unzip and navigate**  
   ```bash
   cd mail
   ```

3. **Make and apply migrations**  
   ```bash
   python manage.py makemigrations mail
   python manage.py migrate
   ```

4. **Run the development server**  
   ```bash
   python manage.py runserver
   ```

5. **Register and test**  
   Open `http://127.0.0.1:8000` and register with a test email (e.g., `test@example.com`)

---

## 📁 App Structure

- `mail/models.py`: Defines Email and User models (already done)
- `mail/views.py`: Contains backend routes and API logic (pre-written)
- `mail/static/mail/inbox.js`: Your main working file — all front-end logic
- `mail/templates/mail/inbox.html`: Main HTML layout with placeholders
- `mail/static/mail/styles.css`: CSS styles for the UI

---

## ✅ What I Learned

- Building SPAs using dynamic view toggling
- Making `GET`, `POST`, and `PUT` requests with `fetch()`
- Structuring interactive interfaces using DOM manipulation
- Managing client-side state with JavaScript
- Implementing features like reply/archiving through event-driven programming
- Reading and updating JSON responses from REST APIs
- Using Django’s templating system and static file setup

---

## 🧠 Challenge Highlights

- Implementing `archive/unarchive` logic via `PUT` requests
- Rendering mailbox views dynamically from JSON data
- Adding reply logic with proper subject/body formatting
- Tracking read status and updating the UI accordingly
- Ensuring clean navigation and view hiding/showing transitions

---

## 📌 Specification Reference

Full spec: [CS50W Project 3 Specification](https://cs50.harvard.edu/web/2020/projects/3/mail/)

---

> _This project was a deep dive into SPA design, DOM control, and client-server communication — a great foundation for future front-end development projects!_

---