FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .env /app/

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./backend /app/backend

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]