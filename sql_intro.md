Basic SQL commands.

For testing, you can use, for example, https://sqlite.org/fiddle/index.html


# Create tables and insert data¶

## All Commands (for a quick setup)
```sql
CREATE TABLE IF NOT EXISTS Movie (
  Title VARCHAR(30) NOT NULL,
  Year INTEGER NOT NULL, 
  Length INTEGER,
  Color VARCHAR(5),
  Genre VARCHAR(20),
  StudioName VARCHAR(20),
  ProducerID INTEGER,
  PRIMARY KEY (Title, Year)
);

INSERT INTO Movie VALUES ('Star Wars', 1977, 124, 'TRUE', 'sciFi', 'Fox', 12345)
, ('Star Wars 2', 1980, 124, 'TRUE', 'sciFi', 'Fox', 12345)
, ('Rocky', 1985, 200, 'TRUE', 'action', 'Universal', 12125)
, ('Rambo', 1978, 100, 'TRUE', 'action', 'Universal', 32355)
, ('Galaxy Quest', 1999, 104, 'TRUE', 'comedy', 'DreamWorks', 67890)
, ('Gone with the Wind', 1937, 238, 'TRUE', 'drama', 'Warner Bros', 10000)
, ('Spiel mir das Lied vom Tod', 1968, 165, 'TRUE', 'western', 'Paramount', 10000)
, ('Star Trek', 1979, NULL, 'TRUE', 'sciFi', 'Paramount', 10001);

CREATE TABLE IF NOT EXISTS Actor (
  Name VARCHAR(20) NOT NULL PRIMARY KEY,
  Address VARCHAR(40),
  Gender CHAR,
  Birthdate DATE
);

INSERT INTO Actor VALUES ('Carrie Fisher', 'Hollywood', 'F', '1956-10-21')
, ('Mark Hamill', '456 Oak Rd., Brentwood', 'M', '1951-09-25')
, ('Harrison Ford', 'Beverly Hills', 'M', '1942-07-13')
, ('Angelina Jolie', '123 Maple St., Hollywood', 'F', '1975-06-04')
, ('Brad Pitt', '123 Maple St., Hollywood', 'M', '1963-12-18');

CREATE TABLE IF NOT EXISTS MovieCast (
  MovieTitle VARCHAR(30) NOT NULL,
  MovieYear INTEGER NOT NULL,
  ActorName VARCHAR(20) NOT NULL,
  PRIMARY KEY (MovieTitle, MovieYear, ActorName)
);

INSERT INTO MovieCast VALUES ('Star Wars', 1977, 'Carrie Fisher')
, ('Star Wars', 1977, 'Harrison Ford')
, ('Star Wars', 1977, 'Mark Hamill')
, ('Star Wars 2', 1980, 'Carrie Fisher')
, ('Heroes', 1977, 'Harrison Ford');

CREATE TABLE IF NOT EXISTS Producer (
  Name VARCHAR(20),
  Address VARCHAR(40),
  Id INTEGER NOT NULL PRIMARY KEY,
  Salary INTEGER
);

INSERT INTO Producer VALUES ('Stephen Spielberg', 'Hollywood', 9999, 1000000)
, ('Gary Kurtz', NULL, 12345, NULL)
, ('Brad Pitt', '123 Maple St., Hollywood', 10002, NULL);

CREATE TABLE IF NOT EXISTS Studio (
  Name VARCHAR(20) NOT NULL PRIMARY KEY,
  Address VARCHAR(20),
  PresidentId INTEGER
);

INSERT INTO Studio VALUES ('Fox', 'Los Angeles', 7777)
, ('Universal', 'Universal City', 8888)
, ('DreamWorks', 'Universal City', 9999);
```


## Individual Commands

```sql
CREATE TABLE IF NOT EXISTS Movie (
  Title VARCHAR(30) NOT NULL,
  Year INTEGER NOT NULL, 
  Length INTEGER,
  Color VARCHAR(5),
  Genre VARCHAR(20),
  StudioName VARCHAR(20),
  ProducerID INTEGER,
  PRIMARY KEY (Title, Year)
);
```

```sql
INSERT INTO Movie VALUES ('Star Wars', 1977, 124, 'TRUE', 'sciFi', 'Fox', 12345)
, ('Star Wars 2', 1980, 124, 'TRUE', 'sciFi', 'Fox', 12345)
, ('Rocky', 1985, 200, 'TRUE', 'action', 'Universal', 12125)
, ('Rambo', 1978, 100, 'TRUE', 'action', 'Universal', 32355)
, ('Galaxy Quest', 1999, 104, 'TRUE', 'comedy', 'DreamWorks', 67890)
, ('Gone with the Wind', 1937, 238, 'TRUE', 'drama', 'Warner Bros', 10000)
, ('Spiel mir das Lied vom Tod', 1968, 165, 'TRUE', 'western', 'Paramount', 10000)
, ('Star Trek', 1979, NULL, 'TRUE', 'sciFi', 'Paramount', 10001);
```

```sql
CREATE TABLE IF NOT EXISTS Actor (
  Name VARCHAR(20) NOT NULL PRIMARY KEY,
  Address VARCHAR(40),
  Gender CHAR,
  Birthdate DATE
);
```

```sql
INSERT INTO Actor VALUES ('Carrie Fisher', 'Hollywood', 'F', '1956-10-21')
, ('Mark Hamill', '456 Oak Rd., Brentwood', 'M', '1951-09-25')
, ('Harrison Ford', 'Beverly Hills', 'M', '1942-07-13')
, ('Angelina Jolie', '123 Maple St., Hollywood', 'F', '1975-06-04')
, ('Brad Pitt', '123 Maple St., Hollywood', 'M', '1963-12-18');
```

```sql
CREATE TABLE IF NOT EXISTS MovieCast (
  MovieTitle VARCHAR(30) NOT NULL,
  MovieYear INTEGER NOT NULL,
  ActorName VARCHAR(20) NOT NULL,
  PRIMARY KEY (MovieTitle, MovieYear, ActorName)
);
```

```sql
INSERT INTO MovieCast VALUES ('Star Wars', 1977, 'Carrie Fisher')
, ('Star Wars', 1977, 'Harrison Ford')
, ('Star Wars', 1977, 'Mark Hamill')
, ('Star Wars 2', 1980, 'Carrie Fisher')
, ('Heroes', 1977, 'Harrison Ford');
```

```sql
CREATE TABLE IF NOT EXISTS Producer (
  Name VARCHAR(20),
  Address VARCHAR(40),
  Id INTEGER NOT NULL PRIMARY KEY,
  Salary INTEGER
);
```

```sql
INSERT INTO Producer VALUES ('Stephen Spielberg', 'Hollywood', 9999, 1000000)
, ('Gary Kurtz', NULL, 12345, NULL)
, ('Brad Pitt', '123 Maple St., Hollywood', 10002, NULL);
```

```sql
CREATE TABLE IF NOT EXISTS Studio (
  Name VARCHAR(20) NOT NULL PRIMARY KEY,
  Address VARCHAR(20),
  PresidentId INTEGER
);
```

```sql
INSERT INTO Studio VALUES ('Fox', 'Los Angeles', 7777)
, ('Universal', 'Universal City', 8888)
, ('DreamWorks', 'Universal City', 9999);
```

# Basic SQL Queries

## 1. Basic structure

All SQL queries are structured as follows:
```sql
SELECT <attribute_list>
FROM <schema_list>
WHERE <condition_list>;
```

`SELECT <attribute list>`
    
- Projection of the specified attributes, separated by commas  
- Select all attributes using the wildcard `*`

`FROM <schema list>`
- Relation(s) on which the projection is based

`WHERE <condition list>`
- Selection of tuples based on attribute conditions

### All movies of the database:

```sql
SELECT *
FROM Movie;
```

### The tile and year of all movies from Fox:
```sql
SELECT Title, Year
FROM Movie
WHERE StudioName = 'Fox';
```

### All movies from Fox which where created in 1980:
```sql
SELECT *
FROM Movie
WHERE StudioName = 'Fox' AND Year = 1980;
```

## 1.1 Projection: SELECT clause

#### 1.1.1 Projection of specific attributes
```sql
SELECT Title, Year, Genre
FROM Movie;
```
#### 1.1.2 Select all attributes
```sql
SELECT *
FROM Movie;
```
#### 1.1.3 Rename attributes
```sql
SELECT attrName_old AS attrName_new
```
```sql
SELECT Title AS Name, Year AS Time
FROM Movie;
```
Defined alias can be used in remaining request
#### 1.1.4 Expressions
```sql
SELECT Title, Length*0.016667 AS Hours
FROM Movie;
```

## 1.2 Selection: WHERE clause

- Selection of output tuples
- Comparison operators
  - Logical: =, <>, <, >, <=, >=
  - Range: BETWEEN x AND y
  - Containment: IN (a,b,c ,...)
- Result is boolean TRUE or FALSE
  - Multiple clauses can be linked with AND, OR or NOT
  - Brackets are allowed
    ```sql
    SELECT Title
    FROM Movie
    WHERE (Year > 1980 OR Length > 200)
        AND StudioName = 'Universal';
    ```
- Comparisons can be made between constants, attributes and arithmetic expressions

### Examples:

```sql
SELECT * FROM Movie
WHERE Year IN (1980, 1990, 2000);
```

```sql
SELECT * FROM Movie
WHERE Year BETWEEN 1980 AND 2000;
```

## 1.3 Data Types
### 1.3.1 Strings
- Fixed length array, variable length strings, constants
#### Comparison Operators for Strings: <, >, <=, >=, <>
- Lexicographic comparison, e.g. ’bar’ < ’bargain’
- Case sensitive, e.g. ’Hello’ <> ’hello’
- Case sensitive, e.g. ’Hello’ <> ’hello’
- Example: All occurrences of sciFi, scifi, SciFi

```sql
SELECT * FROM Movie
WHERE lower(Genre) = 'scifi' ;
```

### String Concatenation

```sql
SELECT Title || ', ' || Year AS MovieInfo FROM Movie
WHERE Year BETWEEN 1980 AND 2000;
```

Alternative syntax using the concat() function

```sql
SELECT concat(Title, ', ', Year) AS MovieInfo FROM Movie
WHERE Year BETWEEN 1980 AND 2000;
```

### Pattern Matching Using LIKE
- Pattern consists of:
  - Characters of the alphabet
  - '%' corresponds to any sequence of 0 or more characters
  - ' ' corresponds to exactly one character of the alphabet
- Example: All movies that start with 'S'

```sql
SELECT Title
FROM Movie
WHERE Title LIKE 'S%';
```

## 1.3.2 Date and Time
Supported functionality (e.g., data types, time zone support, functions) depends on specific database system
(https://sqlite.org/lang_datefunc.html)

```sql
SELECT datetime('now', 'localtime')
FROM Movie
LIMIT 1;
```

## 1.4 Unknown Values: NULL
- Database systems can store and evaluate unknown values
  (can be used for unknown or optional values)
- Unspecified attribute values NULL are evaluated to UNKNOWN in the
WHERE clause
- If the WHERE-clause returns the value **UNKNOWN**, the corresponding tuples are **not in the result**


```sql
CREATE Table IF NOT EXISTS Person (
    Name VARCHAR(40),
    BirthYear INTEGER
);
```

```sql
INSERT INTO Person VALUES('Sarah', 1986)
, ('Larry', NULL);
```

```sql
SELECT *
FROM Person
WHERE BirthYear >= 1986 OR BirthYear < 1986;
```

### Truth table for three-valued logic with UNKNOWN

| x       | y       | x OR y  | x AND y   |
|---------|---------|---------|-----------|
| TRUE    | TRUE    | TRUE    | TRUE      |
| TRUE    | UNKNOWN | TRUE    | UNKNOWN   |
| TRUE    | FALSE   | TRUE    | FALSE     |
| UNKNOWN | TRUE    | TRUE    | UNKNOWN   |
| UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN   |
| UNKNOWN | FALSE   | UNKNOWN | FALSE     |
| FALSE   | TRUE    | TRUE    | FALSE     |
| FALSE   | UNKNOWN | UNKNOWN | FALSE     |
| FALSE   | FALSE   | FALSE   | FALSE     |


## Querying NULL Values: IS NULL and IS NOT NULL

```sql
SELECT *
FROM Person
WHERE BirthYear IS NULL;
```

## 1.5 Sorting: ORDER BY

- ORDER BY-clause at the end of the query
  - ORDER BY <attr list> [DESC|ASC]
  - ASC (ascending) is default value
- Examples:
  - ```sql
      SELECT * FROM Movie
      ORDER BY Length , Title;
    ```
  - ```sql
      SELECT * FROM Movie
      ORDER BY Length DESC, Title ASC;
    ```

```sql
SELECT * FROM Movie
ORDER BY Length DESC, Title ASC;
```

## 1.6 Duplicate Elimination: DISTINCT
- SQL is returns multisets as default
- Duplicates are caused by:
  - Inserting duplicates into the base relation
  - Changes in tuples in the base relation
  - Projection in queries
  - Subqueries (UNION)
- Duplicate elimination by SELECT DISTINCT <attr list>
- Example: Return all studio names contained in the Movies table exactly once:
```sql
SELECT DISTINCT(StudioName)
FROM Movie;
```

## 1.7 Aggregations
- Operators for aggregating attributes or attribute values are:
  - COUNT(<attr>) counts the number of selected tuples
  - SUM(<attr>) sums up the numerical values of attr
  - AVG(<attr>) calculates the average of the numeric attribute attr
  - MIN(<attr>), MAX(<attr>) returns the minimum/maximum value
- Combination with DISTINCT
  - COUNT(DISTINCT Year)
  - AVG(DISTINCT Year)

```sql
SELECT COUNT(DISTINCT Year)
FROM Movie;
```
- COUNT(*) includes tuples with NULL values
- COUNT(<attr>) does not counts NULL values

```sql
DROP TABLE IF EXISTS Person;
```

```sql
CREATE Table Person (
    Name VARCHAR(40),
    BirthYear INTEGER
);
```

```sql
INSERT INTO Person VALUES('Sarah', 1986)
, ('Larry', NULL);
```

```sql
SELECT COUNT(*)
FROM Person;
```

```sql
SELECT COUNT(BirthYear)
FROM Person;
```


## 1.8 Grouping: GROUP BY
- The **GROUP BY**-clause groups attribute values and follows the **FROM**- (and **WHERE**-clause, if any exists) in the query

```sql
SELECT StudioName, COUNT(*) FROM Movie
GROUP BY StudioName
ORDER BY COUNT(*) DESC;
```

Note: **SELECT**-clause in queries with **GROUP BY** must only contain attributes that are either:
- grouped
- or aggregated
SQLite is an exception

```sql
SELECT COUNT(*) FROM Movie
GROUP BY StudioName
ORDER BY COUNT(*) DESC;
```

⚠️ For the next query, SQLite will NOT throw an error. Instead, it uses a non-standard rule:
- You may select columns that are not in the GROUP BY
- SQLite will then return an arbitrary value for those columns — usually from one of the rows in the group, but it is not guaranteed which one

The same query will fail in other systems.

```sql
SELECT Genre, Year, COUNT(*) FROM Movie
GROUP BY StudioName
ORDER BY COUNT(*) DESC;
```

## Selection of groups: HAVING
Restricting the result set after grouping with the HAVING-clause
```sql
SELECT ...
FROM ...
[WHERE ...]
GROUP BY <attr list >
HAVING <cond>;
```

```sql
SELECT StudioName, COUNT(*) FROM Movie
GROUP BY StudioName
HAVING COUNT(*) > 1;
```

# 2 Database Modifications
## 2.1 Insertion: INSERT
We can insert complete tuples or specify only selected attributes.
```sql
INSERT INTO Actor (Name, Address, Gender, Birthdate)
VALUES ('Tom Hanks', 'Los Angeles', 'M', '1956-07-09');
```

```sql
INSERT INTO Actor (Name, Gender, Birthdate)
VALUES ('Heike Makatsch', 'F', '1971-08-13');
```

```sql
SELECT * FROM Actor;
```

## 2.2 Deletion: DELETE
Deletes tuples that satisfy a condition.

```sql
DELETE FROM Actor
WHERE Name = 'Tom Hanks';
```

```sql
SELECT * FROM Actor;
```

⚠️ Without a WHERE clause, ALL rows are deleted.

```sql
DELETE FROM Actor;
```

## 2.3 Updates: UPDATE
Update values of existing tuples.

```sql
UPDATE Producer
SET Salary = 2000000
WHERE Name = 'Gary Kurtz';
```

```sql
SELECT * FROM Producer;
```

# 3 Querying Multiple Tables
## 3.1 Cartesian Product
The Cartesian product pairs **every row of one table with every row of another**.
It is the basis for joins.
```sql
SELECT *
FROM Movie, Studio;
```

## 3.2 JOIN

Joins combine tuples from different tables based on matching attributes.

### Example: Movies and their Studios
```sql
SELECT Movie.Title, Studio.Name, Studio.Address
FROM Movie
JOIN Studio ON Movie.StudioName = Studio.Name;
```
Alternative syntax with **INNER**
```sql
SELECT Movie.Title, Studio.Name, Studio.Address
FROM Movie
INNER JOIN Studio ON Movie.StudioName = Studio.Name;
```
Alternative, less convenient approach with JOIN condition in **WHERE** clause:
```sql
SELECT Movie.Title, Studio.Name, Studio.Address
FROM Movie, Studio
WHERE Movie.StudioName = Studio.Name;
```

### 3.2.1 JOIN with three tables (Actors in each Movie)

```sql
SELECT Movie.Title, Actor.Name
FROM Movie
JOIN MovieCast ON Movie.Title = MovieCast.MovieTitle
             AND Movie.Year = MovieCast.MovieYear
JOIN Actor ON MovieCast.ActorName = Actor.Name;
```

### 3.2.2 OUTER JOINs
Return **all movies**, even those with **no cast members**.

```sql
SELECT Movie.Title, MovieCast.ActorName
FROM Movie
LEFT JOIN MovieCast
ON Movie.Title = MovieCast.MovieTitle AND Movie.Year = MovieCast.MovieYear;
```

Return all cast members, even for movies without infos.

```sql
SELECT Movie.Title, MovieCast.ActorName
FROM Movie
RIGHT JOIN MovieCast
ON Movie.Title = MovieCast.MovieTitle AND Movie.Year = MovieCast.MovieYear;
```

Return all movies and all cast members.
    
```sql
SELECT Movie.Title, MovieCast.ActorName
FROM Movie
FULL JOIN MovieCast
ON Movie.Title = MovieCast.MovieTitle AND Movie.Year = MovieCast.MovieYear;
```

### 3.2.3 Natural JOIN
**Implicit** join condition: Matching attributes

```sql
SELECT *
FROM Actor
NATURAL JOIN Producer;
```

# 4 Set Operations
SQL supports three main set operations:

| Operation | Meaning |
|-----------|---------|
| UNION     | Set union |
| INTERSECT | Set intersection |
| EXCEPT    | Set difference |

All participating queries must have:
- Same number of attributes
- Same compatible data types

The operations use set semantic, i.e., they remove duplicates.
To preserve duplicates, we can use the corresponding operations **UNION ALL**, **INTERSECT ALL**, and **EXCEPT ALL**

### 4.1 UNION
All actors and producers.
**UNION** removes duplicates

```sql
SELECT Name FROM Actor
UNION
SELECT Name FROM Producer;
```

**UNION ALL** preserves DUPLICATES
```sql
SELECT Name FROM Actor
UNION ALL
SELECT Name FROM Producer;
```

### 4.2 Intersect
All persons that are actors and producers.

```sql
SELECT Name FROM Actor
INTERSECT
SELECT Name FROM Producer;
```

### 4.3 Difference
All actors that are not producers.

```sql
SELECT Name FROM Actor
EXCEPT
SELECT Name FROM Producer;
```
