from firebird.driver import connect
from django.conf import settings

class DB:
    def __init__(self, host, database, user, password, charset='UTF8'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.charset = charset

    def connect(self):
        return connect(
            database=f'{self.host}:{self.database}',
            user=self.user,
            password=self.password,
            charset=self.charset,
        )

    def close(self):
        self.conn.close()

db = DB(settings.FIREBIRD_HOST, settings.FIREBIRD_DATABASE, settings.FIREBIRD_USER, settings.FIREBIRD_PASSWORD)