# 🚨 Error Tracking & Debugging

This document tracks recurring issues, debugging notes, and known limitations throughout development.

---

# Status Legend


| Status | Meaning     |
| ------ | ----------- |
| 🟥     | Open        |
| 🟨     | In Progress |
| 🟩     | Fixed       |
| 🔵     | Enhancement |

---

# Current Issues

## AUTH-001

**Status:** 🟥

Title

```
Duplicate Email Registration
```

Description

```
User can attempt to register with an existing email.
```

Expected

```
Return HTTP 409 Conflict with a friendly error message.
```

---

## TASK-001

**Status:** 🟥

Title

```
Task Validation
```

Description

```
Empty task titles should not be accepted.
```

---

## NOTE-001

**Status:** 🟥

Title

```
Large Notes Performance
```

Description

```
Investigate rendering performance for very large notes.
```

---

## UI-001

**Status:** 🟨

Title

```
Responsive Dashboard
```

Description

```
Improve tablet and small-screen layouts.
```

---

## AI-001

**Status:** 🔵

Title

```
Roast Generator
```

Description

```
Add contextual AI-generated satirical reminders.
```

---

# Error Log Template

```
ID:

Date:

Component:

Description:

Steps to Reproduce:

Expected Result:

Actual Result:

Severity:

Assigned To:

Status:

Resolution:
```

---

# Debugging Checklist

* Verify environment variables.
* Check MongoDB Atlas connection.
* Inspect browser console.
* Review Flask logs.
* Confirm API status codes.
* Validate JWT/session.
* Check CORS configuration.
* Verify indexes in MongoDB.
* Test network requests.

---

# Future Monitoring

Recommended tools:

* Sentry
* Logtail
* Better Stack
* Grafana
* Prometheus

---

> **Remember:** If the bug disappears after adding `print()` statements, it has entered its canon event.
>
