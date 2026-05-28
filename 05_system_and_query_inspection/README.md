# SQLite Examples

This folder contains an example SQLite database file that can be opened and explored using tools such as DB Browser for SQLite (https://sqlitebrowser.org/).

The database can be used to inspect:
- the schema (tables, attributes, and data types)
- existing indexes
- existing views
- database settings and configuration settings (enabled features, logging, page size, ...)

## Manual Setup

The database was populated using the following commands: https://github.com/klauck/dbpra/blob/main/sql_intro.md#all-commands-for-a-quick-setup

The index and view were created with these SQL statements:

```sql
CREATE INDEX index_actor_birthdate ON "Actor" (
   "Birthdate" ASC
);
```

```sql
CREATE VIEW SciFiMovie AS
  SELECT Title, Year
  FROM Movie
  WHERE Genre = 'sciFi';
```


# PostgreSQL Examples

## Schema Inspection

1. Using PostgreSQL-specific Tables/Views

```sql
SELECT schemaname, tablename
FROM pg_catalog.pg_tables
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY schemaname, tablename;
```

2. Using The Information Schema (defined by the SQL standard)

```sql
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
    AND table_schema NOT IN ('pg_catalog', 'information_schema')
ORDER BY table_schema, table_name;
```





## Query Inspection

1. Query Planning
   Shows:
   - Planned execution plan/tree
   - Estimated cardinalities
   - Estimated costs (internal metric)

```sql
EXPLAIN SELECT *
FROM orders
WHERE o_totalprice < 1000
ORDER BY o_orderkey;
```

```sql
EXPLAIN SELECT *
FROM orders
WHERE o_orderkey = 42;
```

2. Query Execution
   Shows:
   - Actual cardinalities
   - Execution time
   - Buffer and memory usage


```sql
EXPLAIN (ANALYZE, BUFFERS) SELECT *
FROM orders
WHERE o_totalprice < 1000
ORDER BY o_orderkey;
```
