#Cette classe permet d'appliquer facilement un theme global a des widgets

def rootStyle(root) :
    root.geometry('500x250')
    root.configure(background='gray')

def buttonStyle(button) :
    types = ['bg', 'fg', 'activeforeground', 'activebackground', 'borderwidth']
    values = ['black', 'pink', 'black', 'pink', 3]
    apply(types, values, button)

def checkButtonStyle(checkButton) :
    buttonStyle(checkButton)
    types = ['selectcolor']
    values = ['gray']
    apply(types, values, checkButton)

def labelStyle(label) :
    types = ['bg', 'fg', 'borderwidth', 'relief']
    values = ['black', 'pink', 2, 'sunken']
    apply(types, values, label)

def frameStyle(frame) :
    types = ['borderwidth', 'bg']
    values = ['10', 'pink']
    apply(types, values, frame)

def apply(lt, lv, object) :
    for t, v in zip(lt, lv) :
        object[t] = v