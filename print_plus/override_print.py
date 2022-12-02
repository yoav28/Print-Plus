from sys import stdout


class PrintOverride:

    def __init__(self, disable_print: bool = False):
        self._print_history = []
        self._original_stdout = stdout.write
        self.disable_print = disable_print
        stdout.write = self


    def __call__(self, *args):
        self._print_history.append(*args)

        if not self.disable_print:
            self.stdout(*args)


    def __str__(self):
        return ''.join(self._print_history)


    def __del__(self):
        stdout.write = self._original_stdout


    def stdout(self, *args):
        self._original_stdout(*args)


    def to_file(self, file_name: str):
        with open(file_name, 'w') as file:
            for args in self._print_history:
                file.write(''.join(args))


    def clear(self):
        self._print_history = []


    def print_history(self):
        self.stdout(*self._print_history)


    def flush(self):
        pass
