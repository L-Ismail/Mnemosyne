#!/usr/bin/env python3
# coding: UTF-8
#

import wx
from query_edit import MyFrame as QueryEditFrame
from query_variable import dlg_var as Variable_Dialogue
import sqlite3 as sl

connexion = sl.connect("bd_test.db")



class Dlg_query(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((520, 300))
        self.SetTitle("SQL Query")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_query = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_query, 1, wx.EXPAND, 0)

        self.listctrl_query = wx.ListCtrl(self.panel_1, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        self.listctrl_query.AppendColumn("Query", format=wx.LIST_FORMAT_LEFT, width=500)
        sizer_query.Add(self.listctrl_query, 1, wx.ALL | wx.EXPAND, 1)

        sizer_action = wx.BoxSizer(wx.VERTICAL)
        sizer_query.Add(sizer_action, 0, wx.EXPAND, 0)

        self.bt_add = wx.Button(self.panel_1, wx.ID_ANY, "Ajouter")
        sizer_action.Add(self.bt_add, 0, wx.ALL, 2)

        self.bt_mod = wx.Button(self.panel_1, wx.ID_ANY, "Modifier")
        sizer_action.Add(self.bt_mod, 0, wx.ALL, 2)

        self.bt_supp = wx.Button(self.panel_1, wx.ID_ANY, "Supprimer")
        sizer_action.Add(self.bt_supp, 0, wx.ALL, 2)

        self.bt_edit = wx.Button(self.panel_1, wx.ID_ANY, "Edit Query")
        sizer_action.Add(self.bt_edit, 0, wx.ALL, 2)
        self.bt_edit.Bind(wx.EVT_BUTTON, self.open_query_edit)

        self.bt_var = wx.Button(self.panel_1, wx.ID_ANY, "Variables")
        sizer_action.Add(self.bt_var, 0, wx.ALL, 2)
        self.bt_var.Bind(wx.EVT_BUTTON, self.open_variable_dialog)

        sizer_bt = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_bt, 0, wx.ALIGN_RIGHT | wx.ALL, 2)

        self.bt_ok = wx.Button(self.panel_1, wx.ID_ANY, u"Exécuter")
        sizer_bt.Add(self.bt_ok, 0, wx.ALL, 2)

        self.bt_annuler = wx.Button(self.panel_1, wx.ID_ANY, "Annuler")
        sizer_bt.Add(self.bt_annuler, 0, wx.ALL, 2)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

    def open_query_edit(self, event):
        query_edit_frame = QueryEditFrame(None, wx.ID_ANY, "Edit Query")
        query_edit_frame.Show()

    def open_variable_dialog(self, event):
        variable_dialog = Variable_Dialogue(None, wx.ID_ANY, "Variables")
        variable_dialog.ShowModal()
        variable_dialog.Destroy()

class MyApp(wx.App):
    def OnInit(self):
        self.frame = Dlg_query(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


if __name__ == "__main__":
    query = MyApp(0)
    query.MainLoop()
