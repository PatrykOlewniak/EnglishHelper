import pymysql

class Connection:
    def __init__(self, user, password, database, host='localhost', port=3306, autoconect = True):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.autoconnect = autoconect
        self.conn=None
        self.curr=None
        self.initial_connection()

    conn = pymysql.connect(host='localhost', port=3306, user='englishhelper', passwd='english123', db='ENGLISH_HELPER')

    def initial_connection(self):
        self.conn = pymysql.connect(host=self.host,
                                    user=self.user,
                                    passwd=self.password,
                                    db=self.database,
                                    port=self.port)
        self.curr=self.conn.cursor()


    def query_exec(self,query):
        try:#
            sql = str(query)
            self.curr.execute(sql, ('webmaster@python.org', 'very-secret'))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
                cursor.execute(sql, ('webmaster@python.org',))
                result = cursor.fetchone()
                print(result)
        finally:
            connection.close()



k = Connection(user='englishhelper', password='english123', database='ENGLISH_HELPER')

k.initial_connection()
k.curr.execute("SELECT * FROM ENGLISH_HELPER.EnglishWords")
for row in k.curr:
    print(row)