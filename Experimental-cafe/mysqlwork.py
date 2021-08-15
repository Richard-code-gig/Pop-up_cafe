import pymysql
import os, time, sys, csv
from dotenv import load_dotenv


class Database:

    def __init__(self):
        load_dotenv()
        host = os.environ.get("mysql_host")
        user = os.environ.get("mysql_user")
        password = os.environ.get("mysql_pass")
        database = os.environ.get("mysql_db")

        
        self.mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )

        self.cursor = self.mydb.cursor()


    # Execute SQL query
    
    def load_product(self):
        self.cursor.execute('SELECT * FROM product') #We fetched all including PKs
        prod_elements = self.cursor.fetchall()
        prod_list = [{'product_id': t[0], 'item_name': t[1], 'price': t[2]} for t in prod_elements]
        return prod_list if prod_list else []
    
    def load_courier(self):
        self.cursor.execute('SELECT * FROM courier')
        cour_elements = self.cursor.fetchall()
        cour_list = [{'courier_id': t[0], 'courier': t[1], 'phone': t[2]} for t in cour_elements]
        return cour_list if cour_list else []
                
    def load_order(self):
        self.cursor.execute('SELECT * FROM order_tab')
        ord_elements = self.cursor.fetchall()
        ord_list = [{'order_id': t[0], 'name': t[1], 'address': t[2], 'phone': t[3], 'courier': t[4], 'status': t[5], 
                    'item_id': t[6]} for t in ord_elements]
        
        return ord_list if ord_list else []
    
    
    #Use setter and getter to insert values that will be generated in datagen.py file
    def setProduct(self, ProdVal):
        self.__ProdVal = ProdVal

    def getProduct(self):    
        return self.__ProdVal
    
    val_prod = property(getProduct, setProduct) 
        
    def insert_product(self): 
        self.cursor.execute("TRUNCATE TABLE product")
        sql = "INSERT INTO product (item_name, price) VALUES (%s, %s)" #We didn't return the Pks
        try:                                                       #This resets table's PKs after each run
            self.cursor.executemany(sql, self.val_prod)  
        except Exception as e:
            print(e)
        else:  
            self.mydb.commit() 

    def setCourier(self, CourVal):
        self.__CourVal = CourVal

    def getCourier(self):    
        return self.__CourVal
    
    val_cour = property(getCourier, setCourier)        
            
    def insert_courier(self):
        self.cursor.execute("TRUNCATE TABLE courier")
        sql = "INSERT INTO courier (name, phone) VALUES (%s, %s)"
        try:
            self.cursor.executemany(sql, self.val_cour)
        except Exception as e:
            print(e)
        else:    
            self.mydb.commit()
            
            
    def setOrder(self, OrdVal):
        self.__OrdVal = OrdVal

    def getOrder(self):    
        return self.__OrdVal
    
    val_ord = property(getOrder, setOrder)        
            
    def insert_order(self):
        self.cursor.execute("TRUNCATE TABLE order_tab")
        sql = "INSERT INTO order_tab (name, address, phone, courier, status, item_id) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            self.cursor.executemany(sql, self.val_ord)  
        except Exception as e:
            print(e)
        else:    
            self.mydb.commit()


class Pretty_print:
    
    def blink_once(self, d='PREPARING'):
        print(f'\r {d}')
        time.sleep(0.5)
        b = ("Loading")
        print('\r     ')
        time.sleep(0.5)

    def blink(self, number=3, d='PREPARING'):
        for x in range(0,number):
            self.blink_once(d)

    def loading(self):                                  
        spaces = 0                                      
        while spaces <= 7:                                     
            print("\b "*spaces+".", end=".", flush=True) 
            spaces = spaces+1                          
            time.sleep(0.3)                             
            if (spaces>2):                              
                print("\b \b"*spaces, end="")           
            spaces += 1

    def order_stat(self, d='PREPARING'):
        for _ in range(1, 4):
            print(d, end="\r")
            time.sleep(.2)
            print(' ', end="\r ")
            time.sleep(.2)

class Write_csv:
    
    def setProductCSV(self, ProdValcsv):
        self.__ProdValcsv = ProdValcsv

    def getProductCSV(self):    
        return self.__ProdValcsv
    
    val_prod_csv = property(getProductCSV, setProductCSV) 
    
    def inventory_writer_csv(self):
        with open(r'inventory-dict.csv', 'w', newline='', encoding='utf-8') as file4:
            fieldname = ['product_id', 'item_name', 'price']
            writer = csv.DictWriter(file4, fieldnames=fieldname, delimiter = ',', quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            writer.writerows(item for item in self.val_prod_csv)
 

    def setCourierCSV(self, CourValcsv):
        self.__CourValcsv = CourValcsv

    def getCourierCSV(self):    
        return self.__CourValcsv
    
    val_cour_csv = property(getCourierCSV, setCourierCSV) 

    def courier_writer_csv(self):
        with open(r'courier-dict.csv', 'w', newline='', encoding='utf-8') as file5:
            fieldname = ['courier_id', 'courier', 'phone']
            writer = csv.DictWriter(file5, fieldnames=fieldname, delimiter = ',', quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            writer.writerows(item for item in self.val_cour_csv)
            
            
    def setOrderCSV(self, OrdValcsv):
        self.__OrdValcsv = OrdValcsv

    def getOrderCSV(self):    
        return self.__OrdValcsv
    
    val_ord_csv = property(getOrderCSV, setOrderCSV)         
            
    def order_writer_csv(self):
        with open(r'order-dict.csv', 'w', newline='', encoding='utf-8') as file6:
            fieldname = ['order_id', 'name', 'address', 'phone', 'courier', 'status', 'item_id']
            writer = csv.DictWriter(file6, fieldnames=fieldname, delimiter = ',', quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            writer.writerows(item for item in self.val_ord_csv)

            
item = Database()

item.cursor.close()

item.mydb.close()

writing = Write_csv()