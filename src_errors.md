# Source Code Errors Report

The following is a list of errors, warnings, and formatting issues identified in the `src` codebase using `flake8` and `pylint`.

> [!WARNING]
> As requested, these errors have only been identified and listed. No automatic fixes have been applied.

## 1. Critical Errors / Bugs

### Function Redefinition
- **`src/auth/router.py`**: The function `login_url` is defined twice (at line 21 and again at line 39). This redefinition will cause the second implementation to overwrite the first. *(Pylint: E0102, Flake8: F811)*

## 2. Unused Variables & Imports

### Unused Local Variables
- **`src/auth/service.py`**: Local variable `e` is assigned to but never used (line 42). *(Flake8: F841)*

### Unused Imports
Many modules import classes or functions that are never used in the file. This can lead to unnecessary memory usage and clutter. *(Flake8: F401)*
- **`src/auth/schemas.py`**: `pydantic.EmailStr`
- **`src/auth/service.py`**: `src.auth.jwt.verify_token`, `datetime.datetime`
- **`src/note/router.py`**: `fastapi.templating.Jinja2Templates`, `src.config.database.conn`, `pymongo.MongoClient`, `pathlib.Path`, `bson.ObjectId`
- **`src/routes/about.py`**: `fastapi.templating.Jinja2Templates`, `src.config.database.conn`, `pymongo.MongoClient`, `pathlib.Path`, `bson.ObjectId`
- **`src/routes/dashboard.py`**: `fastapi.templating.Jinja2Templates`, `src.config.database.conn`, `pymongo.MongoClient`, `pathlib.Path`, `bson.ObjectId`
- **`src/routes/home.py`**: `fastapi.templating.Jinja2Templates`, `src.config.database.conn`, `pymongo.MongoClient`, `pathlib.Path`, `bson.ObjectId`
- **`src/task/router.py`**: `fastapi.templating.Jinja2Templates`, `src.config.database.conn`, `pymongo.MongoClient`, `pathlib.Path`, `bson.ObjectId`
- **`src/user/router.py`**: `fastapi.templating.Jinja2Templates`, `fastapi.HTTPException`, `src.config.database.conn`, `pymongo.MongoClient`, `pathlib.Path`, `bson.ObjectId`
- **`src/user/service.py`**: `src.user.schemas.USER`, `src.config.database.conn`, `src.config.settings.templates`

## 3. Formatting & Style Issues (PEP 8)

The codebase has widespread syntax styling deviations that violate PEP 8 standards.

### Indentation Errors
- **`src/auth/router.py`**: Indentation is not a multiple of 4, over-indented and under-indented continuation lines (lines 32, 33, 36, 40).
- **`src/auth/service.py`**: Indentation is not a multiple of 4, over-indented and under-indented continuation lines (lines 15, 19, 34, 42, 43, 47, 55, 56, 62, 64, 66, 69, 74, 75).
- **`src/note/schemas.py`**: Indentation is not a multiple of 4 (lines 4, 5).
- **`src/task/schemas.py`**: Indentation is not a multiple of 4 (lines 4, 5, 6).
- **`src/user/service.py`**: Indentation is not a multiple of 4 (line 7).

### Whitespace and Line Length Errors
- Missing whitespace around colons, commas, and keywords across multiple files (`src/auth/router.py`, `src/auth/schemas.py`, `src/auth/service.py`, `src/note/schemas.py`, `src/routes/dashboard.py`, `src/task/schemas.py`, `src/user/router.py`, `src/user/schemas.py`).
- Line lengths exceeding the 79 character limit in `src/auth/service.py` (lines 20, 27, 31, 71).
- Missing blank lines between function/class definitions in schemas and routers.
