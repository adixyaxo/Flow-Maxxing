# 📡 API Documentation

## Base URL

```
http://127.0.0.1:8000/
```

---

# Authentication

## Register

```
POST /api/auth/register
```

Request

```json
{
  "firstName": "",
  "lastName": "",
  "email": "",
  "password": ""
}
```

Response

```json
{
  "success": true,
  "message": "Account created."
}
```

---

## Login

```
POST /api/auth/login
```

---

## Logout

```
POST /api/auth/logout
```

---

# Tasks

## Get Tasks

```
GET /api/tasks
```

---

## Create Task

```
POST /api/tasks
```

---

## Update Task

```
PUT /api/tasks/:id
```

---

## Delete Task

```
DELETE /api/tasks/:id
```

---

## Complete Task

```
PATCH /api/tasks/:id/complete
```

---

# Notes

```
GET /api/notes
POST /api/notes
PUT /api/notes/:id
DELETE /api/notes/:id
```

---

# Tags

```
GET /api/tags
POST /api/tags
DELETE /api/tags/:id
```

---

# Focus Sessions

```
GET /api/focus
POST /api/focus
```

---

# AI

```
POST /api/ai/summarize

POST /api/ai/roast

POST /api/ai/planner
```

---

## Response Format

Successful

```json
{
    "success": true,
    "data": {}
}
```

Error

```json
{
    "success": false,
    "message": "Something went wrong."
}
```

---

## Authentication

Protected endpoints require

```
JWT Token
```

or Session Cookie depending on deployment.
