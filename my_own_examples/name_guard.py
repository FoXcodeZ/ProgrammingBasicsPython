# Suppose this is foo.py.


print("before import")


import math


print("before function_a")


def function_a():
    print("Function A")


print("before function_b")


def function_b():
    print("Function B {}".format(math.sqrt(100)))


print("before __name__ guard")
# This code will be executed ONLY when this is a main script.
# Script loaded from other script will be named with script name instead of __main__.
# For example:
# __name__ for script "foo.py" loaded from another script will be "foo".
# __name__ for main script (1st executed script) will be "__main__".
if __name__ == '__main__':
    function_a()
    function_b()
print("after __name__ guard")
