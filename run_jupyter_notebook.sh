pipenv shell || true
conda deactivate || true
DJANGO_ALLOW_ASYNC_UNSAFE=true && python manage.py shell_plus --notebook
