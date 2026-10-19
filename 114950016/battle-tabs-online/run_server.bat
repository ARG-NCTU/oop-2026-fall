@echo off
python -m pip install -r requirements.txt
python -m uvicorn server:app --host 0.0.0.0 --port 8000
pause
