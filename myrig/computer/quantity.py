class Quantity(object):
    '''
    Represents a positive integer quantity
    '''
    
    _PREFIXES = {
        10**3:  'k',
        10**6:  'M',
        10**9:  'G',
        10**12: 'T',
    }
    
    def __init__(self, value, unit):
        '''
        Initializes the quantity
        '''
        self._value, self._unit = value, unit
    
    def __int__(self):
        '''
        Returns the integer value of the quantity
        '''
        return self._value
    
    def __unicode__(self):
        '''
        Returns a string representation of the quantity
        '''
        if self._value < 10**3:
            return '%d %s' % (
                self._value,
                self._unit,
            )
        else:
            v, d = float(self._value), 1
            while v / 10**3 >= 1 and d <= 10**12:
                d *= 10**3
                v /= 10**3
            return '%.1f %s%s' % (
                v,
                self._PREFIXES[d],
                self._unit,
            )
