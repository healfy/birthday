python manage.py makemigrations
python manage.py migrate
echo "yes" | python manage.py collectstatic
python manage.py runserver 0.0.0.0:8000
# вот эти команды
# первые две делают миграции в базе, они впринципе не нужны
# третья можно без
