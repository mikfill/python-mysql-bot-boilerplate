<html align="center">
<h2>
User table: 
</h2>

```sql
+------------+------------------+------+-----+---------+----------------+
| Field      | Type             | Null | Key | Default | Extra          |
+------------+------------------+------+-----+---------+----------------+
| id         | int unsigned     | NO   | PRI | NULL    | auto_increment |
| user_id    | bigint unsigned  | NO   |     | 0       |                |
| first_name | varchar(64)      | YES  |     |         |                |
| last_name  | varchar(64)      | YES  |     |         |                |
| user_name  | varchar(64)      | NO   |     |         |                |
| level      | tinyint unsigned | NO   |     | 1       |                |
| age        | tinyint unsigned | YES  |     | NULL    |                |
+------------+------------------+------+-----+---------+----------------+
```
<h2>
Sentences table:
</h2>

```sql
+-------+------------------+------+-----+---------+----------------+
| Field | Type             | Null | Key | Default | Extra          |
+-------+------------------+------+-----+---------+----------------+
| id    | int unsigned     | NO   | PRI | NULL    | auto_increment |
| level | tinyint unsigned | NO   |     | NULL    |                |
| text  | text             | NO   |     | NULL    |                |
+-------+------------------+------+-----+---------+----------------+
```
</html>