#!/usr/bin/env python3
def outer():
    x = 1
    def inner():
        nonlocal x
        x += 1 
        print("inner:", x)
    inner()
    print("outer:", x)

if __name__ == '__main__':
  outer()
