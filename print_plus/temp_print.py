from time import sleep


class TempPrint:

    def __init__(self, time_to_print: int = 1):
        self.time_to_print = time_to_print


    def print(self, text: str, time_to_print: int = None):
        print(text, end='')
        sleep(time_to_print or self.time_to_print)
        print('\b' * len(text), end='', flush=True)


    def print_list(self, text_list: str, time_to_print: int = None):
        for text in text_list:
            self.print(text, time_to_print)
