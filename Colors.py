class Color:
    def __init__(self) -> None:
        self.CEND    = '\33[0m'
        self.CBLACK  = '\33[30m'
        self.CRED    = '\33[31m'
        self.CGREEN  = '\33[32m'
        self.CYELLOW = '\33[33m'
        self.CBLUE   = '\33[34m'
        self.CVIOLET = '\33[35m'

    def print_green(self, string):
        print(self.CGREEN + string + self.CEND) 

    def print_red(self, string):
        print(self.CRED + string + self.CEND) 

    def print_blue(self, string):
        print(self.CBLUE + string + self.CEND)          