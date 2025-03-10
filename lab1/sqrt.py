#!/usr/bin/env python3

import sys
import math

try:
    num=float(sys.stdin.read().strip())
    
    if num<0:
        raise ValueError("Wrong Value!")
    
    sq=math.sqrt(num)
    
    with open("output.txt", "w") as output_f:
        output_f.write(f"{sq}\n")
        
    with open("logs.txt", "a") as log:
        log.write(f"num = {num}\n")
        
    with open("logs.txt", "a") as log:
        log.write(f"sqrt = {sq}\n")
    
except Exception as e:
    with open("errors.txt", "a") as error:
        error.write(f"Error: {str(e)}\n")
    

