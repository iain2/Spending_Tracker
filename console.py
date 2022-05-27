import pdb
from models.merchant import Merchant

from models.tag import Tag

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

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

tag_repository.delete(tag1.id)
merchant_repository.delete(merchant2.id)

tags = tag_repository.select_all()
merchants = merchant_repository.select_all()

for tag in merchants:
    print(tag.__dict__)
