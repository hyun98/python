class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def is_time_valid(string):
        hour, minute, second = map(int, string.split(':'))
        if hour < 0 or hour > 24:
            return False
        elif minute < 0 or minute > 59:
            return False
        elif second < 0 or second > 60:
            return False
        else:
            return True
    
    def from_string(tstring):
        hour, minute, second = map(int, tstring.split(':'))
        time = Time(hour, minute, second)
        return time

time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')