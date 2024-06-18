import PySimpleGUI as psg

psg.set_options(font=("Arial Bold", 14))
toprow = ["S.No.", "Name", "Age", "Marks"]
rows = [
    [1, "Rajeev", 23, 78],
    [2, "Rajani", 21, 66],
    [3, "Rahul", 22, 60],
    [4, "Robin", 20, 75],
]
tbl1 = psg.Table(
    values=rows,
    headings=toprow,
    auto_size_columns=True,
    display_row_numbers=False,
    justification="center",
    key="-TABLE-",
    selected_row_colors="red on yellow",
    enable_events=True,
    expand_x=True,
    expand_y=True,
    enable_click_events=True,
)
layout = [[tbl1]]
window = psg.Window("Table Demo", layout, size=(715, 200), resizable=True)
while True:
    event, values = window.read()
    print("event:", event, "values:", values)
    if event == psg.WIN_CLOSED:
        break
    if "+CLICKED+" in event:
        psg.popup("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))
window.close()
