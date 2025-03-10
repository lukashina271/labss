#!/usr/bin/env python3

import sys
import random

try:
    A=int(sys.stdin.readline().strip())
    B=random.randint(-10,10)
    
    if B==0:
        raise ZeroDivisionError("Division by zero!")
    
    res=A/B
    print(res)
    
    with open("logs.txt", "a") as log:
        log.write(f"A = {A}, B = {B}, A/B = {res}\n")
        
except Exception as e:
    with open("errors.txt", "a") as error:
        error.write(f"Error: {str(e)}\n")
