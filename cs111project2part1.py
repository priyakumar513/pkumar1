# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:39:24 2019

@author: pkuma
"""
def print_all_links(text):
    """To extract the url from html source code."""
    url_start = "<a href="
    ahref_is_there=1 
    current_index=0 
    ahref_is_there= text.find(url_start, current_index)
    while ahref_is_there !=-1: 
        ahref_is_there= text.find(url_start, current_index+1)
        if ahref_is_there >= 0 : 
            start_index=text.find('"', ahref_is_there)
            end_index=text.find('"', start_index+1)
            url = text[start_index+1: end_index]
            print (url)
            current_index=end_index
        #if ahref_is_there <= 0 :
            #break
webpage_source = input()

print_all_links(webpage_source)  
