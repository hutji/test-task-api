# test-task-api
HTTP API включающий в себя базовый эндпоинт для проверки состояния сервера и эндпоинт для хеширования строк с использованием алгоритма SHA256.

## Установка зависимостей для локального разворачивания<a id="installation"></a>

1. Склонируйте репозиторий:

  ```
    git clone git@github.com:hutji/test-task-api.git
  ```
2. Активируйте виртуальное окружение:
  ```
    python -m venv venv
    source venv/bin/activate
  ```
3. Установите зависимости:
  ```
    pip install -r requirements.txt
  ```

## Запуск <a id="start"></a>

Запустите локально
  ```
    cd backend
    python server.py
  ```


Запустите контейнеры с проектом следующей командой:
  ```
    docker build -t test-task-api .
    docker run -p 8080:8080 test-task-api
  ```

##  Тестирование <a id="tests"></a>

Запустите тесты командой:
  ```
    pytest
  ```
