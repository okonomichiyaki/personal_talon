os: mac
and app.bundle: com.sequelpro.SequelPro
-
paste that: key(cmd-v)
(ron current|run current): key(cmd-r)


select: "SELECT "
star: "*"
from: "FROM "
select star from: "SELECT * FROM "
where: "WHERE "
and: "AND "

order by: "ORDER BY "
descending: " DESC"
ascending: " ASC"
dot i d: ".id"
is not null: " IS NOT NULL"
is null: " IS NULL"
inner join:
    insert("INNER JOIN  ON ")
    key(left)
    key(left)
    key(left)
    key(left)

limit <number>: "LIMIT {number}"
like:
    " LIKE \"%%\""
    key(left)
    key(left)


 