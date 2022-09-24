from dadjokes import Dadjoke
import PySimpleGUI as sg


sg.theme("Python")
dadjoke = Dadjoke()

# All the stuff inside your window.
layout = [
    [sg.Text("Wanna hear a joke?")],
    [sg.Text(size=(30, 1), key="-OUTPUT-")],
    [sg.Button("Yes, please."), sg.Button("No way!")],
]

# Create the Window
window = sg.Window("Dad Jokes Rule", layout)

while True:
    dadjoke = Dadjoke()
    event, values = window.read()

    # See if user wants to quit or window was closed
    if event in [sg.WINDOW_CLOSED, "No way!"]:
        break

    # Output a message to a popup window
    sg.popup(dadjoke.joke)

window.close()
