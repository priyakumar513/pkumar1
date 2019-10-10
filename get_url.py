# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:39:24 2019

@author: pkuma
"""
def get_url(text):
    """To extract the url from html source code."""
    url_start = "<a href="
    if url_start in text: 
        pos1 = text.find(url_start) 
        start_index=text.find('"', pos1)
        end_index=text.find('"', start_index+1)
        url = text[start_index+1: end_index]
        return url 
    else: 
        return -1 