FROM python:alpine

RUN \
    pip install Flask \
    pip install -U flask-cors

WORKDIR /main
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000", "--reload"]