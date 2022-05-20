# Trabajo realizado por Javier García González
#
#
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Fri May 20 19:09:53 2022
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((569, 447))
        self.SetTitle(u"ParKing - Paradigmas de Programación")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("E:\\GitHub\\Practica_2\\coche.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)

        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(sizer_6, 1, wx.EXPAND, 0)

        Seleccion_Nivel = wx.StaticText(self.panel_1, wx.ID_ANY, "Seleccione Nivel")
        Seleccion_Nivel.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_6.Add(Seleccion_Nivel, 0, wx.EXPAND | wx.LEFT, 15)

        self.list_box_1 = wx.ListBox(self.panel_1, wx.ID_ANY, choices=["choice 1"])
        self.list_box_1.SetSelection(0)
        sizer_6.Add(self.list_box_1, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(sizer_7, 1, wx.EXPAND, 0)

        self.button_2 = wx.Button(self.panel_1, wx.ID_ANY, "Comenzar")
        sizer_7.Add(self.button_2, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT | wx.RIGHT,  0)

        self.button_3 = wx.Button(self.panel_1, wx.ID_ANY, "Deshacer")
        sizer_7.Add(self.button_3, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT | wx.RIGHT, 0)

        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(sizer_8, 1, wx.EXPAND, 0)

        Tiempo_Restante = wx.StaticText(self.panel_1, wx.ID_ANY, "Tiempo Restante")
        Tiempo_Restante.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_8.Add(Tiempo_Restante, 0, wx.EXPAND | wx.LEFT, 15)

        label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, "90", style=wx.ALIGN_CENTER_HORIZONTAL)
        label_4.SetFont(wx.Font(45, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_8.Add(label_4, 1, wx.EXPAND, 0)

        grid_sizer_1 = wx.GridSizer(8, 8, 0, 0)
        sizer_4.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Elija un nivel")
        label_1.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_3.Add(label_1, 0, wx.LEFT, 10)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        self.Centre()
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
