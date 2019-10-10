# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:26:42 2019

@author: pkuma
"""
def make_triangle(triangle_char, triangle_height):
    """To create an isoceles triangle with the inputted triangle height using the characters."""
    triangle_string = ''
    for i in range(triangle_height):
        for j in range(i+1): 
            triangle_string+=(triangle_char + ' ')
        triangle_string+=('\n')   
    return triangle_string  
print(make_triangle('%',5))