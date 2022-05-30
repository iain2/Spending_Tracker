import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
import datetime


import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

transaction_repository.delete_all()
tag_repository.delete_all()
merchant_repository.delete_all()


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

# transaction3 = Transaction(30, transaction2.tag, transaction2.merchant, transaction2.id)
# transaction_repository.update(transaction3)

# tag_repository.delete(tag1.id)
# merchant_repository.delete(merchant2.id)

tags = tag_repository.select_all()
merchants = merchant_repository.select_all()
# transaction = transaction_repository.select(transaction1)

print(transaction1.date.month)


pdb.set_trace()
