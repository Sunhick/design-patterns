class GuiApplication(object):
    """ GUI Appication """
    def __init__(self, factory):
        self._factory = factory

    def _show_login(self):
        window = self._factory.create_window()
        password_label = self._factory.create_label('Password')
        okbutton = self._factory.create_button()

        window.add(password_label)
        window.add(okbutton)
        window.show()

    def run(self):
        self._show_login()
