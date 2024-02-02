FROM python:3.9-slim

WORKDIR /app

COPY ./app /app/app
COPY ./tests /app/tests
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV APP_ENV=production

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
