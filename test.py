import wx
import os
import wx.grid as gridlib

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))
        if not self.GetStatusBar():  # Vérifie si une barre de statut existe déjà
            self.CreateStatusBar(style=wx.BORDER_NONE)
        panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        self.label= wx.StaticText(self, label="Bonjour!", pos=(100, 100))        
        self.SetBackgroundColour(wx.Colour(255, 255, 255))  # Set background color to white
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.label = wx.StaticText(self, label="Hello World!", style=wx.ALIGN_CENTRE)
        self.vbox.Add(self.label, 0, wx.EXPAND)
        self.SetSizer(self.vbox)
        self.label2=wx.StaticText(self, label="Hello World!", style=wx.ALIGN_LEFT)
        hbox.Add(self.label2, 0, wx.EXPAND)
        self.vbox.Add(hbox, 0, wx.ALL)
        self.SetSizer(self.vbox)
        gridsizer = wx.GridSizer(4, 4, 15, 15)  # 2 rows, 2 columns, 5 pixels of horizontal and vertical gap
        for i in range(1, 6):
            button = wx.Button(self, label=f"Button {i+1}")
            button.Bind(wx.EVT_BUTTON, self.on_button_click)
            gridsizer.Add(button, 0, wx.EXPAND)
        self.SetSizer(gridsizer)
        # Create a button
        self.button = wx.Button(self, label="Click Me", pos=(210, 610))
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)
        # Create a toggle button
        self.toggle_button = wx.ToggleButton(self, label="Toggle Me", pos=(100, 500))     
        self.toggle_button.Bind(wx.EVT_TOGGLEBUTTON, self.onToggleClick)
        imageFile = os.path.join(os.path.dirname(__file__), "save-icon-5403.png")
        image = wx.Image(imageFile, wx.BITMAP_TYPE_PNG).Rescale(100, 100).ConvertToBitmap()
        self.button2 = wx.BitmapButton(self, bitmap=image, pos=(550, 550), size=(120, 120))

        self.checkbox = wx.CheckBox(self, label="Check Me", pos=(100, 400))
        self.checkbox.Bind(wx.EVT_CHECKBOX, self.on_checkbox)
        self.label = wx.StaticText(self, label="Checkbox is unchecked", pos=(100, 450))        
        def on_checkbox(self, event):
            if self.checkbox.IsChecked():
                self.label.SetLabel("Checkbox is checked")
            else:
                self.label.SetLabel("Checkbox is unchecked")

        self.rb=wx.RadioButton(self, label="Radio Button", pos=(100, 350))
        self.rb.Bind(wx.EVT_RADIOBUTTON, self.on_radio_button)
        self.rbox=wx.RadioBox(self, label="Radio Box", choices=["Choice 1", "Choice 2", "Choice 3"], pos=(500, 250))
        self.rbox.Bind(wx.EVT_RADIOBOX, self.on_selected_box)
        self.rbox.SetSelection(0)  # Set default selection to the first choice
        self.combobox = wx.ComboBox(self, choices=["Choice 1", "Choice 2", "Choice 3"], pos=(500, 350))
        self.combobox.Bind(wx.EVT_COMBOBOX, self.on_combobox)
        self.combobox.SetSelection(0)  # Set default selection to the first choice
        self.messagebox = wx.MessageDialog(self, "Hello World!", "Info", wx.OK | wx.ICON_INFORMATION)
        self.messagebox.ShowModal()
        self.messagebox.Destroy()   
        self.buttonx = wx.Button(self, label="Show Message", pos=(500, 300))
        self.buttonx.Bind(wx.EVT_BUTTON, self.show_message)
        self.Tipclick = wx.ToolTip("This is a tooltip")
        self.buttonx.SetToolTip(self.Tipclick)
        # Removed redundant status bar creation in MyPanel
        # statusbar = self.GetParent().CreateStatusBar(style=wx.BORDER_NONE)
        # statusbar.SetStatusStyke(wx.SB_NORMAL)
        # statusbar.SetStatusText("Hello World!")

        # Change txtcontrol to an instance variable
        self.txtcontrol = wx.TextCtrl(self, style=wx.TE_MULTILINE, pos=(700, 200), size=(200, 100))
        self.txtcontrol.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.buttonfont = wx.Button(self, label="Font", pos=(700, 500))
        self.buttonfont.Bind(wx.EVT_BUTTON, self.onOpen)
        self.buttonfont.SetToolTip("Choose a font")
        
        self.buttonprint = wx.Button(self, label="Print", pos=(700, 600))
        self.buttonprint.Bind(wx.EVT_BUTTON, self.printDialogue)

        self.buttonabout = wx.Button(self, label="About", pos=(400, 850), size=(50, 50))
        self.buttonabout.Bind(wx.EVT_BUTTON, self.on_about)

        self.slider=wx.Slider(self, value=50, minValue=0, maxValue=100, pos=(700, 400), size=(200, -1), style=wx.SL_HORIZONTAL | wx.SL_LABELS)

        # vbox.add(self.slider, 0, wx.ALL | wx.EXPAND, 5)

        self.txt=wx.StaticText(self, label="Hello World!", pos=(450, 450))
        # vbox.Add(self.txt, 0, wx.ALL | wx.EXPAND, 5)
        self.slider.Bind(wx.EVT_SCROLL, self.OnSliderScroll)

        mygride=gridlib.Grid(self, -1, pos=(100, 200), size=(400, 200))
        mygride.CreateGrid(5, 5)
        mygride.SetCellValue(3, 3, "Bonjour")
        mygride.SetBackgroundColour(wx.Colour(0, 255, 0))
        mygride.SetCellTextColour(3, 3, wx.WHITE)

        mygride.SetCellValue(1, 1, "Read Only")
        mygride.SetReadOnly(1, 1, True)

        mygride.SetCellEditor(1, 2, gridlib.GridCellNumberEditor(0, 1000))
        mygride.SetCellValue(1, 2, "333")
        
        # Ensure vbox is consistently used and initialized properly
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.vbox)
        self.vbox.Add(self.buttonabout, 0, wx.ALL | wx.EXPAND, 10)

        # Ensure the sizer is properly set after adding all components
        self.SetSizer(self.vbox)

        

        def OnSliderScroll(self, event):
            value = self.slider.GetValue()
            self.txt.SetLabel(f"Slider Value: {value}")
            self.txt.SetLabel(f"Slider Value: {value}")
            event.Skip()

        def on_about(self, event):
            info = wx.AboutDialogInfo()
            info.SetName("MON TEST")
            info.SetVersion("1.0")
            info.SetDescription("ABCD.")
            info.SetCopyright("(C) 2023 ????")
            info.SetWebSite("https://www.SITEFACTICE.com")
            info.AddDeveloper("SS")
            wx.AboutBox(info)

    def on_about(self, event):
        wx.MessageBox("This is a sample application.", "About", wx.OK | wx.ICON_INFORMATION)

    def printDialogue(self, event):
        data = wx.PrintDialogData()
        data.EnableSelection(True)
        data.EnablePrintToFile(True)
        data.SetMinPage(1)
        data.SetMaxPage(10)

        dialog = wx.PrintDialog(self, data)
        if dialog.ShowModal() == wx.ID_OK:
            data = dialog.GetPrintDialogData()
            print("GetAllPages: %d\n" % data.GetAllPages())
        dialog.Destroy()

    def onOpen(self, event):
        font_data = wx.FontData()
        dialog = wx.FontDialog(self, font_data)
        if dialog.ShowModal() == wx.ID_OK:
            font_data = dialog.GetFontData()
            font = font_data.GetChosenFont()
            # Apply the chosen font to relevant controls
            self.label.SetFont(font)
            self.label2.SetFont(font)
            self.txtcontrol.SetFont(font)  # Apply font to txtcontrol
        dialog.Destroy()

    def messagebox(self, event):
        wx.MessageBox("Button X clicked!", "Info", wx.OK | wx.ICON_INFORMATION)

    def show_message(self, event):
        wx.MessageBox("Hello World!", "Info", wx.OK | wx.ICON_INFORMATION)

    def on_combobox(self, event):
        selected_choice = event.GetString()
        wx.MessageBox(f"You selected: {selected_choice}", "Info", wx.OK | wx.ICON_INFORMATION)

        self.label.SetLabel(f"Selected: {selected_choice}")
        
    def on_selected_box(self, event):
        selected_choice = event.GetEventObject().GetStringSelection()
        wx.MessageBox(f"You selected: {selected_choice}", "Info", wx.OK | wx.ICON_INFORMATION)

        self.label.SetLabel(f"Selected: {selected_choice}")
        self.rbox.Bind(wx.EVT_RADIOBOX, self.on_selected_box)

    def on_button_click(self, event):
        wx.MessageBox("Button clicked!", "Info", wx.OK | wx.ICON_INFORMATION)

    def onToggleClick(self, event):
        state= event.GetEventObject().GetValue()
        if state== True:
            self.label.SetLabel("Toggle is ON")
            event.GetEventObject().SetLabel("Click to ON")
        else:
            self.label.SetLabel("Toggle is OFF")
            event.GetEventObject().SetLabel("Click to OFF")

    def on_checkbox(self, event):
        checkbox_state = event.IsChecked()
        if checkbox_state:
            wx.MessageBox("Checkbox is checked!", "Info", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("Checkbox is unchecked!", "Info", wx.OK | wx.ICON_INFORMATION)
    
    def on_radio_button(self, event):
            radio_button_state = event.GetEventObject().GetValue()
            if radio_button_state:
                wx.MessageBox("Radio button is selected!", "Info", wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox("Radio button is deselected!", "Info", wx.OK | wx.ICON_INFORMATION)
            rb= event.GetEventObject()
            self.label.SetLabel(f"Radio button is {'selected' if rb.GetValue() else 'deselected'}")

    def Question(self, event):
        question = wx.MessageDialog(self, "Do you want to continue?", "Question", wx.YES_NO | wx.ICON_QUESTION)
        result = question.ShowModal()
        if result == wx.ID_YES:
            wx.MessageBox("You clicked Yes!", "Info", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("You clicked No!", "Info", wx.OK | wx.ICON_INFORMATION)

    def OnSliderScroll(self, event):
        obj= event.GetEventObject()
        value = obj.GetValue()
        font=self.GetFont()
        font.SetPointSize(self.slider.GetValue())
        self.txt.SetFont(font)
        # value = self.slider.GetValue()
        # self.txt.SetLabel(f"Slider Value: {value}")
        # self.txt.SetLabel(f"Slider Value: {value}")
        # event.Skip()

        
if __name__ == "__main__":
    app = wx.App(False)  # Création de l'instance wx.App avant toute opération wx
    frame = MyFrame(parent=None, title="Essai#1")
    frame.Show()
    app.MainLoop()