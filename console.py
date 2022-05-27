import pdb

from models.tag import Tag

import repositories.tag_repository as tag_repository

tag_repository.delete_all()

tag1 = Tag("bill")
tag_repository.save(tag1)

tag2 = Tag("food")
tag_repository.save(tag2)

tag_repository.delete(tag1.id)

tags = tag_repository.select_all()

for tag in tags:
    print(tag.__dict__)
