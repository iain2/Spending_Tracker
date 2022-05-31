from db.run_sql import run_sql

from models.merchant import Merchant


def save(merchant):
    sql = "INSERT INTO merchants (name, active) VALUES (?,?) RETURNING *"
    values = [merchant.name, merchant.active]
    results = run_sql(sql, values)
    id = results[0]["id"]
    merchant.id = id
    return merchant


def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row["name"], bool(row["active"]), row["id"])
        merchants.append(merchant)
    return merchants


def select(id):
    tag = None
    sql = "SELECT * FROM merchants WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result["name"], bool(result["active"]), result["id"])
    return merchant


def delete_all():
    sql = "DELETE  FROM merchants"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM merchants WHERE id = ?"
    values = [id]
    run_sql(sql, values)


def update(merchant):
    sql = "UPDATE merchants SET (name, active) = (?,?) WHERE id = ?"
    values = [merchant.name, merchant.active, merchant.id]
    run_sql(sql, values)
