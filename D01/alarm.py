#!/bin/python3

def SQUEAK(func, purse=None):
    def squeak(*args, **kwargs):
        print("SQUEAK!")
        return func(*args, **kwargs)
    return squeak
