# Basics

To select everything from a specific database:

``` SQL
SELECT * FROM table_name_goes_here
```

To rename a column, use the `AS` keyword.

```sql
SELECT column_x AS x from table_name_goes_here
```

```sql
SELECT column_x AS `Column X`
       column_y AS `Column Y`
    FROM table_name_goes_here
```

To get unique values from a column in a data set:

```sql
SELECT DISTINCT column_x FROM table_name_goes_here
```
