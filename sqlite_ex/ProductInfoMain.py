'''
Created on 2021. 7. 22.

@author: pc368
'''
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################
from sqlite_ex import sqliteCRUD

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Product Information System", pos = wx.DefaultPosition, size = wx.Size( 513,318 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"상품번호", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        bSizer8.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txt_productNo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.txt_productNo, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"상품이름", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_staticText2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        bSizer8.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txt_productName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.txt_productName, 0, wx.ALL, 5 )
        
        
        bSizer3.Add( bSizer8, 1, wx.EXPAND, 5 )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"상품가격", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_staticText3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        bSizer10.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.txt_price = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.txt_price, 0, wx.ALL, 5 )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"제조업체명", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_staticText4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        bSizer10.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.txt_manufacturer = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.txt_manufacturer, 0, wx.ALL, 5 )
        
        
        bSizer3.Add( bSizer10, 1, wx.EXPAND, 5 )
        
        
        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"상품등록", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        bSizer4.Add( self.m_button1, 0, wx.ALL, 5 )
        
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"상품삭제", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        bSizer4.Add( self.m_button2, 0, wx.ALL, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"상품수정", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        bSizer4.Add( self.m_button3, 0, wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"상품검색", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        bSizer4.Add( self.m_button4, 0, wx.ALL, 5 )
        
        self.m_button5 = wx.Button( self, wx.ID_ANY, u"모든품목조회", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        bSizer4.Add( self.m_button5, 0, wx.ALL, 5 )
        
        
        
    
        
        self.m_button6 = wx.Button( self, wx.ID_ANY, u"지우기", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        bSizer4.Add( self.m_button6, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        self.resultArea = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,150 ), wx.HSCROLL|wx.TE_MULTILINE )
        self.resultArea.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer1.Add( self.resultArea, 0, wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnInsert )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnDelete )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnUpdate )
        self.m_button4.Bind( wx.EVT_BUTTON, self.OnFind )
        self.m_button5.Bind( wx.EVT_BUTTON, self.OnSelectAll )
        self.m_button6.Bind( wx.EVT_BUTTON, self.OnClear )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnInsert( self, event ):
        productno = self.txt_productNo.GetValue()
        productname = self.txt_productName.GetValue()
        price = self.txt_price.GetValue()
        manufacturer = self.txt_manufacturer.GetValue()
        try:
            sqliteCRUD.insertData(productno,productname,price,manufacturer)
        except:
            print('예외발생!')
        finally:
            print("등록성공")
        event.Skip()
        
    
    def OnDelete( self, event ):
        productno = self.txt_productNo.GetValue()
        try:
            sqliteCRUD.delete(productno)
        except:
            print('')
        finally:
            print("삭제완료")
        event.Skip()
    
    def OnUpdate( self, event ):
        productno = self.txt_productNo.GetValue()
        productname = self.txt_productName.GetValue()
        price = self.txt_price.GetValue()
        manufacturer = self.txt_manufacturer.GetValue()
        try:
            sqliteCRUD.update((productname,price,manufacturer,productno))
        except:
            print("예외발생!")
        finally:
            print("수정작업종료")    
        event.Skip()
        
    def OnFind( self, event ):
        key = self.txt_productNo.GetValue()
        row = sqliteCRUD.select(key)
        self.txt_productNo.SetValue(row[0])
        self.txt_productName.SetValue(row[1])
        self.txt_price.SetValue(row[2])
        self.txt_manufacturer.SetValue(row[3])
        
        event.Skip()
        event.Skip()
    
    def OnSelectAll( self, event ):
        rows = sqliteCRUD.selectAll()
        for row in rows:
            self.resultArea.AppendText("{},{},{},{}\n".format(row[0],row[1],row[2],row[3]))
            
        event.Skip()
        
    def OnClear( self, event ):
        self.txt_productNo.Clear()
        self.txt_productName.Clear()
        self.txt_price.Clear()
        self.txt_manufacturer.Clear()
        self.resultArea.Clear()

        event.Skip()
           
    

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()
