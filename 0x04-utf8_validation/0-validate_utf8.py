#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data) -> bool:
    """ Check valid utf8"""
    num_bytes = 0

    for bytes in data:
        mask = 1 << 7
        if not num_bytes:
            while bytes & mask:
                num_bytes = num_bytes + 1
                mask >>= 1
            if not num_bytes:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if bytes >> 6 != 0b10:
                return False
        num_bytes -= 1
    return num_bytes == 0