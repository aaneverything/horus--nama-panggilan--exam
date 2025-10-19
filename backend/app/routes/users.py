from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from . import users_bp
from ..services.user_service import(
    create_user,
    authenticate_user,
    list_users,
    update_user,
    delete_user
)
from flask_cors import CORS

@users_bp.post("/users/register")
def register():
    user, err = create_user(request.get_json() or {})
    if err == "missing_fields": return jsonify({"message": "Field wajib kurang"}), 400
    if err == "invalid_email": return jsonify({"message": "Email tidak valid"}), 400
    if err == "weak_password": return jsonify({"message": "Password lemah (>=8, huruf+angka)"}), 400
    if err == "username_taken": return jsonify({"message": "Username sudah dipakai"}), 409
    if err == "email_taken": return jsonify({"message": "Email sudah dipakai"}), 409
    return jsonify({"message": "Registrasi berhasil"}), 201
    
    
@users_bp.post("/users/login")
def login():
    data = request.get_json() or {}
    user = authenticate_user(data.get("username"), data.get("password"))
    if not user:
        return jsonify({"message": "Username atau password salah"}), 401
    token = create_access_token(identity=str(user.id))
    return jsonify({"message": "Login berhasil, token: " + token}), 200
    
@users_bp.get("/users")
def get_users():
    rows = list_users()
    return jsonify([
        {"id": int(u.id), "username": u.username, "email": u.email, "nama": u.nama}
        for u in rows
    ]), 200
    
@users_bp.put("/users/<int:user_id>")
def put_user(user_id: int):
    u, err = update_user(user_id, request.get_json() or {})
    if err == "not_found": return jsonify({"message": "User tidak ditemukan"}), 404
    if err == "username_taken": return jsonify({"message": "Username sudah dipakai"}), 409
    if err == "email_taken": return jsonify({"message": "Email sudah dipakai"}), 409
    if err == "invalid_email": return jsonify({"message": "Email tidak valid"}), 400
    return jsonify({"message": "Data user berhasil diperbarui"}), 200

@users_bp.delete("/users/<int:user_id>")
def del_user(user_id: int):
    ok, err = delete_user(user_id)
    if err == "not_found": return jsonify({"message": "User tidak ditemukan"}), 404
    return jsonify({"message": "User berhasil dihapus"}), 200