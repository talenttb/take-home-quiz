FROM python:3.8
WORKDIR /app
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install pipenv && pipenv install --dev \
    && pipenv lock -r > requirements.txt \
    && pip install --requirement /app/requirements.txt

COPY . /app
CMD ["python", "/app/run.py","server"]