s:
	uv run python manage.py runserver
m:
	uv run python manage.py makemigrations
	uv run python manage.py migrate
sh:
	uv run python manage.py shell