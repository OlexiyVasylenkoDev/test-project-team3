FROM python:3.10

RUN mkdir /Backend

WORKDIR /Backend

COPY . .

RUN apt-get update

RUN python -m pip install --upgrade pip

RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y

RUN pip install -U pipenv && pipenv lock && pipenv install --system

CMD ["sh", "-c", "python src/manage.py makemigrations && \
                  python src/manage.py migrate && \
                  python src/manage.py collectstatic --noinput && \
                  python src/manage.py loaddata db.json && \
                  python src/manage.py runserver 0:8000"]
