#!/usr/bin/env python3
# coding: UTF-8
#


import wx

import sqlite3 as sl

connexion = sl.connect("bd_test.db")

curseur = connexion.cursor()



class dlg_var(wx.Dialog):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((730, 441))
        self.SetTitle("dialog")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_var = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_var, 1, wx.EXPAND, 0)

        sizer_listvar = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Variables"), wx.VERTICAL)
        sizer_var.Add(sizer_listvar, 1, wx.ALL | wx.EXPAND, 2)

        self.listbox_variable = wx.ListBox(sizer_listvar.GetStaticBox(), wx.ID_ANY, choices=["choice 1"])
        sizer_listvar.Add(self.listbox_variable, 1, wx.ALL | wx.EXPAND, 2)

        sizer_btvar = wx.BoxSizer(wx.HORIZONTAL)
        sizer_listvar.Add(sizer_btvar, 0, wx.ALL | wx.EXPAND, 2)

        self.bt_add = wx.Button(sizer_listvar.GetStaticBox(), wx.ID_ANY, "Ajouter")
        sizer_btvar.Add(self.bt_add, 1, wx.ALL, 2)

        self.button_modif = wx.Button(sizer_listvar.GetStaticBox(), wx.ID_ANY, "Modifier")
        sizer_btvar.Add(self.button_modif, 1, wx.ALL, 2)

        self.button_3 = wx.Button(sizer_listvar.GetStaticBox(), wx.ID_ANY, "Supprimer")
        sizer_btvar.Add(self.button_3, 1, wx.ALL, 2)

        sizer_param = wx.BoxSizer(wx.VERTICAL)
        sizer_var.Add(sizer_param, 2, wx.EXPAND, 0)

        gridsizer_var = wx.FlexGridSizer(2, 2, 2, 2)
        sizer_param.Add(gridsizer_var, 0, wx.EXPAND, 0)

        lib_var = wx.StaticText(self, wx.ID_ANY, u"Libellé")
        gridsizer_var.Add(lib_var, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)

        self.text_var = wx.TextCtrl(self, wx.ID_ANY, "")
        gridsizer_var.Add(self.text_var, 0, wx.EXPAND, 0)

        lib_type = wx.StaticText(self, wx.ID_ANY, "Type variable")
        gridsizer_var.Add(lib_type, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)

        self.chx_var = wx.Choice(self, wx.ID_ANY, choices=["Texte", "Nombre entier", u"Nombre décimal", u"Booléen"])
        self.chx_var.SetSelection(0)
        gridsizer_var.Add(self.chx_var, 0, wx.ALL | wx.EXPAND, 2)

        sizer_min_max = wx.BoxSizer(wx.HORIZONTAL)
        sizer_param.Add(sizer_min_max, 0, wx.EXPAND, 0)

        self.cbox_min = wx.CheckBox(self, wx.ID_ANY, "Min")
        sizer_min_max.Add(self.cbox_min, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)

        self.text_min = wx.TextCtrl(self, wx.ID_ANY, "")
        sizer_min_max.Add(self.text_min, 1, wx.ALL | wx.EXPAND, 2)

        self.cbox_max = wx.CheckBox(self, wx.ID_ANY, "Max")
        sizer_min_max.Add(self.cbox_max, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)

        self.text_max = wx.TextCtrl(self, wx.ID_ANY, "")
        sizer_min_max.Add(self.text_max, 1, wx.ALL | wx.EXPAND, 2)

        lib_comment = wx.StaticText(self, wx.ID_ANY, "Commentaire")
        sizer_param.Add(lib_comment, 0, 0, 0)

        self.text_comment = wx.TextCtrl(self, wx.ID_ANY, "")
        sizer_param.Add(self.text_comment, 1, wx.ALL | wx.EXPAND, 2)

        sizer_bt = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_bt, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.bt_ok = wx.Button(self, wx.ID_OK, "")
        self.bt_ok.SetDefault()
        sizer_bt.AddButton(self.bt_ok)

        self.bt_annuler = wx.Button(self, wx.ID_CANCEL, "")
        sizer_bt.AddButton(self.bt_annuler)

        sizer_bt.Realize()

        gridsizer_var.AddGrowableCol(1)

        self.SetSizer(sizer_1)

        self.SetAffirmativeId(self.bt_ok.GetId())
        self.SetEscapeId(self.bt_annuler.GetId())

        self.Layout()

        self.bt_add.Bind(wx.EVT_BUTTON, self.add_variable)

    def add_variable(self, event, args, argument_a, argument_b):

        argument_a=input("entrer terme a: ")
        argument_b=("entrer terme b: ")
        if argument_a != argument_b:
            print((argument_a, argument_b))
        else:
            wx.MessageBox("Les deux termes sont identiques", "Info", wx.OK | wx.ICON_INFORMATION)


class MyApp(wx.App):
    def OnInit(self):
        self.dlg_variables = dlg_(None, wx.ID_ANY, "")
        self.SetTopWindow(self.dlg_variables)
        self.dlg_variables.ShowModal()
        self.dlg_variables.Destroy()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
