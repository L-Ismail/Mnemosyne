#!/usr/bin/env python3
# coding: UTF-8
#
#

import wx
from query_variable import dlg_var
import sqlite3 as sl

connexion = sl.connect("bd_test.db")
curseur = connexion.cursor()


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle(u"Edition requête SQL")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)

        sizer_panel1 = wx.BoxSizer(wx.VERTICAL)

        self.nbook_base = wx.Notebook(self.panel_1, wx.ID_ANY, style=0)
        sizer_panel1.Add(self.nbook_base, 0, wx.ALL | wx.EXPAND, 2)

        self.nbpage_mysql = wx.Panel(self.nbook_base, wx.ID_ANY)
        self.nbook_base.AddPage(self.nbpage_mysql, "MySQL")

        grid_sizer_1 = wx.FlexGridSizer(3, 4, 2, 2)

        self.lib_host = wx.StaticText(self.nbpage_mysql, wx.ID_ANY, "Serveur")
        grid_sizer_1.Add(self.lib_host, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)

        self.text_host = wx.TextCtrl(self.nbpage_mysql, wx.ID_ANY, "")
        grid_sizer_1.Add(self.text_host, 0, wx.ALL | wx.EXPAND, 2)

        self.lib_port = wx.StaticText(self.nbpage_mysql, wx.ID_ANY, "Port")
        grid_sizer_1.Add(self.lib_port, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)

        self.text_port = wx.TextCtrl(self.nbpage_mysql, wx.ID_ANY, "")
        grid_sizer_1.Add(self.text_port, 0, wx.ALL | wx.EXPAND, 2)

        self.lib_base = wx.StaticText(self.nbpage_mysql, wx.ID_ANY, "Base")
        grid_sizer_1.Add(self.lib_base, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)

        self.text_base = wx.TextCtrl(self.nbpage_mysql, wx.ID_ANY, "")
        grid_sizer_1.Add(self.text_base, 0, wx.ALL | wx.EXPAND, 2)

        grid_sizer_1.Add((20, 20), 0, wx.ALIGN_CENTER_VERTICAL, 0)

        grid_sizer_1.Add((20, 20), 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.lib_user = wx.StaticText(self.nbpage_mysql, wx.ID_ANY, "Utilisateur")
        grid_sizer_1.Add(self.lib_user, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)

        self.text_user = wx.TextCtrl(self.nbpage_mysql, wx.ID_ANY, "")
        grid_sizer_1.Add(self.text_user, 0, wx.ALL | wx.EXPAND, 2)

        self.lib_passw = wx.StaticText(self.nbpage_mysql, wx.ID_ANY, "Mot de passe")
        grid_sizer_1.Add(self.lib_passw, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)

        self.text_passw = wx.TextCtrl(self.nbpage_mysql, wx.ID_ANY, "", style=wx.TE_PASSWORD)
        grid_sizer_1.Add(self.text_passw, 0, wx.ALL | wx.EXPAND, 2)

        self.nbpage_sqlite = wx.Panel(self.nbook_base, wx.ID_ANY)
        self.nbook_base.AddPage(self.nbpage_sqlite, "SQLite")

        grid_sizer_sqlite = wx.FlexGridSizer(1, 2, 2, 2)

        self.lib_filesqlite = wx.StaticText(self.nbpage_sqlite, wx.ID_ANY, "Fichier")
        grid_sizer_sqlite.Add(self.lib_filesqlite, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)

        self.select_file = wx.FilePickerCtrl(self.nbpage_sqlite, wx.ID_ANY, "", "Select file", "Text files (*.txt)|*.txt|All files|*.*")
        grid_sizer_sqlite.Add(self.select_file, 0, wx.ALL | wx.EXPAND, 2)

        sizer_sql = wx.StaticBoxSizer(wx.StaticBox(self.panel_1, wx.ID_ANY, "SQL"), wx.VERTICAL)
        sizer_panel1.Add(sizer_sql, 1, wx.ALL | wx.EXPAND, 2)

        sizerh_sql = wx.BoxSizer(wx.HORIZONTAL)
        sizer_sql.Add(sizerh_sql, 1, wx.EXPAND, 0)

        self.text_sql = wx.TextCtrl(sizer_sql.GetStaticBox(), wx.ID_ANY, "", style=wx.TE_MULTILINE)
        sizerh_sql.Add(self.text_sql, 3, wx.ALL | wx.EXPAND, 2)

        sizer_var = wx.BoxSizer(wx.VERTICAL)
        sizerh_sql.Add(sizer_var, 1, wx.ALL | wx.EXPAND, 2)

        self.bt_variable = wx.Button(sizer_sql.GetStaticBox(), wx.ID_ANY, "Variables")
        sizer_var.Add(self.bt_variable, 0, wx.ALL | wx.EXPAND, 2)

        self.listbox_variable = wx.ListBox(sizer_sql.GetStaticBox(), wx.ID_ANY, choices=["choice 1"])
        sizer_var.Add(self.listbox_variable, 1, wx.ALL | wx.EXPAND, 2)

        sizer_chxbox = wx.BoxSizer(wx.VERTICAL)
        sizer_sql.Add(sizer_chxbox, 0, 0, 0)

        self.ckbox_newgrid = wx.CheckBox(sizer_sql.GetStaticBox(), wx.ID_ANY, u"Créer une nouvelle grille")
        sizer_chxbox.Add(self.ckbox_newgrid, 0, wx.ALL, 1)

        sizer_bt = wx.BoxSizer(wx.HORIZONTAL)
        sizer_panel1.Add(sizer_bt, 0, wx.ALIGN_RIGHT, 0)

        self.bt_ok = wx.Button(self.panel_1, wx.ID_ANY, u"Exécuter")
        sizer_bt.Add(self.bt_ok, 2, wx.ALL, 2)

        self.bt_fermer = wx.Button(self.panel_1, wx.ID_ANY, "Fermer")
        sizer_bt.Add(self.bt_fermer, 0, wx.ALL, 2)

        grid_sizer_sqlite.AddGrowableCol(1)
        self.nbpage_sqlite.SetSizer(grid_sizer_sqlite)

        grid_sizer_1.AddGrowableCol(1)
        grid_sizer_1.AddGrowableCol(3)
        self.nbpage_mysql.SetSizer(grid_sizer_1)

        self.panel_1.SetSizer(sizer_panel1)

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.Layout()

        self.listbox_variable.Bind(wx.EVT_LISTBOX_DCLICK, self.evt_addvariable)
        self.bt_ok.Bind(wx.EVT_BUTTON, self.ExecSQL)
        self.bt_variable.Bind(wx.EVT_BUTTON, self.open_variable_dialog)


    def evt_addvariable(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'evt_addvariable' not implemented!")
        event.Skip()

    def ExecSQL(self, event, var):  # wxGlade: MyFrame.<event_handler>
        curseur.execute("SELECT * FROM eleve WHERE identifiant = ?", (var))
        print ("Information élève-------\n", curseur.fetchall())
        wx.MessageBox(("Information élève-------\n", curseur.fetchall()), "Info", wx.OK | wx.ICON_INFORMATION)

        print("Event handler 'ExecSQL' not implemented!")
        # event.Skip()

    def open_variable_dialog(self, event):
        variable_dialog = dlg_var(self, wx.ID_ANY, "Variables")
        variable_dialog.ShowModal()
        variable_dialog.Destroy()


