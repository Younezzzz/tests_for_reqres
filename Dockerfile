FROM python:3.10-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends wget unzip openjdk-11-jre-headless \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN wget -qO- https://github.com/allure-framework/allure2/releases/latest/download/allure-2.21.0.zip > /tmp/allure.zip \
    && unzip /tmp/allure.zip -d /opt/ \
    && rm /tmp/allure.zip

ENV PATH="/opt/allure-2.21.0/bin:${PATH}"

COPY . .

CMD pytest tests --alluredir=allure-results && allure generate allure-results --clean -o allure-report
