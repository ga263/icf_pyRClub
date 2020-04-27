# -*- coding: utf-8 -*-

long_list_of_string_numbers = list(range(100000000))

a = sum([float(x) for x in long_list_of_string_numbers])
b = sum(float(x) for x in long_list_of_string_numbers)

assert a == b
