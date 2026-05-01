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



# Constraints

```sql
CREATE TABLE customer(
    id BIGINT PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%'),
    phone TEXT);

CREATE TABLE "order"(
    id BIGINT PRIMARY KEY,
    date TIMESTAMP WITH TIME ZONE NOT NULL,
    price DECIMAL(20,2) NOT NULL,
    customer_id BIGINTREFERENCES customer(id) ON DELETE CASCADE);
```

```sql
INSERT INTO customer VALUES(1, 'Sarah', 'TU Berlin', 'sarah@tu-berlin.de', NULL);
```

```sql
INSERT INTO "order" VALUES(1, CURRENT_TIMESTAMP, '3.14', 1);
```

```sql
DELETE FROM customer WHERE id=1;
```


# Table Expressions

```sql
CREATE TABLE customer(
    id BIGINT PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%'),
    phone TEXT);

CREATE TABLE "order"(
    id BIGINT PRIMARY KEY,
    date TIMESTAMP WITH TIME ZONE NOT NULL,
    price DECIMAL(20,2) NOT NULL,
    customer_id BIGINTREFERENCES customer(id) ON DELETE CASCADE);

INSERT INTO customer VALUES(1, 'Sarah', 'TU Berlin', 'sarah@tu-berlin.de', NULL);
INSERT INTO customer VALUES(2, 'Jin', 'HPI', 'jin@hpi.de', NULL);
INSERT INTO customer VALUES(3, 'Fynn', 'Finland', 'fynn@finland.fi', NULL);
INSERT INTO customer VALUES(4, 'Mika', 'BTU', 'mika@btu.de', NULL);

INSERT INTO "order" VALUES(1, CURRENT_TIMESTAMP, '3.14', 1);
INSERT INTO "order" VALUES(2, CURRENT_TIMESTAMP, '41.00', 1);
INSERT INTO "order" VALUES(3, CURRENT_TIMESTAMP, '42.14', 2);
INSERT INTO "order" VALUES(4, CURRENT_TIMESTAMP, '0.81', 3);
INSERT INTO "order" VALUES(5, CURRENT_TIMESTAMP, '17.11', 3);
INSERT INTO "order" VALUES(5, CURRENT_TIMESTAMP, '23.00', 3);
```


### Finds the customer(s) who have spent the most money in total across all their orders, and then returns all orders belonging to that customer (or those customers).


## Subqueries

```sql
SELECT *
FROM   customer
       JOIN "order"
       ON customer.id = "order".customer_id
WHERE  customer.id = (SELECT customer_id
                      FROM   (SELECT   customer.id AS customer_id,
                                       Sum(price)  AS order_volumne
                              FROM     customer
                                       JOIN "order"
                                       ON customer.id = "order".customer_id
                              GROUP BY customer.id) customer_order_volumne
                      WHERE  order_volumne = (SELECT Max(order_volumne)
                                              FROM   (SELECT   customer.id AS customer_id,
                                                               Sum(price)  AS order_volumne
                                                      FROM     customer
                                                               JOIN "order"
                                                               ON customer.id = "order".customer_id
                                                      GROUP BY customer.id)));

```

## Views

```sql
CREATE VIEW customer_order_volume
     AS (SELECT   customer.id AS customer_id,
                  Sum(price)  AS order_volume
         FROM     customer
                  JOIN "order"
                  ON customer.id = "order".customer_id
         GROUP BY customer.id);

  SELECT *
  FROM   customer
         JOIN "order"
         ON customer.id = "order".customer_id
  WHERE  customer.id = (SELECT customer_id
                        FROM   customer_order_volume
                        WHERE  order_volume = (SELECT Max(order_volume)
                                               FROM   customer_order_volume));

```


## Common Table Expressions (CTEs)

```sql
WITH customer_order_volume
     AS (SELECT   customer.id AS customer_id,
                  Sum(price)  AS order_volume
         FROM     customer
                  JOIN "order"
                  ON customer.id = "order".customer_id
         GROUP BY customer.id) 
  SELECT *
  FROM   customer
         JOIN "order"
         ON customer.id = "order".customer_id
  WHERE  customer.id = (SELECT customer_id
                        FROM   customer_order_volume
                        WHERE  order_volume = (SELECT Max(order_volume)
                                               FROM   customer_order_volume));
```



