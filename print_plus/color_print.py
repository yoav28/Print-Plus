class ColorPrint:

    def print(self, text, color=None, background=None, end='\n'):
        if color is None and background is None:
            return print(text)

        if color is None:
            return print(f'\033[0;{self._background_list[background]}m{text}\033[0m', end=end)

        if background is None:
            return print(f'\033[0;{self._color_list[color]}m{text}\033[0m', end=end)

        color_code = self._color_list[color]
        background_code = self._background_list[background]
        print(f'\033[{color_code};{background_code}m{text}\033[0m', end=end)


    @property
    def _color_list(self):
        return {
            "black": 30,
            "red": 31,
            "green": 32,
            "yellow": 33,
            "blue": 34,
            "magenta": 35,
            "cyan": 36,
            "white": 37,
            "gray": 90,
            "light_red": 91,
            "light_green": 92,
            "light_yellow": 93,
            "light_blue": 94,
            "light_magenta": 95,
            "light_cyan": 96,
            "light_white": 97
        }


    @property
    def _background_list(self):
        return {
            "black": 40,
            "red": 41,
            "green": 42,
            "yellow": 43,
            "blue": 44,
            "magenta": 45,
            "cyan": 46,
            "white": 47,
            "gray": 100,
            "light_red": 101,
            "light_green": 102,
            "light_yellow": 103,
            "light_blue": 104,
            "light_magenta": 105,
            "light_cyan": 106,
            "light_white": 107
        }


    def all_colors(self):
        for color in self._color_list:
            self.print(color, color=color, end=', ')

        print()


    def all_backgrounds(self):
        for background in self._background_list:
            self.print(background, background=background, end=', ')

        print()
