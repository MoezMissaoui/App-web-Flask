web: gunicorn fbapp:app



initdb: FLASK_APP=run.py flask init-db
initdb1: set FLASK_APP=run.py
initdb2: flask init-db

test: flask test