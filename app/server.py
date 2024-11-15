from getpass import fallback_getpass

from .connect import client
from .mongo import collections, MongoCRUD

def get_data_by_collection(collection, query: dict[str, str] | None = None):
    instance_mogo = MongoCRUD(client, collection)
    find = instance_mogo.read({} if query is None else query)
    return find['data']

def validate_email(email: str) -> dict[str, str | bool | dict]:
    m = MongoCRUD(client, collections['can'])
    find = m.read({ 'email': email }) # { data, message }

    flag = True if find['data'] is not None and len(find['data']) else False
    print(find)
    return {
        'status': flag,
        '_id': find['data']['_id'] if find['data'] is not None else ''
    }