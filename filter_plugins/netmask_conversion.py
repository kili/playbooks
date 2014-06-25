def len2mask(len):

    """Convert a bit length to a dotted netmask (aka. CIDR to netmask)"""
    mask = ''
    if not isinstance(len, int) or len < 0 or len > 32:
        print "Illegal subnet length: %s (which is a %s)" % \
            (str(len), type(len).__name__)
        return None

    for t in range(4):
        if len > 7:
            mask += '255.'
        else:
            dec = 255 - (2**(8 - len) - 1)
            mask += str(dec) + '.'
        len -= 8
        if len < 0:
            len = 0

    return mask[:-1]


def mask2len(subnet):
    """Convert a dotted netmask to bit length (aka. netmask to CIDR)"""

    octets = [int(x) for x in subnet.split(".")]
    count = 0
    for octet in octets:
        highest_bit = 128
        while highest_bit > 0:
            if octet >= highest_bit:
                count = count + 1
                octet = octet - highest_bit
                highest_bit = highest_bit / 2
            else:
                return count
    return count


class FilterModule(object):
    ''' utility to convert cidr netmasks into len and reverse '''

    def filters(self):
        return {'mask2len': mask2len,
                'len2mask': len2mask}
