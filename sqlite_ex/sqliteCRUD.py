'''
Created on 2021. 7. 22.
상품정보 CRUD
@author: pc368
'''
import sqlite3
#C - 테이블 생성하기
def createTable():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS PRODUCT
        (PRODUCTNO TEXT PRIMARY KEY,
        PRODUCTNAME TEXT,
        PRICE TEXT,
        MANUFACTURER TEXT)
    ''')
    conn.commit()
    c.close()
    conn.close()
    pass
#C - 데이터등록하기
def insertData(productno,productname,price,manufacturer):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO PRODUCT(productno,productname,price,manufacturer)
        VALUES(?,?,?,?)
    ''',(productno,productname,price,manufacturer) )
    conn.commit()
    c.close()
    conn.close()
    pass

def insertManyData(tupleData):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.executemany('''
        INSERT INTO PRODUCT(productno,productname,price,manufacturer)
        VALUES(?,?,?,?)''',tupleData)

    conn.commit()
    c.close()
    conn.close()
    pass

#R - Read(select)
def selectAll():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute('SELECT * FROM PRODUCT') 
    rows = c.fetchall()
    conn.commit()
    c.close()
    conn.close()
    pass
    return rows

def select(key):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute('SELECT * FROM PRODUCT WHERE PRODUCTNO = ?',(key,)) 
    row = c.fetchone()
    conn.commit()
    c.close()
    conn.close()
    return row
    pass


#U - Update
def update(vo):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute('''
        UPDATE PRODUCT SET PRODUCTNAME=?, PRICE=?, MANUFACTURER=? WHERE PRODUCTNO=?
    ''',vo)
    
    conn.commit()
    c.close()
    conn.close()
    pass

#D- Delete
def delete(key):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    res = c.execute('''DELETE FROM PRODUCT WHERE PRODUCTNO = ?''',(key,))

    conn.commit()
    c.close()
    conn.close()
    return len(list(res)) #삭제된 것이 있다면 리스트에 만들어진 개수만큼 리턴시킴
    pass
