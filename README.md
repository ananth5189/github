# Task manager App - FastAPI Backend

A modern FastAPI-based Todo application featuring user authentication, task management, and role-based access control. Built with SQLAlchemy ORM, JWT authentication, and database migrations using Alembic.

## 🎯 Project Overview

A full-featured Todo/Task management API with the following capabilities:

- **Authentication** - User registration, login, JWT token management
- **User Management** - User profiles, profile updates, address management
- **Task Management** - Create, read, update, delete tasks with priority levels
- **Admin Operations** - Administrative controls and user management
- **Role-Based Access** - Different permission levels for users and admins

## 🏗️ Project Structure

```
todo App/
├── main.py              # FastAPI app entry point with router imports
├── models.py            # SQLAlchemy database models (Users, Tasks)
├── database.py          # Database configuration and session management
├── requirements.txt     # Project dependencies
├── secrets.env          # Environment variables (not tracked in git)
├── alembic.ini          # Alembic migration configuration
│
├── routers/             # API endpoint handlers
│   ├── auth.py          # Authentication endpoints
│   ├── user.py          # User management endpoints
│   ├── tasks.py         # Task management endpoints
│   └── admin.py         # Admin operations endpoints
│
├── pydantics/           # Pydantic request/response models
│   ├── user.py          # User schemas
│   ├── taskrequest.py   # Task schemas
│   ├── userupdates.py   # User update schemas
│   └── tokens.py        # Token schemas
│
└── alembic/             # Database migration files
    ├── env.py
    ├── script.py.mako
    └── versions/        # Migration scripts
```

## 📊 Database Schema

### Users Table
- `id` - Primary key
- `username` - Unique username
- `email` - Unique email address
- `firstname`, `lastname` - User names
- `hashed_password` - Encrypted password
- `is_active` - Account status
- `role` - User role (user/admin)
- `address` - User address

### Tasks Table
- `id` - Primary key
- `title` - Task title
- `description` - Task description
- `priority` - Priority level (1-5)
- `complete` - Completion status
- `owner_id` - Foreign key to Users table

## 🎓 Key Technologies & Concepts

### FastAPI Framework
- Async Python web framework with automatic API documentation
- Type hints with Pydantic for request/response validation
- Built-in OpenAPI/Swagger UI support

### Database Layer
- **SQLAlchemy ORM** - Object-relational mapping for database operations
- **SQLite** - Lightweight database (tasksapp.db)
- **Alembic** - Database schema versioning and migrations

### Authentication & Security
- **JWT Tokens** - JSON Web Tokens for stateless authentication
- **OAuth2 + Bearer Tokens** - Standard authentication scheme
- **Passlib + Bcrypt** - Secure password hashing and verification

### Routing & API Structure
- Modular routers for different services (auth, users, tasks, admin)
- RESTful endpoints organized by functionality
- Centralized database session management

### Future Development Tools
- **pylint**, **flake8** - Code linting
- **pytest** - Unit testing framework
- **python-dotenv** - Environment variable management

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "folder_name"
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file with required variables
   # Copy secrets.env as reference
   ```

5. **Initialize the database**
   ```bash
   # Create tables
   python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
   ```

### Running the Application

**Start the FastAPI server**
```bash
python -m uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

### Accessing the API

- **Swagger UI Documentation**: `http://localhost:8000/docs`
- **Alternative API Docs (ReDoc)**: `http://localhost:8000/redoc`
- **OpenAPI Schema**: `http://localhost:8000/openapi.json`

## 📝 API Endpoints

### Authentication Routes (`/auth`)
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login user (returns JWT token)
- `POST /auth/refresh` - Refresh expired token

### User Routes (`/users`)
- `GET /users/{user_id}` - Get user profile
- `PUT /users/{user_id}` - Update user profile
- `GET /users` - List all users (admin only)
- `DELETE /users/{user_id}` - Delete user (admin only)

### Task Routes (`/tasks`)
- `GET /tasks` - Get all tasks for current user
- `POST /tasks` - Create a new task
- `GET /tasks/{task_id}` - Get specific task
- `PUT /tasks/{task_id}` - Update task
- `DELETE /tasks/{task_id}` - Delete task

### Admin Routes (`/admin`)
- `GET /admin/users` - List all users
- `GET /admin/stats` - Get application statistics
- `POST /admin/promote` - Promote user to admin
- `DELETE /admin/users/{user_id}` - Remove user

## 🗄️ Database Migrations with Alembic

### Creating a new migration
```bash
alembic revision --autogenerate -m "description of changes"
```

### Applying migrations
```bash
alembic upgrade head
```

### Viewing migration history
```bash
alembic history
```

### Reverting migrations
```bash
alembic downgrade -1
```

## 🔐 Environment Variables

Create a `.env` file or use `secrets.env`:
```
DATABASE_URL=sqlite:///tasksapp.db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 📦 Project Dependencies

**Core Framework**
- fastapi==0.104.1
- uvicorn[standard]==0.24.0

**Database**
- sqlalchemy==2.0.23
- alembic==1.13.1

**Authentication**
- python-jose[cryptography]==3.3.0
- passlib[bcrypt]==1.7.4

**Additional**
- pydantic==2.5.0
- python-dotenv==1.0.0

**Development & Testing**
- pytest==7.4.3
- black==23.12.0
- pylint==3.0.3
- flake8==6.1.0

## 🧪 Testing

Run tests with pytest:
```bash
pytest
# With coverage
pytest --cov=.
```

## 🛠️Future Development

### Code Formatting
```bash
black .
```

### Linting
```bash
pylint routers/ models.py main.py
flake8 .
```

## 💡 Usage Examples

### 1. Register a User
```bash
curl -X POST http://localhost:8000/api/v1/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword"
  }'
```

### 2. Login
```bash
curl -X POST http://localhost:8000/api/v1/auth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john_doe&password=securepassword"
```

### 3. Create a Task
```bash
curl -X POST http://localhost:8000/api/v1/tasks \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project",
    "description": "Finish API gateway setup"
  }'
```

### 4. Get Tasks
```bash
curl -X GET http://localhost:8000/api/v1/tasks \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### 5. Interactive Testing
Visit: `http://localhost:8000/docs` - Use Swagger UI to test all endpoints

## 🔐 Security

- JWT token-based authentication
- Bcrypt password hashing
- Environment variables for secrets (.env file)
- Database connection pooling

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Use different port
uvicorn gateway:app --port 8001
```

### Docker Won't Start
```bash
# Check if Docker is installed
docker --version

# Rebuild image
docker-compose up --build
```

### Database Connection Error
```bash
# Check database.py configuration
# Ensure database path is correct
# Verify file permissions
```

### Module Not Found
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

## 📦 Deployment

### Deploy to Cloud (Heroku, AWS, DigitalOcean)

1. **With Docker**
```bash
docker build -t my-gateway .
docker run -p 8000:8000 my-gateway
```

2. **Push to Registry**
```bash
docker tag my-gateway:latest username/my-gateway:latest
docker push username/my-gateway:latest
```

3. **Deploy using docker-compose**
```bash
docker-compose up -d
```

## 🤝 Development

### Adding a New Service

1. Create router in `routers/new_service.py`
2. Add to `gateway.py`:
```python
from routers import new_service
app.include_router(new_service.router)
```
3. Test at `http://localhost:8000/docs`

### Running Tests
```bash
# See individual service endpoints at /docs
```

## 📚 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [Docker Documentation](https://docs.docker.com/)
- [JWT Authentication](https://jwt.io/)

## 📝 Configuration

Edit `.env` file for custom settings:
```env
DATABASE_URL=sqlite:///./todos.db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🎓 Concepts Demonstrated

✅ **Microservices Architecture** - Modular service design  
✅ **API Gateway Pattern** - Centralized routing  
✅ **RESTful APIs** - Standard HTTP methods  
✅ **JWT Authentication** - Token-based security  
✅ **Database ORM** - SQLAlchemy  
✅ **Async Programming** - FastAPI async/await  
✅ **Docker & Containerization** - Deployment ready  
✅ **API Documentation** - Auto-generated Swagger UI  
✅ **Schema Validation** - Pydantic models  
✅ **Environment Configuration** - .env management  

## 📄 License

This project is open source and available under the MIT License.

## 📧 Contact

For questions or issues, please open a GitHub issue.

---

**Ready to use!** Start with `uvicorn main:app --reload` 
