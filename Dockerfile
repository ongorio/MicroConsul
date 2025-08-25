FROM python:3.11-slim AS builder

RUN mkdir /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libffi-dev \
    libssl-dev \
    firebird-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim AS runner

RUN apt-get update && apt-get install -y \
    libfbclient2 \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -r ongorio && \
    mkdir /app && \
    chown -R ongorio:ongorio /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/ /usr/local/bin/

WORKDIR /app

COPY --chown=ongorio:ongorio . .

WORKDIR /app/src

USER ongorio
