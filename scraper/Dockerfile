FROM python:3.9.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
RUN python -m pip install --upgrade pip
COPY requirements.txt /app/

RUN pip3 install -r requirements.txt
COPY . /app/

EXPOSE 8000

COPY entrypoint.sh /app/entrypoint.sh
RUN ["chmod", "+x", "/app/entrypoint.sh"]
CMD ["/app/entrypoint.sh"] 