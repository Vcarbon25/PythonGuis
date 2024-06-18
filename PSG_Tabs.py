import PySimpleGUI as psg

psg.set_options(font=("Arial Bold", 14))
# l1 is the layout for tab1
# l2 is the layout for tab2
l1 = psg.Text("Enter Name")
lt1 = psg.Text("Address")
t1 = psg.Input("", key="-NM-")
a11 = psg.Input(key="-a11-")
a12 = psg.Input(key="-a12-")
a13 = psg.Input(key="-a13-")
tab1 = [[l1, t1], [lt1], [a11], [a12], [a13]]
lt2 = psg.Text("EmailID:")
lt3 = psg.Text("Mob No:")
a21 = psg.Input("", key="-ID-")
a22 = psg.Input("", key="-MOB-")
tab2 = [[lt2, a21], [lt3, a22]]
layout = [
    [psg.TabGroup([[psg.Tab("Basic Info", tab1), psg.Tab("Contact Details", tab2)]])],
    [psg.OK(), psg.Cancel()],
]
# This titlegroup object may be further used
# in the row of the main layout.
window = psg.Window("Tab Group Example", layout)
while True:
    event, values = window.read()
    print(event, values)
    if event in (psg.WIN_CLOSED, "Exit"):
        break
window.close()
