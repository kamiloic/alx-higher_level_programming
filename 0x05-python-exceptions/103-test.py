#!/usr/bin/python3 -u

import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]
s = b"Hello"
lib.print_python_bytes(s)
b = b'\xff\xf8\x00\x00\x00\x00\x00\x00'
lib.print_python_bytes(b)
b = b'What does the \'b\' character do in front of a string literal?'
lib.print_python_bytes(b)
_list = [b'Hello', b'World']
lib.print_python_list(_list)
del _list[1]
lib.print_python_list(_list)
_list = _list + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"School", "Betty"]
lib.print_python_list(_list)
_list = []
lib.print_python_list(_list)
_list.append(0)
lib.print_python_list(_list)
_list.append(1)
_list.append(2)
_list.append(3)
_list.append(4)
lib.print_python_list(_list)
_list.pop()
lib.print_python_list(_list)
_list = ["School"]
lib.print_python_list(_list)
lib.print_python_bytes(_list)
f = 3.14
lib.print_python_float(f)
_list = [-1.0,
         -0.1,
         0.0,
         1.0,
         3.14,
         3.14159,
         3.14159265,
         3.141592653589793238462643383279502884197169399375105820974944592]
print(_list)
lib.print_python_list(_list)
lib.print_python_float(_list)
lib.print_python_list(f)
