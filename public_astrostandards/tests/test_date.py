import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import public_astrostandards
from public_astrostandards import helpers

def test_dates():
    from datetime import datetime, timezone, timedelta
    now = datetime.now( timezone.utc )
    ds = now.strftime('%y%j%H%M%S.%f')[:-3]

    x = public_astrostandards.TimeFuncDll.DTGToUTC(  helpers.Cstr( ds,20 ) )
    #epoch = datetime.strptime( '1950-01-01T00:00:00', "%Y-%m-%dT%H:%M:%S")
    epoch = datetime.strptime( '1949-12-31T00:00:00', "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)

    def get_days_between(datePast, dateFuture):
        difference = dateFuture - datePast
        return difference.total_seconds() / timedelta(days=1).total_seconds()
    
    print('-------------- TIME TEST -------------')
    print('Now :            : {}'.format(now.isoformat()))
    print('Test date string : {}'.format(ds) )
    print('AstroStd answer  : {}'.format(x) )
    print('Python answer    : {}'.format( get_days_between( epoch, now ) ) )
    print('Difference (s)   : {}'.format( 86400. * (x - get_days_between( epoch, now ) ) ) )
    print('-------------- TIME TEST -------------')
    
if __name__ == '__main__':
    test_dates()