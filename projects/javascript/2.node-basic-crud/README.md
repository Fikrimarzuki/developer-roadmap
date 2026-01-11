# Nodejs Basic CRUD

Node.js basic crud.

## Installation
```
npm install
```

## Run the Project
```
node index.js
```

## API Routes
- GET `/`
  ```
  Hello World!
  ```
- GET `/users`
  ```
  [
    {
      "id": 1,
      "name": "Javaskip",
      "email": "javaskip@mail.com"
    }
  ]
  ```
- POST `/users`
  ```
  {
    "name": "Pythonia",
    "email": "pythonia@mail.com"
  }
  ```
- PATCH `/users/:id`
  ```
  {
    "name": "Javascript"
  }
  ```
- PUT `/users/:id`
  ```
  {
    "name": "New Javascript",
    "email": "new_js@mail.com"
  }
  ```
- DELETE `/users/:id`
  

