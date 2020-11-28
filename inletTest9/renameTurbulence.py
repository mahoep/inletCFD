# -*- coding: utf-8 -*-
"""
Created on Fri Nov  13 12:15:10 2020

@author: mahoep
"""

"""
The turbulenceProperites field function object names the files with ':'.
Ex   (turbulenceProperites:I) which is an invalid character in windows file system.
This small script renames all instances of it.
"""

import os
substring = 'turbulence'
field = ['I','L']

for k in field:
    for root, dirs, files in os.walk("./"):
        for file in files:
            if substring in file and k in file:
                newFile = 'turbulenceProperties.'+k
                os.rename(os.path.join(root,file),os.path.join(root,newFile))