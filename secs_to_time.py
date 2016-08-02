import unittest


def secs_to_time(seconds):
    MIN = 60
    HOUR = 60*60
    time = "00:00:00"
    hour = seconds // HOUR
    minute = (seconds - hour*HOUR) // MIN
    sec = seconds - hour*HOUR - minute*MIN
    if sec < 10:
        sec = '0' + str(sec)
    if minute < 10:
        minute = '0' + str(minute)
    if hour < 10:
        hour = '0' + str(hour)
    return "{}:{}:{}".format(hour, minute, sec)


class SecsToTimeTest(unittest.TestCase):
    def test_one(self):
        time = secs_to_time(0)
        self.assertEqual(time, "00:00:00")

    def test_two(self):
        time = secs_to_time(60)
        self.assertEqual(time, "00:01:00")

    def test_three(self):
        time = secs_to_time(65)
        self.assertEqual(time, "00:01:05")

    def test_four(self):
        time = secs_to_time(3665)
        self.assertEqual(time, "01:01:05")

    def test_one(self):
        time = secs_to_time(86399)
        self.assertEqual(time, "23:59:59")

    def test_one(self):
        time = secs_to_time(359999)
        self.assertEqual(time, "99:59:59")

def main():
    unittest.main()

if __name__ == '__main__':
    main()