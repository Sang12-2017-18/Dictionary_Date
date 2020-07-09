import unittest
import date_dict as dd

class TestDateDict(unittest.TestCase):

	def test_check_diff(self):
		self.assertEqual(dd.checkDiff((2019,1,1),(2019,1,2)) == 2, True)
		self.assertEqual(dd.checkDiff((2019,2,3),(2019,3,4)) == 1, True)
		self.assertEqual(dd.checkDiff((2019,1,3),(2020,10,20)) == 0, True)

	def test_convert_str(self):
		self.assertEqual(dd.convertStr(9) == "09", True)
		self.assertEqual(dd.convertStr(20) == "20", True)
		self.assertEqual(dd.convertStr(-2) == "NUll", True)

	def test_leap_year(self):
		self.assertTrue(dd.leapYear(2000))
		self.assertFalse(dd.leapYear(1900))
		self.assertTrue(dd.leapYear(2016))
		self.assertFalse(dd.leapYear(2002))

	def test_count_Days(self):
		self.assertEqual(dd.countDays((2019,1,2),(2019,1,10)) == 8, True)
		self.assertEqual(dd.countDays((2019,2,3),(2019,2,3)) == 0,True)
		self.assertEqual(dd.countDays((2019,2,3),(2019,1,2)) == -32,True)

	def test_solution(self):
		D1={'2018-12-25':10,'2019-01-05':21}
		D2={'2018-12-25': 10, '2018-12-26': 11, '2018-12-27': 12, '2018-12-28': 13, '2018-12-29': 14, '2018-12-30': 15, '2018-12-31': 16, '2019-01-01': 17, '2019-01-02': 18, '2019-01-03': 19, '2019-01-04': 20, '2019-01-05': 21}
		self.assertEqual(dd.solution(D1)==D2,True)
		D1={'2019-01-25':10,'2019-01-31':21}
		D2={'2019-01-25': 10, '2019-01-26': 12, '2019-01-27': 14, '2019-01-28': 16, '2019-01-29': 17, '2019-01-30': 19, '2019-01-31': 21}
		self.assertEqual(dd.solution(D1)==D2,True)
		D1={'2019-01-25':10, '2019-02-03':20}
		D2={'2019-01-25': 10, '2019-01-26': 11, '2019-01-27': 12, '2019-01-28': 13, '2019-01-29': 14, '2019-01-30': 16, '2019-01-31': 17, '2019-02-01': 18, '2019-02-02': 19, '2019-02-03': 20}
		self.assertEqual(dd.solution(D1)==D2,True)


if __name__ == '__main__':
	unittest.main()
