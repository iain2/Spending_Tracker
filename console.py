import pdb
from models.user import User
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
import datetime


import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository

transaction_repository.delete_all()
tag_repository.delete_all()
merchant_repository.delete_all()
user_repository.delete_all()


tag1 = Tag("bill")
tag_repository.save(tag1)

tag2 = Tag("food")
tag_repository.save(tag2)

merchant1 = Merchant("Tesco")
merchant2 = Merchant("ASDA")
merchant_repository.save(merchant1)
merchant_repository.save(merchant2)

transaction1 = Transaction(60, tag2, merchant2, datetime.date(2020, 5, 17))
transaction_repository.save(transaction1)
transaction2 = Transaction(90, tag1, merchant1, datetime.date(2020, 7, 13))
transaction_repository.save(transaction2)

user1 = User(2000, "Harry")
user_repository.save(user1)

users = user_repository.select_all()
user = users[0]
print(user.name)

user1 = User(1000, "Iain", user1.id)

user_repository.update(user1)
users = user_repository.select_all()
user = users[0]
print(user.name)


# transaction3 = Transaction(30, transaction2.tag, transaction2.merchant, transaction2.id)
# transaction_repository.update(transaction3)

# tag_repository.delete(tag1.id)
# merchant_repository.delete(merchant2.id)

tags = tag_repository.select_all()
merchants = merchant_repository.select_all()
# transaction = transaction_repository.select(transaction1)


pdb.set_trace()
