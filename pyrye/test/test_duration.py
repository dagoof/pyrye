import unittest
import pyrye

class DurationTests(unittest.TestCase):
    def test_from_timedelta(self):
        import datetime

        td = datetime.timedelta(days = 1)
        self.assertEqual(pyrye.Durations.Day, pyrye.Duration.from_timedelta(td))

    def test_to_timedelta(self):
        import datetime

        dt_day = datetime.timedelta(days = 1)
        rye_day = pyrye.Durations.Day
        self.assertEqual(rye_day.timedelta, dt_day)

    def test_seconds(self):
        n = 72
        d = pyrye.Durations.Second * n

        self.assertEqual(d.seconds, n)
        self.assertEqual(d.minutes, 1)
        self.assertEqual(d.remaining_seconds, n - pyrye.Durations.Minute.seconds)

        self.assertEqual(pyrye.Durations.Second, 1)


    def test_minutes(self):
        n = 72
        d = pyrye.Durations.Minute * n

        self.assertEqual(d.minutes, n)
        self.assertEqual(d.hours, 1)
        self.assertEqual(d.remaining_minutes, n - pyrye.Durations.Hour.minutes)

        self.assertEqual(pyrye.Durations.Minute, pyrye.Durations.Second * 60)


    def test_hours(self):
        n = 32
        d = pyrye.Durations.Hour * n

        self.assertEqual(d.hours, n)
        self.assertEqual(d.days, 1)
        self.assertEqual(d.remaining_hours, n - pyrye.Durations.Day.hours)

        self.assertEqual(pyrye.Durations.Hour, pyrye.Durations.Minute * 60)


    def test_days(self):
        n = 9
        d = pyrye.Durations.Day * n

        self.assertEqual(d.days, n)
        self.assertEqual(d.weeks, 1)
        self.assertEqual(d.remaining_days, n - pyrye.Durations.Week.days)

        self.assertEqual(pyrye.Durations.Day, pyrye.Durations.Hour * 24)


    def test_weeks(self):
        n = 6
        d = pyrye.Durations.Week * n

        self.assertEqual(d.weeks, n)
        self.assertEqual(d.months, 1)
        self.assertEqual(d.remaining_weeks, n - pyrye.Durations.Month.weeks)

        self.assertEqual(pyrye.Durations.Week, pyrye.Durations.Day * 7)


    def test_months(self):
        n = 18
        d = pyrye.Durations.Month * n

        self.assertEqual(d.months, n)
        self.assertEqual(d.years, 1)
        self.assertEqual(d.remaining_months, n - pyrye.Durations.Year.months)

        self.assertEqual(pyrye.Durations.Month, pyrye.Durations.Week * 4)


    def test_years(self):
        n = 2
        d = pyrye.Durations.Year * n

        self.assertEqual(d.years, n)
        self.assertEqual(pyrye.Durations.Year, pyrye.Durations.Month * 12)


class RatesTests(unittest.TestCase):

    def test_seconds(self):
        n = 30
        d = pyrye.Durations.Second * n
        self.assertEqual(d.rate, pyrye.Durations.Second)
        self.assertEqual(d.next_rate, pyrye.Durations.Minute)
        self.assertEqual(d.prev_rate, 0)

        n = 72
        d = pyrye.Durations.Second * n
        self.assertEqual(d.rate, pyrye.Durations.Minute)

    def test_minutes(self):
        n = 30
        d = pyrye.Durations.Minute * n
        self.assertEqual(d.rate, pyrye.Durations.Minute)
        self.assertEqual(d.next_rate, pyrye.Durations.Hour)
        self.assertEqual(d.prev_rate, pyrye.Durations.Second)

        n = 72
        d = pyrye.Durations.Minute * n
        self.assertEqual(d.rate, pyrye.Durations.Hour)

    def test_hours(self):
        n = 12
        d = pyrye.Durations.Hour * n
        self.assertEqual(d.rate, pyrye.Durations.Hour)
        self.assertEqual(d.next_rate, pyrye.Durations.Day)
        self.assertEqual(d.prev_rate, pyrye.Durations.Minute)

        n = 32
        d = pyrye.Durations.Hour * n
        self.assertEqual(d.rate, pyrye.Durations.Day)

    def test_days(self):
        n = 6
        d = pyrye.Durations.Day * n
        self.assertEqual(d.rate, pyrye.Durations.Day)
        self.assertEqual(d.next_rate, pyrye.Durations.Week)
        self.assertEqual(d.prev_rate, pyrye.Durations.Hour)

        n = 9
        d = pyrye.Durations.Day * n
        self.assertEqual(d.rate, pyrye.Durations.Week)

    def test_weeks(self):
        n = 3
        d = pyrye.Durations.Week * n
        self.assertEqual(d.rate, pyrye.Durations.Week)
        self.assertEqual(d.next_rate, pyrye.Durations.Month)
        self.assertEqual(d.prev_rate, pyrye.Durations.Day)

        n = 6
        d = pyrye.Durations.Week * n
        self.assertEqual(d.rate, pyrye.Durations.Month)

    def test_months(self):
        n = 10
        d = pyrye.Durations.Month * n
        self.assertEqual(d.rate, pyrye.Durations.Month)
        self.assertEqual(d.next_rate, pyrye.Durations.Year)
        self.assertEqual(d.prev_rate, pyrye.Durations.Week)

        n = 18
        d = pyrye.Durations.Month * n
        self.assertEqual(d.rate, pyrye.Durations.Year)

    def test_years(self):
        n = 2
        d = pyrye.Durations.Year * n
        self.assertEqual(d.rate, pyrye.Durations.Year)
        self.assertEqual(d.next_rate, 0)
        self.assertEqual(d.prev_rate, pyrye.Durations.Month)

        n = .5
        d = pyrye.Durations.Year * n
        self.assertEqual(d.rate, pyrye.Durations.Month)








