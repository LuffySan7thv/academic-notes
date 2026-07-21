FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --default-timeout=100 --index-url https://pypi.org/simple --trusted-host pypi.org -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]