def test_args_kwargs(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

args = ("two", 3, 5)
test_args_kwargs(*args)

def test_args_1(*argv):
    for arg in argv:
        print "arg from argv", arg

test_args_1('1','2')

def test_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg from argv:", arg

test_args('1','2','3')

def test_kwargs(**kwargs):
    for key, value in kwargs.items():
        print "{0} == {1}".format(key, value)

kwargs = {"arg3": 3,"arg2": "two"}
test_kwargs(**kwargs)

