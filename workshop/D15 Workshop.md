# D15 Workshop

1. 

```sql
CREATE TABLE bands (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT
debut INTEGER
);
   
INSERT INTO bands(name, debut)
VALUES('Queen', 1973),('Coldplay', 1998),('MCR', 2001);
```

2.

```sql
SELECT id, name FROM bands;
```

3.

```sql
SELECT name FROM bands WHERE debut<2000;
```

