#!/usr/bin/python3
""" A script to determines if a given data
    set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    count = 0
    for byte in data:
        if count == 0:
            # Check leading byte
            mask = 0x80
            while (byte & mask) != 0:
                count += 1
                mask >>= 1
            if count == 0:
                continue
            if count > 4 or count == 1:
                return False
        else:
            # Check continuation byte
            if (byte & 0xC0) != 0x80:
                return False
        count -= 1

    return count == 0
