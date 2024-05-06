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

## Примеры API эндпоинтов:
* ```http://127.0.0.1:8080/healthcheck```  GET-запрос – возвращает пустой JSON.
 ``` json
{}
```

* ```http://127.0.0.1:8080/hash```  POST-запрос – вычисляет хэш строки по алгоритму SHA256 и возвращает его в JSON ответе.
 ``` json
{
    "string": "My name is Pavel!"
}
```
 ``` json
{
{
    "hash_string": "8bb80ce11355401f5f45e39717fd00139c5403282b22b53cae595517ff42fd82"
}
}
```

* Примеры ошибок:
``` json
{
    "validated_errors": "Invalid JSON format"
}
```

```json
{
    "validated_errors": "Field string is required"
}
```
