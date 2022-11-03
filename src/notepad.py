import PySimpleGUI as sg

#sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
menubar_layout = [['File', ['Open', 'Save', 'Exit',]],
                ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                ['Help', 'About...'],]

layout = [  [sg.MenuBar(menubar_layout)],
            [sg.Multiline(expand_x=True, expand_y=True, key='textbox')],
            [sg.StatusBar('Status'),sg.FilesBrowse('Open Test')]]

# Create the Window
window = sg.Window(
    'Notepad ¯\_(ツ)_/¯', 
    size=(400,300),
    layout = layout, 
    resizable=True,
    margins=(0,0),
    finalize=True )
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('Event/Values: ', event, values)
    #print(values['textbox'])

window.close()