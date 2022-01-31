name=input('Enter your Name: ')
age=input('Enter your age: ')
clg=input('Enter your Colloege name: ')
pas=input('Enter year of passing: ')

template='''
GREETINS!!!
Student Name: <name>
Age:<age>
College: <clg>
Year of passing: <pas>'''

print(template.replace('<name>',name).replace('<age>',age).replace('<clg>',clg).replace('<pas>',pas))