# -*- coding: utf-8 -*-
"""64se64.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FIgcjBN57dxDv2rZ1YlMGtwm4lX6lD1R
"""

import base64

encoded_data = "IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwphc2M9WzY4LCA3MiwgMTIzLCA5OCwgMTAxLCA0OCwgNTIsIDU0LCA5OCwgNTUsIDUzLCA1MCwgNTAsIDk3LCA5NywgNTAsIDEwMSwgNTAsIDU2LCAxMDIsIDUwLCA1NSwgNTQsIDEwMSwgNDgsIDk5LCA1NywgNDksIDQ4LCA1MywgNTAsIDQ5LCAxMDIsIDUwLCA1MSwgOTcsIDQ4LCA1MywgNTYsIDU1LCA0OCwgNDgsIDUzLCA5NywgNTYsIDUxLCA1NSwgNTUsIDUxLCA1NSwgNDgsIDk3LCA0OSwgNDksIDEwMSwgNTMsIDEwMSwgNTIsIDEwMCwgOTksIDQ5LCA1MywgMTAyLCA5OCwgNTAsIDk3LCA5OCwgMTI1XQphcnI9WzAgZm9yIGkgaW4gcmFuZ2UoNjgpXQpmb3IgaSBpbiByYW5nZSgwLDY4KToKICAgIGFycltpXT1jaHIoYXNjW2ldKQpmbGFnPScnLmpvaW4oYXJyKQpwcmludChmbGFnKQ=="

decoded_data = base64.b64decode(encoded_data).decode('utf-8')

print(decoded_data)

#!/usr/bin/env python3
asc=[68, 72, 123, 98, 101, 48, 52, 54, 98, 55, 53, 50, 50, 97, 97, 50, 101, 50, 56, 102, 50, 55, 54, 101, 48, 99, 57, 49, 48, 53, 50, 49, 102, 50, 51, 97, 48, 53, 56, 55, 48, 48, 53, 97, 56, 51, 55, 55, 51, 55, 48, 97, 49, 49, 101, 53, 101, 52, 100, 99, 49, 53, 102, 98, 50, 97, 98, 125]
arr=[0 for i in range(68)]
for i in range(0,68):
    arr[i]=chr(asc[i])
flag=''.join(arr)
print(flag)