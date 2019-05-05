import pymysql.cursors # 游标
from . import settings

sqlConnect = pymysql.connect(
    host = settings.Mysql_host,
    user = settings.Mysql_user,
    passwd = settings.Mysql_pwd,
    db = settings.Mysql_db,
    charset = 'utf8'
)

cur = sqlConnect.cursor()  # 操作的游标对象

class Sql:
    @staticmethod
    def insert_pm25(dataItem):
        sqlCommand = 'insert into pmdatanew values (null ,"%s","%s","%s","%s","%s","%s")'\
        %(dataItem['pmTime'],dataItem['airCondition'],dataItem['city'],dataItem['province'],dataItem['AQI'],dataItem['pmConcentration'],)
        print(sqlCommand)
        cur.execute(sqlCommand)
        sqlConnect.commit() # 提交数据
        pass

    @classmethod
    def closeMysql(cls):
        cur.close()
        sqlConnect.close()
        pass
    pass