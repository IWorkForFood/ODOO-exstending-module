# Пример установки в чистый инстанс

добавляем в корневую папку данную

Запускаем базу данных:

```
docker run -d --name pg-odoo \
  -e POSTGRES_USER=odoo \
  -e POSTGRES_PASSWORD=mypass \
  -e POSTGRES_DB=mydb \
  -p 5433:5432 \
  postgres:16
```

запускаем odoo:

```
python3 odoo-bin --addons-path=addons,custom_addons -d mydb --db_host=localhost --db_port=5432 --db_user=odoo --db_password=mypass -u odoo_bezizvestnyi
```
