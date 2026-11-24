FROM python:3.12-slim

WORKDIR /usr/src/app

COPY . .

EXPOSE 80

CMD ["python", "app.py"]
