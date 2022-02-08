FROM centos:7

RUN yum update -y
RUN yum -y install yum-utils
RUN yum -y install python36
RUN python3.6 -V
RUN yum -y install python36-pip
RUN pip3.6 install virtualenv

WORKDIR /app

ADD . /app

RUN pip3.6 install -r requirements.txt

CMD python3 main.py