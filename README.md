# Todo App - API Gateway

A FastAPI-based API Gateway that routes requests to multiple microservices (Auth, Users, Tasks, Admin). This project demonstrates microservices architecture, centralized routing, and containerization with Docker.

## 🎯 Project Overview

This API Gateway acts as a single entry point for all client requests and routes them to appropriate backend services. It includes:

- **Authentication Service** (`/api/v1/auth`) - User login, registration, tokens
- **User Service** (`/api/v1/users`) - User profile management
- **Tasks Service** (`/api/v1/tasks`) - Todo/task management
- **Admin Service** (`/api/v1/admin`) - Administrative operations

## 🏗️ Architecture

```
Client Requests
    ↓
API Gateway (gateway.py)
    ├─ /api/v1/auth → Authentication Service
    ├─ /api/v1/users → User Service
    ├─ /api/v1/tasks → Tasks Service
    └─ /api/v1/admin → Admin Service
    ↓
Database (SQLite)
```

## 📚 Key Concepts Covered

### 1. **Microservices Architecture**
- Decoupled services that handle specific domains
- Each service has its own router
- Independent deployment capability

### 2. **API Gateway Pattern**
- Single entry point for all requests
- Centralized routing with `/api/v1` prefix
- Simplifies client integration

### 3. **Request Routing**
- Routes incoming requests to appropriate services
- Maintains consistent API structure
- Easy to add/remove services

### 4. **FastAPI Framework**
- Async Python web framework
- Auto-generated API documentation (Swagger UI)
- Type hints and validation

### 5. **Database Integration**
- SQLAlchemy ORM
- SQLite database
- Alembic migrations

### 6. **Authentication & Authorization**
- JWT token-based auth
- bcrypt password hashing
- OAuth2 implementation

### 7. **Containerization (Docker)**
- Dockerfile for image creation
- docker-compose for orchestration
- Consistent deployment across environments

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Docker & Docker Compose (optional)
- Git

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd "todo App"

# Install dependencies
pip install -r requirements.txt
```

### 🚀 Quick Start (5 Steps)

1. **Verify Gateway is Running**
```bash
# Start the gateway
python gateway.py
# OR: uvicorn gateway:app --reload
```

2. **Check Health**
```bash
curl http://localhost:8000/health
```

3. **Access API Documentation**
   - Interactive: `http://localhost:8000/docs`
   - Alternative: `http://localhost:8000/redoc`

4. **Test Auth Endpoint**
```bash
curl -X POST http://localhost:8000/api/v1/auth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=testpassword"
```

5. **Use Custom Port** (if 8000 is busy)
```bash
uvicorn gateway:app --port 8001
```

### Run with Docker

**Option 1: Using docker-compose**
```bash
# Start
docker-compose up

# Stop
docker-compose down

# View logs
docker-compose logs -f
```

**Option 2: Using Docker directly**
```bash
# Build image
docker build -t my-gateway .

# Run container
docker run -p 8000:8000 my-gateway
```

## 📋 API Endpoints

### Authentication Service (`/api/v1/auth`)
```
POST   /api/v1/auth/token        - User login
POST   /api/v1/auth/signup       - Register new user
POST   /api/v1/auth/email        - Email verification
POST   /api/v1/auth/refresh-token - Refresh token
```

### User Service (`/api/v1/users`)
```
GET    /api/v1/users             - Get all users
GET    /api/v1/users/{user_id}   - Get specific user
PUT    /api/v1/users/{user_id}   - Update user
DELETE /api/v1/users/{user_id}   - Delete user
```

### Tasks Service (`/api/v1/tasks`)
```
GET    /api/v1/tasks             - Get all tasks
GET    /api/v1/tasks/{task_id}   - Get specific task
POST   /api/v1/tasks             - Create task
PUT    /api/v1/tasks/{task_id}   - Update task
DELETE /api/v1/tasks/{task_id}   - Delete task
```

### Admin Service (`/api/v1/admin`)
```
GET    /api/v1/admin             - Admin dashboard
POST   /api/v1/admin             - Admin operations
```

## 📁 Project Structure

```
todo App/
├── gateway.py              # API Gateway entry point
├── main.py                 # Original FastAPI app
├── models.py               # Database models (Users, Tasks)
├── database.py             # Database configuration
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container image definition
├── docker-compose.yml      # Docker orchestration
├── .env.example            # Environment variables template
├── secrets.env             # Secret configurations
├── QUICKSTART.md           # Quick start guide
├── README.md               # This file
├── alembic.ini             # Database migration config
├── routers/                # Microservices
│   ├── auth.py             # Authentication service
│   ├── user.py             # User service
│   ├── tasks.py            # Tasks service
│   └── admin.py            # Admin service
├── pydantics/              # Request/Response schemas
│   ├── user.py
│   ├── tokens.py
│   ├── taskrequest.py
│   └── userupdates.py
└── alembic/                # Database migrations
```

## 🔑 Technology Stack

| Technology | Purpose |
|-----------|---------|
| **FastAPI** | Web framework |
| **Uvicorn** | ASGI server |
| **SQLAlchemy** | ORM |
| **SQLite** | Database |
| **Pydantic** | Data validation |
| **Python-Jose** | JWT tokens |
| **Passlib + Bcrypt** | Password hashing |
| **Alembic** | Database migrations |
| **Docker** | Containerization |

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
app.include_router(new_service.router, prefix="/api/v1/new-service")
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

**Ready to use!** Start with `python gateway.py` or `docker-compose up`
