# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-115-g11c2dec8)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################


import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/opt/homebrew/Cellar/wxwidgets/3.3.1/include/wx-3.3/wx/')

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class CalculatorFrame
###########################################################################

class CalculatorFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 308,311 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        topLevelSizer = wx.BoxSizer( wx.VERTICAL )

        textControlSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.textInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,40 ), 0 )
        textControlSizer.Add( self.textInput, 1, wx.ALL, 5 )


        topLevelSizer.Add( textControlSizer, 0, wx.EXPAND, 5 )

        GridButtonSizer = wx.GridSizer( 5, 4, 5, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, _(u"7"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button1, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, _(u"8"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button2, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, _(u"9"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button3, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button4 = wx.Button( self, wx.ID_ANY, _(u"*"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button4, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button5 = wx.Button( self, wx.ID_ANY, _(u"6"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button5, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button6 = wx.Button( self, wx.ID_ANY, _(u"5"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button6, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button7 = wx.Button( self, wx.ID_ANY, _(u"4"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button7, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button8 = wx.Button( self, wx.ID_ANY, _(u"+"), wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
        GridButtonSizer.Add( self.m_button8, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button9 = wx.Button( self, wx.ID_ANY, _(u"3"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button9, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button10 = wx.Button( self, wx.ID_ANY, _(u"2"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button10, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button11 = wx.Button( self, wx.ID_ANY, _(u"1"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button11, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button12 = wx.Button( self, wx.ID_ANY, _(u"/"), wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
        GridButtonSizer.Add( self.m_button12, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button13 = wx.Button( self, wx.ID_ANY, _(u"0"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button13, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button14 = wx.Button( self, wx.ID_ANY, _(u"."), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button14, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button15 = wx.Button( self, wx.ID_ANY, _(u"EXP"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button15, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button16 = wx.Button( self, wx.ID_ANY, _(u"-"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button16, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button17 = wx.Button( self, wx.ID_ANY, _(u"DEL"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button17, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button18 = wx.Button( self, wx.ID_ANY, _(u"AC"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button18, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button19 = wx.Button( self, wx.ID_ANY, _(u"ANS"), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button19, 0, wx.LEFT|wx.RIGHT, 5 )

        self.m_button20 = wx.Button( self, wx.ID_ANY, _(u"="), wx.DefaultPosition, wx.Size( 65,35 ), 0 )
        GridButtonSizer.Add( self.m_button20, 0, wx.LEFT|wx.RIGHT, 5 )


        topLevelSizer.Add( GridButtonSizer, 1, wx.EXPAND, 5 )


        self.SetSizer( topLevelSizer )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


