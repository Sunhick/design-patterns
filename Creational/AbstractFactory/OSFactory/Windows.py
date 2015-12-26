from Interfaces import Button, Label, WindowFrame, GuiFactory


class WindowsButton(Button):
    def paint(self):
        print('This is a {name}'.format(name=type(self).__name__))


class WindowsLabel(Label):
    def __init__(self, name):
        self.Name = name

    def paint(self):
        print('This is a {name} with label = {label}'.
              format(name=type(self).__name__, label=self.Name))


class WindowsFrame(WindowFrame):
    def paint(self):
        print('This is a {name}'.format(name=type(self).__name__))


class WindowsFactory(GuiFactory):
    def create_button(self):
        return WindowsButton()

    def create_window(self):
        return WindowsFrame()

    def create_label(self, name):
        return WindowsLabel(name)
