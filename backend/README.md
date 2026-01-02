# FloatChat Backend

A minimal FastAPI backend for FloatChat.

## Quick Start

1. Create/activate a virtual environment (optional if already set):

```powershell
Push-Location "A:\floatchat\backend"
python -m venv venv
venv\Scripts\Activate.ps1
Pop-Location
```

2. Install dependencies:

```powershell
Push-Location "A:\floatchat\backend"
venv\Scripts\python.exe -m pip install -r requirements.txt
Pop-Location
```

3. Run the dev server:

```powershell
Push-Location "A:\floatchat\backend"
venv\Scripts\python.exe -m uvicorn app.main:app --reload
Pop-Location
```

## API

- `GET /` → Health message
- `POST /chat` → Body: `{ "query": "your question" }`
