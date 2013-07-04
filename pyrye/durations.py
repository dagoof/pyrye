class Duration(int):
    @classmethod
    def from_timedelta(cls, td):
        if hasattr(td, 'total_seconds'):
            return cls(int(td.total_seconds()))
        return cls((td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6)

    def __add__(self, other):
        return Duration(int(self) + other)

    def __sub__(self, other):
        return Duration(int(self) - other)

    def __mul__(self, other):
        return Duration(int(self) * other)

    def __div__(self, other):
        return Duration(int(self) / other)

    def __mod__(self, other):
        return Duration(int(self) % other)

    @property
    def seconds(self):
        return self / Durations.Second

    @property
    def minutes(self):
        return self / Durations.Minute

    @property
    def hours(self):
        return self / Durations.Hour

    @property
    def days(self):
        return self / Durations.Day

    @property
    def weeks(self):
        return self / Durations.Week

    @property
    def months(self):
        return self / Durations.Month

    @property
    def years(self):
        return self / Durations.Year

    @property
    def remaining_seconds(self):
        return self % Durations.Minute / Durations.Second

    @property
    def remaining_minutes(self):
        return self % Durations.Hour / Durations.Minute

    @property
    def remaining_hours(self):
        return self % Durations.Day / Durations.Hour

    @property
    def remaining_days(self):
        return self % Durations.Week / Durations.Day

    @property
    def remaining_weeks(self):
        return self % Durations.Month / Durations.Week

    @property
    def remaining_months(self):
        return self % Durations.Year / Durations.Month

class Durations:
    Second = Duration(1)
    Minute = Second * 60
    Hour   = Minute * 60
    Day    = Hour   * 24
    Week   = Day    * 7
    Month  = Week   * 4
    Year   = Month  * 12

