import psycopg2 as pg2


conn = pg2.connect(
    database="dvdrental",
    user="postgres",
    password="2552",  # no reasons to bother with venv
)

# Setting cursor to execute queries.
cursor = conn.cursor()
cursor.execute(
    "SELECT * "
    "FROM payment"
)
# Returns tuples with data from rows all/one/many
# print(cursor.fetchall())
# print(cursor.fetchone())
# print(cursor.fetchmany(10))
# data = cursor.fetchmany(10)
# print(data[5:])

# Already been working with SQLAlchemy, and it's essentially the same, but outdated.
# Last updates in 2015. So it's better to practice with pure SQLQuery methods in SQLAlchemy later.


