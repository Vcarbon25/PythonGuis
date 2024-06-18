"""
import wx

app = wx.App()
frame = wx.Frame(parent=None, title='Hello World')
frame.Show()
app.MainLoop()"""
# define as class
import wx


class MinhaTela(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Hello World")
        self.Show()


if __name__ == "__main__":
    app = wx.App()
    frame = MinhaTela()
    app.MainLoop()
