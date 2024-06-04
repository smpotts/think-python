from datetime import datetime


class Time:
    """Represents the time of day.
    """

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def print_time(self):
        time_string = '%.2d:%.2d:%.2d' % (self.hours, self.minutes, self.seconds)
        print(time_string)
        return time_string

    @staticmethod
    def is_after(t1, t2):
        time_format = "%H:%M:%S"
        t1_time = datetime.strptime(t1.print_time(), time_format).time()
        t2_time = datetime.strptime(t2.print_time(), time_format).time()
        return t1_time > t2_time

    @staticmethod
    def time_to_int(time):
        minutes = time.hours * 60 + time.minutes
        seconds = minutes * 60 + time.seconds
        return seconds

    @staticmethod
    def int_to_time(seconds):
        time = Time()
        minutes, time.seconds = divmod(seconds, 60)
        time.hours, time.minutes = divmod(minutes, 60)
        return time

    @staticmethod
    def add_time(t1, t2):
        seconds = Time.time_to_int(t1) + Time.time_to_int(t2)
        return Time.int_to_time(seconds)


