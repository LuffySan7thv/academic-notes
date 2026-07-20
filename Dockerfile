FROM python:3.10-slim

WORKDIR /app


RUN pip config set global.index-url https://mirror.iranserver.com/pypi/web/simple && \
    pip config set global.trusted-host mirror.iranserver.com

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]