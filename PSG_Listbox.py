import PySimpleGUI as sg

sg.theme("Dark Blue 3")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
layout = [
    [
        sg.Listbox(
            values=lista,
            size=(20, 4),
            font=("Arial Bold", 14),
            expand_y=True,
            enable_events=True,
            key="-LIST-",
        )
    ]
]

janela = sg.Window("listbox", layout, resizable=True)
while True:
    eventos, valores = janela.read()
    if eventos == "-LIST-":
        print(valores["-LIST-"][0])
    if eventos == sg.WINDOW_CLOSED:
        break
