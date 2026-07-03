from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    Header
)
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from database import engine, get_db
from models import Base, User
from schemas import UserCreate
from auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Authentication API Running"}


@app.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    # Check if email already exists
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    print(user.password)    
    print(type(user.password))
    print(len(user.password))
    # Hash password
    hashed_pw = hash_password(user.password)

    # Create user
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw
    )

    # Save to DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }

from auth import (
    hash_password,
    verify_password,
    create_access_token
)

from schemas import UserCreate, UserLogin

@app.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    # Find user
    db_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    # Check user exists
    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials"
        )

    # Verify password
    if not verify_password(
        form_data.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials"
        )

    # Create token
    access_token = create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.get("/dashboard")
def dashboard(
    current_user: User = Depends(get_current_user)
):

    return {
        "message": f"Welcome {current_user.username}",
        "email": current_user.email
    }