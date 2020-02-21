FROM python:3.7
MAINTAINER NiJia <louis70109@gmail.com>
LABEL Name=flask-line-notify Version=0.0.1
WORKDIR /app
COPY ["requirements.txt", "/app/"]
RUN python3 -m pip install -r requirements.txt
ADD . /app
EXPOSE 5000
CMD ["python3", "-m", "api"]
