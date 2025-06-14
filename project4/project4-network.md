# 🧠 Project 4: Network – CS50W

This is my solution for **Project 4: Network** from Harvard's [CS50’s Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/). The project is a **social network web application** that allows users to register, post, follow, like, and interact with each other — all implemented using **Django**, **JavaScript**, and **HTML/CSS**.

---

## 🚀 Features

- ✅ User registration, login, and logout
- ✅ New post creation (text-based)
- ✅ All posts feed with pagination (10 posts per page)
- ✅ User profiles with follower/following stats
- ✅ Follow/Unfollow other users
- ✅ "Following" feed showing only followed users' posts
- ✅ Edit own posts inline using JavaScript (without page reload)
- ✅ Like/Unlike posts asynchronously using `fetch` API
- ✅ Responsive UI and clean layout using Bootstrap

---

## 🛠️ Technologies Used

- **Python** with **Django** (back-end)
- **JavaScript** with `fetch()` for async requests
- **HTML/CSS** and **Bootstrap** (front-end)
- **SQLite** database with Django ORM
- **Django Paginator** for backend pagination
- Django’s `AbstractUser` for custom user model extension

---

## 🧩 Getting Started

### 📦 Setup

1. **Download distribution code**  
   From: [`network.zip`](https://cdn.cs50.net/web/2020/spring/projects/4/network.zip)

2. **Unzip and navigate**  
   ```bash
   cd project4
   ```

3. **Set up database**  
   ```bash
   python manage.py makemigrations network
   python manage.py migrate
   ```

4. **Run development server**  
   ```bash
   python manage.py runserver
   ```

5. **Register a user in the browser**  
   Visit `http://127.0.0.1:8000`, click **Register**, and create an account.

---

## 📁 App Structure

- `network/models.py`: User, Post, Like, Follower models
- `network/views.py`: Django views for routes (index, login, logout, register, posts API)
- `network/templates/network/`: HTML templates
- `network/static/network/`: CSS and JavaScript
- `network/urls.py`: URL routing
- `admin/`: Django admin site support

---

## ✅ What I Learned

- Full-stack Django development (models, views, templates, forms)
- Implementing RESTful endpoints with Django views and JSON
- Building dynamic UIs using JavaScript and asynchronous fetch calls
- Handling authentication and permission checks
- Implementing pagination using Django’s `Paginator` class
- Structuring scalable Django apps with reusable templates
- Working with relational models (ForeignKey, ManyToMany)
- JavaScript DOM manipulation and event handling

---

## 🧠 Challenge Highlights

- Inline editing and like/unlike features using JavaScript without full-page reload
- Secure permission handling to restrict post edits to only owners
- Real-time updates to like count and post edits via `fetch()` and JSON APIs

---

## 📌 Specification Reference

Full spec: [CS50W Project 4 Specification](https://cs50.harvard.edu/web/2020/projects/4/network/)

---

> _This project is part of my journey in mastering full-stack web development. Feel free to explore the code and reach out with feedback or suggestions!_

---