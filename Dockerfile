jobs:
  run-tests:
    runs-on: ubuntu-latest

    container:
      image: python:3.11  # Docker-образ, внутри которого будет выполняться job
      options: --user root  # необязательно, но полезно для установки пакетов

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run all tests
        run: |
          pytest tests/ --maxfail=1 --disable-warnings -v
