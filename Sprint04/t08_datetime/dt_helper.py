import datetime, pytz

def create_datetime(*args, **kwargs):

    if 'timezone_str' in kwargs.keys() : #kwargs and
        timezone = pytz.timezone(kwargs.get('timezone_str'))
        result = timezone.localize(datetime.datetime(*args))
    else:
        timezone = None #LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        result = datetime.datetime(*args)
    return  result#datetime.datetime(*args).astimezone(timezone)

def print_formatted_datetime(dtime_in, format_in):
    print(dtime_in.strftime(format_in))
#    return None

def print_difference(dtime_in1, dtime_in2, *timezone_in):

    if not timezone_in :
        result = dtime_in1.replace(tzinfo=None) - dtime_in2.replace(tzinfo=None)
    else:
        tz = pytz.timezone(timezone_in)
        result = dtime_in1.astimezone(tz) - dtime_in2.astimezone(tz)# timedelta
    print(result)
#    return None

if __name__ == '__main__':

    ukraine_timezone= 'Etc/GMT+3'
    datetime_1= create_datetime(2015, 5, 21, 12, 0)
    #print(datetime_1)
    datetime_2= create_datetime(2016, 6, 14, 3, 0, timezone_str='Asia/Shanghai')
    #print(datetime_2)
    datetime_3= create_datetime(2016, 6, 14, 3, 0, timezone_str=ukraine_timezone)
    #print(datetime_3)
    datetime_1_format= '%d.%m.%y %H:%M:%S'
    datetime_2_format= '%y-%m-%d %H:%M'
    datetime_3_format= '%y : %H, %M, %S'

    print_formatted_datetime(datetime_1, datetime_1_format)
    print_formatted_datetime(datetime_2, datetime_2_format)
    print_formatted_datetime(datetime_3, datetime_3_format)

    print_difference(datetime_1, datetime_1)
    print_difference(datetime_3, datetime_2)
    print_difference(datetime_1, datetime_3)
    print_difference(datetime_3, datetime_1)