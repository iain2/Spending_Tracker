from db.run_sql import run_sql

from models.user import User


def save(user):
    sql = "INSERT INTO users (amount, name) VALUES (?,?) RETURNING *"
    values = [user.amount, user.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    user.id = id
    return user


def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row["amount"], row["name"], row["id"])
        users.append(user)
    return users


def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User(result["amount"], result["name"], result["id"])
    return user


def delete_all():
    sql = "DELETE  FROM  users"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM users WHERE id = ?"
    values = [id]
    run_sql(sql, values)


def update(user):
    sql = "UPDATE users SET (amount, name) = (?,?) WHERE id = ?"
    values = [user.amount, user.name, user.id]
    run_sql(sql, values)
