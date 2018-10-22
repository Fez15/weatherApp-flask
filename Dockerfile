FROM ubuntu:latest

RUN apt-get update -y
#Timezone stuff
RUN apt-get install -y tzdata
RUN ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata
#Get python 3 for project to run
RUN apt-get install -y python3 
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev
#Get pip3
RUN pip3 install --upgrade pip
#Set up directories
COPY . /app
WORKDIR /app
EXPOSE 8000
#install requirements
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]

# CMD ["app.py"]
