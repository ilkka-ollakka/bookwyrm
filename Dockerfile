FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /app /app/static /app/images

WORKDIR /app

RUN apt-get update && apt-get install -y gettext libgettextpo-dev tidy && apt-get clean

WORKDIR /app

COPY pyproject.toml /app/
RUN python -mvenv /venv
ENV PATH=/venv/bin:$PATH
RUN pip install --compile . --no-cache-dir


FROM python:3.11-slim

RUN apt-get update && apt-get install -y gettext libpq5 tidy && apt-get clean


RUN addgroup --system app && adduser --system --group bookwyrm
WORKDIR /app
USER bookwyrm
COPY --from=build-image /venv /venv
COPY README.md LICENSE.md pyproject.toml /app/
ENV PYTHONUNBUFFERED=1
ENV PATH=/venv/bin:$PATH
