import mysql.connector
from mysql.connector import errorcode
from logger import *

ordersLogger = Logger()
# Mainly for handling Backend Server Connections


class OrdersManager:
    def __init__(self):
        self.connected = False
        self.conn = None

    def callServer(self):
        config = {
            'host': 'chi-pnode1.websitehostserver.net',
            'user': 'sungloww_orderform_w',
            'password': 'Window12345',
            'database': 'sungloww_orders_db'
        }
        try:
            self.conn = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                return("Database does not exist")
            else:
                return(err)
        else:
            self.connected = True
            self.cursor = self.conn.cursor(dictionary=True)
            return("Connected")

    def getOrders(self):
        self.callServer()
        if(self.connected == True):
            # cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='test1')
            sql = ("SELECT * FROM `order_tag` WHERE `submit` = '1'")
            self.cursor.execute(sql)

            result = []

            # results = cursor.fetchall()
            # print(results)

            row = self.cursor.fetchone()
            while row is not None:
                # print(row.get('orderTag'))
                # print(row.get('PO'))
                # print(row.get('email'))
                # print('\n')
                result.append(row)
                # print(row)
                row = self.cursor.fetchone()

            # cursor = conn.cursor()
            # cursor.execute("SELECT * FROM `order_tag` WHERE `submit` = '1'")
            # for row in cursor:
            #     # print(type(row))
            #     print(row)
            self.conn.close()
            self.connected = False
            return result
        else:
            self.conn.close()
            return -105

    def getProducts(self, POList):
        self.callServer()
        if(self.connected == True):
            result = []
            # print(POList)
            for PO in POList:
                # for PO in range(1):
                # cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='test1')
                sql = (
                    f"SELECT * FROM `order_entry` WHERE `PO` = '{PO}' ORDER BY `date` ASC")
                # sql = (f"SELECT * FROM `order_entry` WHERE `PO` = '{PO}' ORDER BY CONVERT(shadeID, SIGNED) ASC")
                self.cursor.execute(sql)

                currentOrder = []
                # results = cursor.fetchall()
                # print(results)

                row = self.cursor.fetchone()
                while row is not None:
                    # print(row.get('reid'))
                    # print(row.get('shadeID'))
                    # print(row.get('email'))
                    # print('\n')
                    currentOrder.append(row)
                    # print(row)
                    row = self.cursor.fetchone()

                # cursor = conn.cursor()
                # cursor.execute("SELECT * FROM `order_tag` WHERE `submit` = '1'")
                # for row in cursor:
                #     # print(type(row))
                #     print(row)
                # conn.close()
                # print('\n'.join('{}: {}'.format(*k) for k in enumerate(currentOrder)))
                # print()
                result.append(currentOrder)
            # print(result)
            self.conn.close()
            self.connected = False
            return result
        else:
            self.conn.close()
            return -105

    def submitOrder(self, POList):
        self.callServer()
        if(self.connected == True):
            myRows = 0
            # rows = 2
            # Rows = 8
            # POList = ['ReiCheck', '15604323949365', '15602836445485']
            for PO in POList:
                sql = (
                    f"UPDATE `order_tag` SET `submit` = 92 WHERE `PO` = '{PO}'")
                ordersLogger.log(sql)
                # sql = (f"UPDATE `order_tag` SET `submit` = 10 WHERE `PO` = '{PO}'")
                self.cursor.execute(sql)
                self.conn.commit()
                myRows += self.cursor.rowcount
                # results = cursor.fetchall()
                # print(results)
                # print(f'Rows updated: {myRows}')
                # row = self.cursor.fetchone()
                # while row is not None:
                # print()
                # print(row)

            ordersLogger.log("Submitted Orders")
            ordersLogger.log(
                "------------------------------------------------------")
            ordersLogger.log("")
            return myRows
        else:
            return -105

    def getSimpleService(self):
        self.callServer()
        if(self.connected == True):
            # cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='test1')
            sql = ("SELECT * FROM `simple_service` where submit = 1")
            self.cursor.execute(sql)

            result = []

            row = self.cursor.fetchone()
            while row is not None:
                result.append(row)
                row = self.cursor.fetchone()

            self.conn.close()
            self.connected = False
            return len(result)
        else:
            self.conn.close()
            return -105
