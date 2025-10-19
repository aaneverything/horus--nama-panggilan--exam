from datetime import datetime
from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"
    __table_args__ = (
        db.UniqueConstraint("username", name="uq_users_username"),
        db.UniqueConstraint("email", name="uq_users_email"),
    )
    
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False, index=True)
    nama = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    
    def set_password(self, raw: str):
        self.password = generate_password_hash(raw)
    
    def check_password(self, raw: str) -> bool:
        return check_password_hash(self.password, raw)
    
