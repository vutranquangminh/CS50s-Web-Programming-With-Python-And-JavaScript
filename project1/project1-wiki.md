# 🧠 Project 1: Wiki – CS50W

This is my solution for **Project 1: Wiki** from Harvard’s [CS50’s Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/). The project is a **Wikipedia-like encyclopedia** that allows users to view, search, edit, and create entries using **Markdown**, all rendered dynamically through Django.

---

## 🚀 Features

- ✅ View encyclopedia entries rendered from Markdown
- ✅ Create new entries with title and Markdown content
- ✅ Edit existing entries via pre-populated form
- ✅ Search for entries by exact match or partial substring
- ✅ Show search results when no exact match is found
- ✅ Redirect to error page for non-existent entries
- ✅ Clickable links on index and results page
- ✅ Random entry page access
- ✅ Clean layout with sidebar navigation

---

## 🛠️ Technologies Used

- **Python** with **Django** (web framework)
- **HTML/CSS** for templating and design
- **Markdown2** library for rendering Markdown to HTML
- **Django Template Language** for rendering content
- Built-in file system storage for entry content

---

## 📦 Getting Started

1. **Download starter code**  
   [`wiki.zip`](https://cdn.cs50.net/web/2020/spring/projects/1/wiki.zip)

2. **Unzip and navigate**  
   ```bash
   cd wiki
   ```

3. **Install dependencies**  
   ```bash
   pip3 install markdown2
   ```

4. **Run server**  
   ```bash
   python manage.py runserver
   ```

5. **Open** `http://127.0.0.1:8000` to start browsing/editing your wiki

---

## 📁 App Structure

- `encyclopedia/views.py`: View logic for index, entry, search, edit, new, and random
- `encyclopedia/util.py`: Utility functions to list, retrieve, and save entries
- `encyclopedia/templates/encyclopedia/`: HTML templates
- `entries/`: Markdown files for each wiki page
- `urls.py`: Route management

---

## ✅ What I Learned

- Rendering Markdown as HTML in Django
- Managing user input through forms and GET/POST methods
- Using Django templates and filters (e.g. `|safe`)
- Routing logic for dynamic URL parameters (`/wiki/<title>`)
- Error handling and redirects in Django views
- Random content selection and file management

---

## 🧠 Challenge Highlights

- Converting user input into valid Markdown entries
- Search functionality with partial match filtering
- Edit view with pre-filled content using textarea
- Preventing overwrite of existing entries during creation
- Ensuring consistent routing and URL-safe title usage

---

## 📌 Specification Reference

Full spec: [CS50W Project 1 Specification](https://cs50.harvard.edu/web/2020/projects/1/wiki/)

---

> _This project was a great intro to dynamic content handling and Markdown rendering in Django, laying the foundation for content management systems and blogging platforms._

---