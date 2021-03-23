#Как запустить

сначала запустим бд
Нужно будет скачать [Docker](https://www.docker.com)
```
docker-compose up
```
дожидаемся запуска бд

так же будут нужны следующие пакеты
1. mysql-server
2.  mysql-client
3. libmysqlclient15-dev

установите их любым пакетным менеджером
   
в другой консоли открываем снова рут проекта
заходим в виртуальное окружение
и запускаем приложение
```
source /venv/bin/activate
export FLASK_APP=app.py
flask db upgrade
flask run
```