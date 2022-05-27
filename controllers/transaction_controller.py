from flask import Flask, redirect, render_template, Blueprint
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

transaction_blueprint = Blueprint("Transactions", __name__)


@transaction_blueprint.route("/transactions")
def books():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions=transactions)
