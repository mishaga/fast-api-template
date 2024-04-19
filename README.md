# FastAPI template project

Pull this repo to quickly start a new project with FastAPI and JSON Web Token (JWT) authorisation


## Run server locally (in PyCharm)

1. Create `.env` file:
   ```
   ENVIRONMENT=local
   DEBUG=true

   SENTRY_DSN=
   JWT_SECRET=...replace.secret...

   POSTGRES_HOST=127.0.0.1
   POSTGRES_DATABASE=database_name
   POSTGRES_USER=username
   POSTGRES_PASSWORD=...replace.password...
   ```
2. Run database server
   * In console: run `make dev`
3. Create environment:
   * In console: run `poetry shell`
   * In console: run `poetry install`
4. Add interpreter:
   * Add new interpreter
   * Local interpreter
   * Poetry interpreter
   * Choose created environment
5. Add configuration for API:
   * Open "Edit configurations"
   * Add new configuration → FastAPI
   * Fill "Application file": full path to `api/app.py` file
   * Fill "Application name": `app`
   * Fill "Uvicorn options": `--host=127.0.0.1 --reload --no-server-header`
   * Fill "Working directory": full path to project folder


## Run tests locally (in PyCharm)

1. Enter database server
   * In console: run `make postgres`
2. Create database for tests  
   In PostgreSQL console run:  
   ```sql
   CREATE DATABASE database_tests OWNER username;
   ```
   Close console
3. Open "Edit configurations"
4. Open "Edit configuration templates"
5. Choose "Python tests" → "pytest"
6. Fill "Working directory": full path to project folder


## Make and apply migrations (locally)

1. Open console
2. Enter poetry shell (if not in already):
   ```bash
   poetry shell
   ```
3. Create migration:
   ```bash
   alembic revision --autogenerate -m "<migration_name>" --rev-id "<revision_id>"
   ```
   For example:
   ```bash
   alembic revision --autogenerate -m "create_event_table" --rev-id "02"
   ```
4. Apply migration(s):
   ```bash
   alembic upgrade head
   ```
   Or upgrade to next revision:
   ```bash
   alembic upgrade +1
   ```
   Or look at SQL code:
   ```bash
   alembic upgrade --sql
   ```
5. Downgrade (if needed):
   ```bash
   alembic downgrade base
   ```
   Or downgrade to previous revision:
   ```bash
   alembic downgrade -1
   ```


## Management commands

In order to tun a management command you need to define `PYTHONPATH` variable first  
So here are some examples:

Example for fish shell:
```fish
PYTHONPATH=(pwd) python management_commands/create_user.py --email=me@mysite.com --first_name=me --last_name=myself
PYTHONPATH=(pwd) python management_commands/generate_token.py --user_id=1
```

Example for bash shell:
```bash
PYTHONPATH=$(pwd) python management_commands/create_user.py --email=me@mysite.com --first_name=me --last_name=myself
PYTHONPATH=$(pwd) python management_commands/generate_token.py --user_id=1
```
