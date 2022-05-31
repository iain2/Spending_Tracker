from flask import Flask, redirect, render_template, Blueprint, request
from models.transaction import *
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository
import datetime

transaction_blueprint = Blueprint("Transactions", __name__)


@transaction_blueprint.route("/transactions")
def transaction():
    transactions = transaction_repository.select_all()
    transactions.sort(key=lambda x: x.date)
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    total = total_spent(transactions)
    users = user_repository.select_all()
    user = users[0]

    return render_template(
        "transactions/index.html",
        transactions=transactions,
        merchants=merchants,
        tags=tags,
        total=total,
        user=user,
    )


@transaction_blueprint.route("/transactions", methods=["POST"])
def create_transaction():
    date = request.form["date"]
    split_date = date.split("-")
    date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    amount = request.form["amount"]
    merchant_id = request.form["merchant_id"]
    tag_id = request.form["tag_id"]
    tag = tag_repository.select(tag_id)
    merchant = merchant_repository.select(merchant_id)
    transaction = Transaction(amount, tag, merchant, date)
    transaction_repository.save(transaction)
    return redirect("/transactions")


@transaction_blueprint.route("/transactions/<id>/delete", methods=["POST"])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")


@transaction_blueprint.route(
    "/transactions/month",
)
def month():

    return render_template(
        "transactions/month.html",
    )


@transaction_blueprint.route("/transactions/<month>")
def transaction_by_month(month):
    selected_transactions = []
    transactions = transaction_repository.select_all()

    for transaction in transactions:
        if transaction.date.month == int(month):
            selected_transactions.append(transaction)
    total = total_spent(selected_transactions)
    return render_template(
        "transactions/show.html", transactions=selected_transactions, total=total
    )
