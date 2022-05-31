from db.run_sql import run_sql

from models.tag import Tag


def save(tag):
    sql = "INSERT INTO tags (name, active) VALUES (?,?) RETURNING *"
    values = [tag.name, tag.active]
    results = run_sql(sql, values)
    id = results[0]["id"]
    tag.id = id
    return tag


def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row["name"], bool(row["active"]), row["id"])
        tags.append(tag)
    return tags


def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result["name"], bool(result["active"]), result["id"])
    return tag


def delete_all():
    sql = "DELETE  FROM tags"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM tags WHERE id = ?"
    values = [id]
    run_sql(sql, values)


def update(tag):
    sql = "UPDATE tags SET (name, active) = (?,?) WHERE id = ?"
    values = [tag.name, tag.active, tag.id]
    run_sql(sql, values)
