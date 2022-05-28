from crypt import methods
from gettext import translation
from flask import Flask, redirect, render_template, Blueprint, request
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

transaction_blueprint = Blueprint("Transactions", __name__)


@transaction_blueprint.route("/transactions")
def transaction():
    transactions = transaction_repository.select_all()
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()

    return render_template(
        "transactions/index.html",
        transactions=transactions,
        merchants=merchants,
        tags=tags,
    )


# 'POST' form for add new transactions
# drop down list for tags and merchants


@transaction_blueprint.route("/transactions", methods=["POST"])
def create_transaction():
    amount = request.form["amount"]
    merchant_id = request.form["merchant_id"]
    tag_id = request.form["tag_id"]
    tag = tag_repository.select(tag_id)
    merchant = merchant_repository.select(merchant_id)
    transaction = Transaction(amount, tag, merchant)
    transaction_repository.save(transaction)
    return redirect("/transactions")


# form for new tags

# form for new merchants

# total spent
# select_all loop through add translation.amount to total return total
