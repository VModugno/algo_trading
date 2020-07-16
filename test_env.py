# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 21:11:57 2020

@author: alfre
"""
from os import getenv

IEX_CLOUD_API_TOKEN = getenv("IEX_CLOUD_API_TOKEN", "<IEX_CLOUD_API_TOKEN>")

print(IEX_CLOUD_API_TOKEN.strip("'"))