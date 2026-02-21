# helloworld

Simple Flask app that serves a small UI and shows current weather for Sydney, Australia.

Quick start

1. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and add your OpenWeatherMap API key:

```powershell
copy .env.example .env
# then edit .env and set OPENWEATHER_API_KEY
```

4. Run the app:

```powershell
python helloworld_test.py
# open http://127.0.0.1:5000/
```

Notes
- The app reads `OPENWEATHER_API_KEY` from the environment. If not set, the UI will show a fallback message.
- Tests are present in `helloworld_test.py` and use Flask's `test_client`.

