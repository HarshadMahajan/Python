#!/usr/bin/env python

import string

str = raw_input()
print ' '.join(map(string.capitalize, str.split(' ')))