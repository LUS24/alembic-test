# Using Alembic with FastAPI

## Docs

[Alembic docs](https://alembic.sqlalchemy.org/en/latest/index.html)

## What is it

From the docs:

> Alembic provides for the creation, management, and invocation of _change management_ scripts for a relational database, using SQLAlchemy as the underlying engine.

This means that we can use alembic to keep track of all the changes made to a database. 


## Installation

```bash
pip install alembic
```

Or add it to the requirements.txt

```requirements.txt
...
alembic
```

```bash
pip install -r requirements.txt
```
## Usage

1. In the project directory, create a migration environment ([docs](https://alembic.sqlalchemy.org/en/latest/tutorial.html#creating-an-environment)):
```bash
alembic init alembic
```

2. In the project directory, edit the `alembic.ini` file where it says `sqlalchemy.url`. Add the URL to the database, if you are working in a small app, add this to use SQLite:

```ini
sqlite:///dev.sqlite3
```

We can also set the database URL from an environment variable by updating the `env.py` file, see the docs for more info. ([docs](https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file))

3. Configure automatic migrations ([docs](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#auto-generating-migrations)). Edit the `env.py` file where it says `target_metadata`. It should be a reference SQLAchemy `Base.metadata` object, for example:

```python
from storeapi.database import metadata

...
target_metadata = metadata
...
```

4. Create a migration script ([docs](https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script))
```bash
alembic revision --autogenerate
```

5. Run the migration 
```bash
alembic upgrade head
```

## Interesting features

- Change the default folder name from alembic to other name. For this check the configuration docs ([LINK](https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file)) where it says `script_location`.

- Adding a numeric prefix to the migration versions to keep the files in order. For this check the configuration docs ([LINK](https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file)) where it says `file_template`.

## Debugging

- **Problem:** Tables are created but changes are not reflected in the migration versions
	- Cause: in the file where the metadata is created, the method `create_all` is used causing the tables to be created before alembic checks the db status. As a result alembic does not detect any changes and the version files are empty. 
	- Solution: remove any call like `metadata.create_all()`