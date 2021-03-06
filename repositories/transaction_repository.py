from db.run_sql import run_sql
import datetime
from models.transaction import Transaction

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository


def save(transaction):
    sql = "INSERT INTO transactions (amount, date, tag_id, merchant_id) VALUES (?,?,?,?) RETURNING *"
    values = [
        transaction.amount,
        transaction.date,
        transaction.tag.id,
        transaction.merchant.id,
    ]
    results = run_sql(sql, values)
    id = results[0]["id"]
    transaction.id = id
    return transaction


def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        tag = tag_repository.select(row["tag_id"])
        merchant = merchant_repository.select(row["merchant_id"])
        date = row["date"]
        split_date = date.split("-")
        date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
        transaction = Transaction(row["amount"], tag, merchant, date, row["id"])
        transactions.append(transaction)
    return transactions


def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = tag_repository.select(result["tag_id"])
        merchant = merchant_repository.select(result["merchant_id"])
        date = result["date"]
        split_date = date.split("-")
        date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
        transaction = Transaction(
            result["amount"], tag, merchant, result["date"], result["id"]
        )
    return transaction


def delete_all():
    sql = "DELETE  FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM transactions WHERE id = ?"
    values = [id]
    run_sql(sql, values)


def update(transaction):
    sql = "UPDATE transactions SET (amount, tag_id, merchant_id) = (?,?,?) WHERE id = ?"
    values = [
        transaction.amount,
        transaction.tag.id,
        transaction.merchant.id,
        transaction.date,
        transaction.id,
    ]
    run_sql(sql, values)


def tags(tag):
    transactions = []

    sql = "SELECT * FROM transactions WHERE tag_id = ?"
    values = [tag.id]
    results = run_sql(sql, values)

    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        date = row["date"]
        split_date = date.split("-")
        date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
        transaction = Transaction(row["amount"], tag, merchant, date, row["id"])
        transactions.append(transaction)

    return transactions


def merchants(merchant):
    transactions = []

    sql = "SELECT * FROM transactions WHERE merchant_id = ?"
    values = [merchant.id]
    results = run_sql(sql, values)

    for row in results:
        tag = tag_repository.select(row["tag_id"])
        date = row["date"]
        split_date = date.split("-")
        date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
        transaction = Transaction(row["amount"], tag, merchant, date, row["id"])
        transactions.append(transaction)

    return transactions
