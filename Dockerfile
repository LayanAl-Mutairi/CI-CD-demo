FROM python:3.11-slim

WORKDIR /app

COPY app.py /app/app.py
COPY tests/ /app/tests/

RUN pip install Flask==2.3.2 pytest requests

EXPOSE 5000

CMD ["python", "app.py"]

