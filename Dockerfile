FROM python:3.7
LABEL Name=flask-line-notify Version=0.0.1
WORKDIR /app
COPY ["requirements.txt", "/app/"]
RUN python3 -m pip install -r requirements.txt
ADD . /app
ENV FLASK_APP=app.py
EXPOSE 8000
# CMD ["gunicorn", "api:app", "--log-file=-"]
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]