FROM mishaga/python:3.12-poetry as production-dependencies

WORKDIR /opt
ENV PYTHONPATH=/opt

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --without dev

FROM production-dependencies as test

RUN poetry install --no-root

COPY ./ ./

FROM production-dependencies as production

ARG VERSION
RUN echo "${VERSION}" > "/var/version"

COPY ./ ./
