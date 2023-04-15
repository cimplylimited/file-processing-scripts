# Reference: https://docs.python.org/3/library/base64.html

# Security Considerations
# A new security considerations section was added to RFC 4648 (section 12); 
# it’s recommended to review the security section for any code deployed to production.

# See also
# Module binascii
# Support module containing ASCII-to-binary and binary-to-ASCII conversions.

# RFC 1521 - MIME (Multipurpose Internet Mail Extensions) Part One: Mechanisms for Specifying and Describing the Format of Internet Message Bodies
# Section 5.2, “Base64 Content-Transfer-Encoding,” provides the definition of the base64 encoding.



# V.1
# In Python 3.x you need to convert your str object to a bytes object for base64 to be able to encode them. 
# You can do that using the str.encode method:
# If you pass the output of your_str_object.encode('utf-8') to the base64 module, 
# you should be able to encode it fine.

import json
import base64
d = {"alg": "ES256"} 
s = json.dumps(d)  # Turns your json dict into a str
print(s)
{"alg": "ES256"}
type(s)
<class 'str'>
base64.b64encode(s)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.2/base64.py", line 56, in b64encode
    raise TypeError("expected bytes, not %s" % s.__class__.__name__)
TypeError: expected bytes, not str
base64.b64encode(s.encode('utf-8'))
b'eyJhbGciOiAiRVMyNTYifQ=='


#V.2
'''
import json
import base64


with open('test.json') as jsonfile:
    data = json.load(jsonfile)
    print(type(data))  #dict
    datastr = json.dumps(data)
    print(type(datastr)) #str
    print(datastr)
    encoded = base64.b64encode(datastr.encode('utf-8'))  #1 way
    print(encoded)

    print(base64.encodebytes(datastr.encode())) #2 method
'''