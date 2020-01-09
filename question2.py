class string_check():
    # Initialization of class
    def __init__(self, string_1, string_2):
        '''
        
        '''
        self.str1 = string_1
        self.str2 = string_2

    def length(self):
        if len(self.str1) == len(self.str2):
            return "Both are equal string"
        elif len(self.str1) < len(self.str2):
            return "String 2 is large"
        else:
            return "String 1 is large"

    def isequal(self):
        if self.str1 == self.str2:
            return "Both string are equal"
        else:
            return "Both string are not equal"

    def stringvaluecheck(self):
        if self.str1 < self.str2:
            return "String 2 value is large"
        else:
            return "String 1 value is large"

    def valuecheck(self):
        if self.str1 is self.str2:
            return True
        else:
            return False

'''
Usage: It is class. We can use noramlly by creating object of specific class.

Example:
string1 = "122345"
string2 = "344567"

test1 = string_check(string1, string2)
test1.isequal()
test1.length()
test1.stringvaluecheck()
test1.valuecheck()
'''