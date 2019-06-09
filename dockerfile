FROM centos:7
RUN yum -y update && yum clean all
RUN yum reinstall -y glibc-common && yum clean all
RUN yum install -y vim && yum clean all
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py --user
RUN pip install awscli --upgrade --user



