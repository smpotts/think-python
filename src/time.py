class Time:
    """Represents the time of day.
    """

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hours, self.minutes, self.seconds)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(self, other)
        else:
            return self.increment(other)

    def print_time(self):
        time_string = '%.2d:%.2d:%.2d' % (self.hours, self.minutes, self.seconds)
        return time_string

    def time_to_int(self):
        minutes = self.hours * 60 + self.minutes
        seconds = minutes * 60 + self.seconds
        return seconds

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def increment(self, seconds):
        seconds += self.time_to_int()
        return self.int_to_time(seconds)

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


