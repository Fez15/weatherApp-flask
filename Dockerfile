# FROM ubuntu:latest

# RUN apt-get update -y\
#   && apt-get install -y python3-pip python3-dev build-essential \
#   && cd /usr/local/bin \
#   && ln -s /usr/bin/python3 python \
#   && pip3 install --upgrade pip

# ADD . /app
# WORKDIR /app

# RUN pip install -r requirements.txt

# #EXPOSE 5000

# ENTRYPOINT ["python"]
# CMD ["app.py"]

# # CMD ["/cmd.sh"]
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]