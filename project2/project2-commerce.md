# 🧠 Project 2: Commerce – CS50W

This is my solution for **Project 2: Commerce** from Harvard’s [CS50’s Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/). The project is an **eBay-style auction site** built using Django, where users can create listings, place bids, comment, and manage a watchlist.

---

## 🚀 Features

- ✅ User registration, login, and logout
- ✅ Create auction listings with title, description, start bid, image, and category
- ✅ View all active listings
- ✅ Listing detail page with bid form and comments
- ✅ Place bids (must be greater than current highest bid)
- ✅ Comment on listings
- ✅ Add/remove listings from a personal Watchlist
- ✅ Close auctions (creator only)
- ✅ Declare winner on closed listings
- ✅ Browse listings by category
- ✅ Django admin panel to manage listings, comments, and bids

---

## 🛠️ Technologies Used

- **Python** with **Django** (full-stack web framework)
- **HTML/CSS** and **Bootstrap** for front-end styling
- **Django ORM** for models and database interaction
- **SQLite** as the development database
- **Django Forms** for creating and validating listing/bid/comment forms

---

## 📦 Getting Started

1. **Download starter files**  
   [`commerce.zip`](https://cdn.cs50.net/web/2020/spring/projects/2/commerce.zip)

2. **Unzip and navigate**  
   ```bash
   cd commerce
   ```

3. **Set up database**  
   ```bash
   python manage.py makemigrations auctions
   python manage.py migrate
   ```

4. **Create superuser (optional)**  
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the server**  
   ```bash
   python manage.py runserver
   ```

6. **Visit site** at `http://127.0.0.1:8000` and register to begin testing

---

## 📁 App Structure

- `auctions/models.py`: Contains models for Listing, Bid, Comment, Watchlist
- `auctions/views.py`: Handles view logic and route responses
- `auctions/forms.py`: Django Forms for listings, bids, comments
- `auctions/templates/auctions/`: HTML templates
- `auctions/static/`: Optional custom CSS or assets
- `commerce/urls.py`: URL routing
- `admin/`: Django admin configuration

---

## ✅ What I Learned

- Designing relational models with Django’s ORM
- Validating business logic (e.g. bid validation)
- Creating secure user-specific features (e.g. Watchlist, permissions)
- Handling POST requests safely and cleanly
- Using Django’s templating engine for dynamic HTML rendering
- Working with Django’s admin panel for model management

---

## 🧠 Challenge Highlights

- Implementing Watchlist logic with conditional rendering
- Validating bid amounts against business rules
- Managing auction closing and winner assignment securely
- Structuring category views for scalability
- Using Django decorators (`@login_required`) for view protection

---

## 📌 Specification Reference

Full spec: [CS50W Project 2 Specification](https://cs50.harvard.edu/web/2020/projects/2/commerce/)

---

> _This project was a solid introduction to relational data modeling and feature-driven development in Django. It helped reinforce core concepts in web architecture, user logic, and form handling._

---