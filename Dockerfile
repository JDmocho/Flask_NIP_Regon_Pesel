FROM python:3.6.9

ARG APP_DIR=/usr/src/flask-nip-regon-pesel

WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p $APP_DIR
ADD validator/ $APP_DIR/validator/
ADD run.py $APP_DIR

CMD PYTHONPATH=$PYTHONPATH:/usr/src/flask-nip-regon-pesel \
    FLASK_APP=validator flask run --host=0.0.0.0