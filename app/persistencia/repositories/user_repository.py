import bcrypt
from sqlalchemy.orm import Session

from app.persistencia.models.models import User


class UserRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_user(self, username: str, password: str, role: str) -> User:
        """Crea un nuevo usuario con contraseña hasheada.

        - username: Nombre de usuario único.
        - password: Contraseña en texto plano (será hasheada).
        - role: Rol del usuario en el sistema (ej: 'developer', 'admin').

        Retorna el usuario creado.
        """
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

        user = User(
            username=username,
            password_hash=password_hash,
            role=role,
            active_status=True,
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_username(self, username: str) -> User | None:
        """Busca un usuario por su nombre de usuario.

        Retorna el usuario si existe, de lo contrario None.
        """
        return self.db.query(User).filter(User.username == username).first()
