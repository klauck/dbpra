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
