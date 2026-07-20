FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip config set global.index-url https://pypi.org/simple
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]