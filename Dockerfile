# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG PYTHON_VERSION=3.12.1
FROM python:${PYTHON_VERSION}-alpine as base
RUN apk update \
    && apk upgrade \
    && apk add --no-cache build-base \
        autoconf \
        bash \
        bison \
        boost-dev \
        cmake \
        flex \
        libressl-dev \
        zlib-dev

RUN  apk add make gcc g++
# Prevents Python from writing pyc files.
# ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

ARG apiKey

ENV AV_KEY=${apiKey}

WORKDIR /app


# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN python -m pip install pipenv

# Copy the Pipfile and Pipfile.lock to the container.
COPY Pipfile ./
COPY Pipfile.lock ./
COPY requirements.txt ./
RUN python -m pipenv install
RUN python -m pip install -r requirements.txt
# Copy the source code into the container.
COPY . .

EXPOSE 80
# Run the application.
CMD pipenv run uvicorn app:app --host 0.0.0.0 --port 80
