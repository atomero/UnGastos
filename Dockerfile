FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD UnGastos/requirements.txt /code/
RUN pip install --upgrade 'pip==10' && pip install -r requirements.txt
ADD . /code/
