from Interfaces import Button, Label, WindowFrame, GuiFactory


class OsxButton(Button):
    def paint(self):
        print('This is a {name}'.format(name=type(self).__name__))


class OsxLabel(Label):
    def __init__(self, name):
        self.Name = name

    def paint(self):
        print('This is a {name} with label = {label}'.
              format(name=type(self).__name__, label=self.Name))


class OsxFrame(WindowFrame):
    def paint(self):
        print('This is a {name}'.format(name=type(self).__name__))


class OsxFactory(GuiFactory):
    def create_button(self):
        return OsxButton()

    def create_window(self):
        return OsxFrame()

    def create_label(self, name):
        return OsxLabel(name)
