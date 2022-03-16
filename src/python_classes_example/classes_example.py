class example:
    def __init__(self):
        self.first_name = input('What is your first name?')
        self.last_name = input('What is your last name?')
        self.how_are_you = input('How are you?')
        self.age = int(input('How old are you?'))
        self.tell_name() # Runs the "tell_name" method witin the class
    def tell_name(self):
        print('your first name is {}'.format(self.first_name))
        print('your last name is ' + self.last_name)
    def tell_how_are_you(self):
        print('you are ' + self.how_are_you)
    def tell_age(self):
        print('you are {} years old'.format(self.age))

example_class = example() # Runs the "__init__" method within the class
example_class.tell_how_are_you() # Runs the "tell_how_are_you" method witin the class
example_class.tell_age() # Runs the "tell_age" method witin the class
