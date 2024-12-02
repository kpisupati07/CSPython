class Clock:
    def __init__(self, hours, minutes):
        if not ( 1<= hours <= 23):
            raise ValueError ("Hours should be between 1 and 23")
        if not (0<= minutes<=59):
            raise ValueError("Min should be between 0 and 59")
        self.__hours = hours
        self.minutes = minutes
    def __str__(self):
        am_pm = 'AM' if self.hours < 12 else 'PM'
        hours = self.hours % 12
        if hours == 0:
            hours = 12
        return (f'The time is {hours}{self.minutes}{am_pm')