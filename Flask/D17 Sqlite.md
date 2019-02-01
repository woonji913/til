20190201 금요일

# D17 Sqlite

### 1.

```sqlite
sqlite> SELECT * FROM classmate;

id          name        age         address   
----------  ----------  ----------  ----------
1           dkstkdgus   43          대전    
2           신채원   15          서울    
4           박성주   15          제주    
sqlite> 
sqlite> SELECT age FROM classmate;
age       
----------
43        
15        
15        
sqlite> SELECT DISTINCT age FROM classmate;
age       
----------
43        
15        
```

### 2.

```sqlite
sqlite> .headers on
sqlite> .mode column
sqlite> .mode csv
sqlite> .import users.csv users
sqlite> .table
classmate  users    
sqlite> .schema users
CREATE TABLE users(
  "id" TEXT,
  "first_name" TEXT,
  "last_name" TEXT,
  "age" TEXT,
  "country" TEXT,
  "phone" TEXT,
  "balance" TEXT
);
sqlite> DROP TABLE users;
sqlite> .tables
classmate
```

