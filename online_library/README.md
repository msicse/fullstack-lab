# 📚 Online Library - Setup Instructions

A modern Django-based online library management system with user authentication, book browsing, reviews, and role-based permissions.

## 🚀 Features

- **User Authentication**: Sign up, login, logout with role-based access
- **Book Management**: Browse books with search, filtering, and pagination
- **Review System**: Users can write and view book reviews
- **Admin Panel**: Full admin interface for managing books, categories, and users
- **Responsive Design**: Clean, modern UI with Tailwind CSS
- **Role-Based Permissions**: User and Admin roles with different capabilities
- **Sidebar Layout**: Book details with reviews in an organized sidebar

## 📋 Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.8+** (Recommended: Python 3.11 or newer)
- **Git** (for version control)
- **Virtual Environment** (venv or virtualenv)

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/msicse/fullstack-lab.git
cd fullstack-lab/online_library
```

### 2. Create Virtual Environment

**On Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

Run database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 6. Load Sample Data (Optional)

If you want to populate the database with sample books and categories:

```bash
python manage.py populate_db
```

To add more sample books:

```bash
python manage.py add_more_books
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## 🌐 Application URLs

| URL | Description | Access Level |
|-----|-------------|--------------|
| `/` | Homepage with hero section and books | Public |
| `/books/` | Books listing without hero section | Public |
| `/books/<id>/` | Individual book details | Public |
| `/accounts/signup/` | User registration | Public |
| `/accounts/login/` | User login | Public |
| `/accounts/logout/` | User logout | Authenticated |
| `/admin/` | Django admin panel | Admin only |

## 👥 User Roles

### 🔵 User Role (Default)
- Browse and search books
- View book details
- Write and view reviews
- Update their own profile

### 🟢 Admin Role
- All User permissions
- Access to Django admin panel
- Manage books, categories, and users
- Full CRUD operations on all models

## 📁 Project Structure

```
online_library/
├── accounts/                 # User authentication app
│   ├── models.py            # UserProfile model with roles
│   ├── views.py             # Custom auth views
│   ├── urls.py              # Auth URL patterns
│   └── templates/           # Auth templates
├── books/                   # Main books app
│   ├── models.py            # Book, Category, Review models
│   ├── views.py             # Book listing, detail views
│   ├── urls.py              # Book URL patterns
│   ├── templates/           # Book templates
│   └── migrations/          # Database migrations
├── config/                  # Django project settings
│   ├── settings.py          # Main configuration
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py              # WSGI configuration
├── templates/               # Global templates
│   └── base.html            # Base template
├── media/                   # User uploaded files
├── static/                  # Static files
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file for environment-specific settings:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Django Settings

Key configuration in `config/settings.py`:

- **Database**: SQLite (default) - can be changed to PostgreSQL/MySQL
- **Media Files**: Configured for user uploads
- **Static Files**: Tailwind CSS via CDN
- **Authentication**: Custom user profiles with role system
- **Pagination**: 12 books per page

## 🎨 Frontend Features

- **Tailwind CSS**: Modern utility-first CSS framework
- **Responsive Design**: Mobile-friendly layout
- **Green Nature Theme**: Consistent color scheme
- **Sidebar Layout**: Book details with organized reviews
- **Search & Filtering**: Advanced book discovery
- **Pagination**: Efficient large dataset handling

## 🧪 Testing

Run Django tests:

```bash
python manage.py test
```

Check for any issues:

```bash
python manage.py check
```

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 5.2.7 | Web framework |
| Pillow | 11.3.0 | Image processing |
| asgiref | 3.9.2 | ASGI compatibility |
| sqlparse | 0.5.3 | SQL parsing |
| tzdata | 2025.2 | Timezone data |
