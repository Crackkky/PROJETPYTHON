# Cette classe permet d'appliquer facilement un theme global a des widgets

WIDTH = 500
HEIGHT = 250


def rootStyle(root):
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
    root.configure(background='gray')


def buttonStyle(button):
    types = ['bg', 'fg', 'activeforeground', 'activebackground', 'borderwidth']
    values = ['black', 'pink', 'black', 'pink', 3]
    apply(types, values, button)


def checkButtonStyle(checkButton):
    buttonStyle(checkButton)
    types = ['selectcolor']
    values = ['gray']
    apply(types, values, checkButton)


def labelStyle(label):
    types = ['bg', 'fg', 'borderwidth', 'relief']
    values = ['black', 'pink', 2, 'sunken']
    apply(types, values, label)


def frameStyle(frame):
    types = ['borderwidth', 'bg', 'highlightbackground', 'highlightthickness']
    values = ['10', 'pink', 'black', 2]
    apply(types, values, frame)


def apply(lt, lv, object):
    for t, v in zip(lt, lv):
        object[t] = v
