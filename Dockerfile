FROM python:3.6
ENV PYTHONUNBUFFRERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
ADD main.py /app/
ADD base_teste[802].txt /app/
RUN pip install -r requirements.txt
ADD . /app/
# RUN python /app/main.py