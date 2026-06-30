# 🏗️ Architecture

## Overview

FlowMaxxing follows a modular three-tier architecture.

```
Frontend (HTML, CSS, JS)
        │
        ▼
 Flask Backend (Python)
        │
        ▼
 MongoDB Atlas
```

---

## Components

### Frontend

Responsible for:

* User Interface
* Forms
* Authentication pages
* Notes
* Tasks
* Dashboard
* Settings

No database logic exists here.

---

### Backend

Handles:

* Authentication
* CRUD Operations
* Validation
* AI Requests
* Session Management
* Business Logic

Routes communicate with MongoDB through models.

---

### Database

Collections:

```
users
tasks
notes
tags
focus_sessions
achievements
```

Every document references its owner using

```
userId
```

instead of creating separate collections for every user.

---

## Request Flow

```
Browser

↓

Flask Route

↓

Validation

↓

MongoDB

↓

JSON Response

↓

UI Update
```

---

## Authentication Flow

```
Register

↓

Create User

↓

Hash Password

↓

Store User

↓

Login

↓

Verify Password

↓

Create Session / JWT

↓

Authenticated Requests
```

---

## Design Principles

* Modular
* Scalable
* RESTful
* Separation of Concerns
* Minimal Dependencies
* Easy to Maintain
* Database Agnostic (future migration possible)

---

## Future Integrations

* Gemini AI
* Notifications
* Calendar Sync
* Discord Rich Presence
* Focus Timer
* Analytics Dashboard
* Aura Leaderboards
