FROM python:3.11 as RUNNER
WORKDIR /app

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .
ENTRYPOINT ["python3", "main.py"]
