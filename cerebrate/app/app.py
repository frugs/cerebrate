import PySimpleGUI as sg

sg.theme("Default1")


def main():
    layout = [[sg.Text("Hello, world!")]]
    window = sg.Window("Cerebrate", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == "__main__":
    main()
