FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN sudo apt install allure

COPY . .

CMD ["pytest -s -v tests alluredir=alluress"]
