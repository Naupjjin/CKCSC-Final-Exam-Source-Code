import urllib.parse
def useless (file_param):
    file_param1 = ignore_it(file_param)
    file_param2 = another_useless_function(file_param1)
    file_param3 = ignore_it(file_param2)
    file_param4 = another_useless_function(file_param3)
    file_param5 = another_useless_function(file_param4)
    return file_param5

def another_useless_function(file_param):
    return urllib.parse.unquote(file_param)

def ignore_it(file_param):
    yoooo = file_param.replace('.', '').replace('/', '')
    if yoooo != file_param:
        return "Illegal characters detected in file parameter!"
    return yoooo

a=urllib.parse.quote("%2E%2E%2Fflag%2Etxt")
b=urllib.parse.quote(a)
print(b)
print(useless(b))