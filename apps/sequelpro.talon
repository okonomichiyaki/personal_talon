app.bundle: com.sequelpro.SequelPro
app.bundle: com.sequel-ace.sequel-ace
-
paste that: key(cmd-v)
(ron current|run current): key(cmd-r)


select: "SELECT "
star: "*"
from: "FROM "
select star from: "SELECT * FROM "
delete from: "DELETE FROM "
where: "WHERE "
and: " AND "
or: " OR "
as: " AS "
in: " IN "
update: "UPDATE "
set: "SET "
order by: "ORDER BY "
descending: " DESC"
ascending: " ASC"
dot i d: ".id"
is not null: " IS NOT NULL"
is null: " IS NULL"
show create table: "SHOW CREATE TABLE "
group by: "GROUP BY "

not in:
    insert("NOT IN ()")
    key(left)

inner join:
    insert("INNER JOIN  ON ")
    key(left)
    key(left)
    key(left)
    key(left)

left join:
    insert("LEFT JOIN  ON ")
    key(left)
    key(left)
    key(left)
    key(left)
    
limit <number>: "LIMIT {number}"
like:
    " LIKE \"%%\""
    key(left)
    key(left)


 