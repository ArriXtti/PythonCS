fruits = ['apples', 'bananas', 'peaches', 'grapes']
separator = ' and I like '
joined = separator.join(fruits)
print('I like', joined)

alphabet = "abcde"  # a string iterable
abc = ("aa", 'bb', 'cc')  # a tuple iterable
aboutPython = ["Python", "programming language"]  # a list iterable
plus = " + "
dual = " = "
print(plus.join(alphabet))  # join with the ' + ' separator
print(dual.join(abc))  # join with the ' = ' separator

sep = ' is a '
print(sep.join(aboutPython))  # join with the ' is a ' separator
