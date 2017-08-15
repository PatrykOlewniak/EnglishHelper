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


    def query_exec(self, query, fetchAll=False):
        """:return: single row (first one) if default value -if fetchAll=False
                    if fetchAll positive - return list with query result elements"""
        query = str(query)
        self.curr.execute(query)
        self.conn.commit()

        if fetchAll:
            resultList=[]
            for k in self.curr:
                resultList.append((k))
            return resultList
        else:
            result = self.curr.fetchone()
            return result


    def close_connection(self):
        self.conn.close()



