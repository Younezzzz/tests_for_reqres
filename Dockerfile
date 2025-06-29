FROM python:3.10-slim

WORKDIR /app

RUN echo "deb http://deb.debian.org/debian bullseye main contrib non-free" > /etc/apt/sources.list \
    && echo "deb http://security.debian.org/debian-security bullseye-security main contrib non-free" >> /etc/apt/sources.list \
    && echo "deb http://deb.debian.org/debian bullseye-updates main contrib non-free" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends wget unzip openjdk-11-jre-headless \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN wget -qO- https://github.com/allure-framework/allure2/releases/latest/download/allure-2.34.1.zip > /tmp/allure.zip \
    && unzip /tmp/allure.zip -d /opt/ \
    && rm /tmp/allure.zip

ENV PATH="/opt/allure-2.34.1/bin:${PATH}"

COPY . .

CMD pytest tests --alluredir=allure-results && allure generate allure-results --clean -o allure-report
