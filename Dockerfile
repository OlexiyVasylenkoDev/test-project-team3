FROM python:3.10

RUN mkdir /Backend

WORKDIR /Backend

COPY Backend .

RUN python -m pip install --upgrade pip

RUN pip install -U pipenv && pipenv install --system

CMD ["sh", "-c", "python src/manage.py makemigrations && \
                  python src/manage.py migrate && \
                  python src/manage.py collectstatic --noinput && \
                  python src/manage.py loaddata db.json && \
                  python src/manage.py runserver 0:8000"]
