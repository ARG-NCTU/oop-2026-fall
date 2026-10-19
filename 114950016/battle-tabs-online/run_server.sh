#!/bin/bash
python3 -m pip install -r requirements.txt
python3 -m uvicorn server:app --host 0.0.0.0 --port 8000
