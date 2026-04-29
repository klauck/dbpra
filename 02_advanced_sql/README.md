# Python SQLite and PostgreSQL Examples

This folder contains examples how to access SQLite and PostgreSQL database systems using Python.

**1. Python SQLite example**

SQLite is included in newer Python installations, so no additional setup is required. You can run the example directly:

```
python sqlite_example.py
```


**2. Python PostgreSQL example**

To run the PostgreSQL example, you need:

- A running PostgreSQL instance
- The Python library `psycopg2`

For PostgreSQL setup instructions, see: [PostgreSQL Setup](https://github.com/klauck/dbpra/new/main/02_advanced_sql#postgresql-setup).

For installing `psycopg2`, you can optionally create and activate a virtual environment first:

```
python3 -m venv .env/dbrpa
source env/dbrpa/bin/activate  
```

For installing psycopg2, run:

```
pip install psycopg2
```

After setting up PostgreSQL and installing psycopg2, run:

```
python postgresql_example.py
```



## PostgreSQL Setup

You can run the examples on an existing PostgreSQL installation.
However, you, then, need to adapt the connection details.

### Docker Setup

Alternatively, you can run PostgreSQL using Docker.


**1. Create and Start the Container**
   
```
docker run --name demo_postgres \
-v .:/root \
-e POSTGRES_USER=postgres \
-e POSTGRES_HOST_AUTH_METHOD=trust \
-e POSTGRES_DB=demo_db_internals \
-p 5432:5432 \
-d postgres:17
```

**2. Connect to PostgreSQL**
   To connect using `psql`:

```
docker exec -it demo_postgres psql -U postgres -d demo_db_internals
```

**3. Manage the Container**
   - Stop the container:

```
docker stop demo_postgres
```

- Start the container again:

```
docker start demo_postgres
```

**4. Open the Container Shell**

Open a shell in the container, e.g., for inspecting the created files by PostgreSQL

```
docker exec -it demo_postgres bash
```
