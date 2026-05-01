import bcrypt
from typing import Any

from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.persistencia.database.dependencies import get_db
from app.persistencia.repositories import UserRepository

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register")
async def register(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
) -> dict[str, Any]:
    """Registra un nuevo usuario en el sistema.

    - username: Nombre de usuario único.
    - password: Contraseña en texto plano.
    - db: Sesión de base de datos inyectada.

    Retorna los datos del usuario creado o un error si ya existe.
    """
    repository = UserRepository(db)

    # Verificar si el usuario ya existe
    existing_user = repository.get_user_by_username(username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre de usuario ya existe",
        )

    try:
        user = repository.create_user(username=username, password=password, role="developer")
        return {
            "id": user.id,
            "username": user.username,
            "role": user.role,
            "active_status": user.active_status,
        }
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error al crear el usuario. El nombre de usuario podría estar duplicado.",
        )


@router.post("/login")
async def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
) -> dict[str, Any]:
    repository = UserRepository(db)
    user = repository.get_user_by_username(username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
        )

    is_valid_password = bcrypt.checkpw(
        password.encode("utf-8"),
        user.password_hash.encode("utf-8"),
    )
    if not is_valid_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
        )

    return {
        "id": user.id,
        "username": user.username,
        "role": user.role,
    }
