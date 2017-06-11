FROM python:3.6

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ENV MONGO_URI=mongodb://mongo/schools

WORKDIR /opt

ENTRYPOINT ["gunicorn", "-b :5000", "--workers=4", "ceeb.app:app"]
