import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import DbModel

logging.basicConfig(level=logging.INFO)

class Cluster():
    def __init__(self) -> None:
        self.hive = [
            Node("es1"),
            Node('es2'),
            Node('es3')
        ]

    def filter_query(self):
        for node in self.hive:
            node.filter_query()
    
    def get_all_query(self):
        for node in self.hive:
            node.get_all_query()
    
class Node():
    def __init__(self,server) -> None:
        self.server = server
        ELASTICSEARCH = {
            'engine': 'elasticsearch',
            'host': server,
            'port': 9200,
            'user': 'elastic',
            'password': 'changeme'
        }

        engine = create_engine("{engine}://{host}:{port}".format(**ELASTICSEARCH))
    
        self.session_local = sessionmaker(
            bind=engine
        )

    def get_db(self):
        db = self.session_local()
        try:
            yield db
        finally:
            db.close()

    def print_result(self, collection: list, func_name: str):
        for item in collection:
            logging.info("{} {}: {}".format(self.server,func_name, str(item)))

    def filter_query(self):
        db = next(self.get_db())
        collection = db.query(DbModel).filter_by(id=3).all()
        self.print_result(collection, "filter_query")

    def get_all_query(self):
        db = next(self.get_db())
        collection = db.query(DbModel).all()
        self.print_result(collection, "get_all_query")
