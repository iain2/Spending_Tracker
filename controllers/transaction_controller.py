from flask import Flask, redirect, render_template, Blueprint, request
from models.transaction import *
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository
import datetime

transaction_blueprint = Blueprint("Transactions", __name__)


@transaction_blueprint.route("/transactions")
def transaction():
    transactions = transaction_repository.select_all()
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    total = total_spent(transactions)

    return render_template(
        "transactions/index.html",
        transactions=transactions,
        merchants=merchants,
        tags=tags,
        total=total,
    )


# 'POST' form for add new transactions
# drop down list for tags and merchants


@transaction_blueprint.route("/transactions", methods=["POST"])
def create_transaction():
    date = request.form["date"]
    # Split the date into a list
    split_date = date.split("-")
    # create a new date object
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


# form for new tags

# form for new merchants

# total spent
# select_all loop through add translation.amount to total return total
