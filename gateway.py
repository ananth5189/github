from fastapi import FastAPI
import models
from database import Base, engine
from routers import auth, tasks, admin, user

app = FastAPI(title="API Gateway")

models.Base.metadata.create_all(bind=engine)

# Include all service routers
app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(user.router, prefix="/api/v1/users")
app.include_router(tasks.router, prefix="/api/v1/tasks")
app.include_router(admin.router, prefix="/api/v1/admin")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("gateway:app", host="127.0.0.1", port=8000, reload=True)
