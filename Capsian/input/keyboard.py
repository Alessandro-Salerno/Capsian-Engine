
from   Capsian.components.component import Component
from   pyglet.window                import key       as Key
import Capsian.engine                                as engine


class KeyboardInputHandler(Component):
    """
    Fields
    ------
        pressed_key       | The currently pressed key (key held) | Pyglet Key State Handler
        key_state_handler | The Key State Handler for the object | CapsianKeyStateHandlerObject

    Methods
    -------
        on_key_pressed  | What happens when a key is pressed
        on_key_released | What happens when a key is released
        on_key_held     | What happens when a key is held down
    """


    # -------------------------
    #
    #       DUNDERSCORE
    #
    # -------------------------

    def __init__(self):
        class CapsianKeyStateHandlerObject(Key.KeyStateHandler):
            def __init__(self, parent):
                self.parent = parent
                super().__init__()

            def on_key_press(self, symbol, modifiers):
                self.parent.on_key_pressed(symbol, modifiers)

            def on_key_release(self, symbol, modifiers):
                self.parent.on_key_released(symbol, modifiers)

            def __eq__(self, value):
                return self.get(value)


        self.pressed_key       = Key.KeyStateHandler()
        self.key_state_handler = CapsianKeyStateHandlerObject(self)

        engine.main_window.push_handlers(self.pressed_key)
        engine.main_window.push_handlers(self.key_state_handler)

        super().__init__()
    

    def __repr__(self):
        return "key_listener"


    # -------------------------
    #
    #       PUBLIC METHODS
    #
    # -------------------------

    def on_key_pressed(self, symbol, modifiers):
        """
        Parameters
        ----------
            symbol    | The key that has been pressed
            modifiers | The modifiers that are applied
        """

        pass


    def on_key_released(self, symbol, modifiers):
        """
        Parameters
        ----------
            symbol    | The key that has been pressed
            modifiers | The modifiers that are applied
        """

        pass


    def on_key_held(self, keys):
        """
        Parameters
        ----------
            keys | The keys that have been pressed | dict
        """

        pass


    # -------------------------
    #
    #       EVENT HANDLERS
    #
    # -------------------------

    def on_update(self, dt, time):
        self.on_key_held(self.pressed_key)

