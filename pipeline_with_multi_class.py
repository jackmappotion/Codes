class MY_CLASS:
    class LETTER_1:
        @staticmethod
        def print_hello():
            print("HELLO")

        @staticmethod
        def print_JACK():
            print("JACK")

        def __call__(self):
            self.print_hello()
            self.print_JACK()

    class LETTER_2:
        @staticmethod
        def print_hello():
            print("HELLO")

        @staticmethod
        def print_DARM():
            print("DARM")

        def __call__(self):
            self.print_hello()
            self.print_DARM()

    def __call__(self):
        letter_1 = self.LETTER_1()
        letter_2 = self.LETTER_2()
        letter_1()
        print("==")
        letter_2()

my_class=MY_CLASS()
my_class()
