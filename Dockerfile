FROM python:3.11 as build
WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PATH=/venv/bin:$PATH
ENV UV_PROJECT_ENVIRONMENT=/venv
ENV UV_NO_CACHE=1
ENV UV_PYTHON_DOWNLOADS=never

RUN apt-get update && apt-get install -y gettext libpq5 tidy && apt-get clean

RUN pip install --no-cache-dir uv
ENV PATH=/venv/bin:$PATH
COPY README.md LICENSE.md pyproject.toml VERSION /app/
COPY manage.py gunicorn.conf.py /app/
COPY celerywyrm /app/celerywyrm
COPY bookwyrm /app/bookwyrm
COPY locale /app/locale
RUN uv sync


FROM python:3.11-slim
RUN addgroup --system app && adduser --system --group bookwyrm
WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PATH=/venv/bin:$PATH

COPY --from=build /app /app
COPY --from=build /venv /venv
USER bookwyrm
