# FastAPI Basic CRUD

## Prequesite
- siapkan venv
- aktifkan venv
- install fastapi
- jalankan

## Endpoint 
- POST `/users`
  body:
  ```json
  { "name": "Pythonia", "email": "Pythonia@mail.com" }
  ```
- GET `/users`
- GET `/users/:id`
- PUT `/users/:id`
- PATCH `/users/:id`
- DELETE `/users/:id`

## Notes
- Saat ini kalau cek melalui swagger akan terlihat bahwa POST `/users` masih tidak ada parameter, hal ini karena membutuhkan parameter `request: Request`
