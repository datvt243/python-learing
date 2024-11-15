from abc import abstractmethod

from pymongo.errors import PyMongoError

class AbstractCRUD:
    @abstractmethod
    def create(self, query: dict[str, str]):
        pass

    @abstractmethod
    def read(self, query):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

class MongoBase:
    db_name = 'resume-api'

    def __init__(self, client, collection):
        self.client = client
        self.db = self.client[self.db_name]
        self.col = self.db[collection]

    def close_conn(self):
        self.client.close()

class MongoCRUD(MongoBase, AbstractCRUD):
    def read(self, query):
        try:
            doc = self.col.find_one(query, {'password': 0, '__v': 0 })
            if doc:
                return {
                    'data': doc,
                    'message': ''
                }
            return {
                'data': None,
                'message': 'No document found matching query.'
            }
        except PyMongoError as e:
            raise e

    def create(self, query):
        pass

    def update(self):
        pass

    def delete(self):
        pass