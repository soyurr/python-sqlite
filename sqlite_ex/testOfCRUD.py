'''
Created on 2021. 7. 22.

@author: pc368
'''
from sqlite_ex import sqliteCRUD

if __name__ == '__main__':
    #테이블 만들기
    # sqliteCRUD.createTable()
    # #자료 하나 입력하기
    # sqliteCRUD.insertData('202101', 'YJP-40A', '190000', '주식회사 와이제이엘')
    # #여러 자료를 동시에 입력하기
    # t_data = (
    #     ('202102','YJP-39A','150000','주식회사 와이제이엘'),
    #     ('202103','YJP-41A','150000','주식회사 와이제이엘')
    # )
    # sqliteCRUD.insertManyData(t_data)
    
    #R테스트
    # sqliteCRUD.selectAll()
    # sqliteCRUD.select('202102')
    
    #U테스트
    # sqliteCRUD.update(('202103','YJP-41A','155500','주식회사 와이제이엘')) 
    # sqliteCRUD.select('202103') 
    
    #D테스트
    # sqliteCRUD.delete('202103')
    # sqliteCRUD.selectAll() 