# Horus Exam Backend (Flask + Postgres)

Backend API sederhana untuk manajemen **users** (registrasi, login, list, detail, update, delete) dengan **Flask + SQLAlchemy + Postgres**. Cocok buat tugas/demo dashboard yang butuh auth minimal (JWT).

## Tech Stack
- Flask, Flask-SQLAlchemy, Flask-Migrate
- Flask-JWT-Extended (JWT), Flask-CORS
- Postgres (driver: psycopg2-binary)
- Optional dev tooling: `uv` (runner/pip), Docker (Postgres)

## Endpoints

### POST `/users/register`
Daftar user baru.
- **Body**
```json
{ "username": "aan", "password": "Passw0rd123", "email": "aan@example.com", "nama": "Aan" }
```
- **201** `{"message":"Registrasi berhasil"}`
- Error: `400 invalid_email/weak_password`, `409 username_taken/email_taken`

### POST `/users/login`
Autentikasi user.
- **Body**
```json
{ "username": "aan", "password": "Passw0rd123" }
```
- **200** `{"message":"Login berhasil","token":"<JWT>"}`

### GET `/users`
Ambil list semua user (tanpa password). **(Bisa dibuat protected jika mau.)**
- **200**
```json
[ { "id": 1, "username": "aan", "email": "aan@example.com", "nama": "Aan" } ]
```

### GET `/users/<id>`
Detail user. **(Opsional protected; atau pakai `/users/me` bila hanya owner.)**
- **200**
```json
{ "id": 1, "username": "aan", "email": "aan@example.com", "nama": "Aan" }
```

### PUT `/users/<id>` _(protected)_
Update data user (owner-only / admin).
- **Header**: `Authorization: Bearer <token>`
- **Body**
```json
{ "username": "aanv", "email": "aanv@example.com", "nama": "Aan V" }
```
- **200** `{"message":"Data user berhasil diperbarui"}`
- Error: `403 Forbidden` (bukan owner), `404 User tidak ditemukan`


### DELETE `/users/<id>` _(protected)_
Hapus user (owner-only / admin).
- **Header**: `Authorization: Bearer <token>`
- **200** `{"message":"User berhasil dihapus"}`
- Error: `403 Forbidden`, `404 Not Found`


## Status Kode Umum
- `200 OK` – Berhasil.
- `201 Created` – Registrasi sukses.
- `400 Bad Request` – Validasi gagal (email tidak valid, password lemah, dsb.).
- `401 Unauthorized` – Token hilang/invalid/expired.
- `403 Forbidden` – Sudah login tapi tidak punya izin (bukan owner/admin).
- `404 Not Found` – Resource tidak ditemukan.
- `409 Conflict` – Duplikasi (username/email sudah dipakai).

---
