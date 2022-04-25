FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /server
COPY Pipfile /server/
RUN pip install pipenv && pipenv lock && pipenv install --system
COPY ./backend/ /server