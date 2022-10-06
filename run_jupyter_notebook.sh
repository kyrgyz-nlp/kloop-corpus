source env/bin/activate || true
conda deactivate || true
python manage.py shell_plus --notebook
