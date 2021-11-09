FROM tiangolo/meinheld-gunicorn-flask:python3.8-alpine3.11

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --disabled-password 1001
RUN chown -R 1001 .
USER 1001
