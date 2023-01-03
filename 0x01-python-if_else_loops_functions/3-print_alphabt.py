#!/usr/bin/python3
for i in range(97, 123):
    c = chr(i)
    if c == 'e' or c == 'q':
        continue
    print('{}'.format(c), end='')
