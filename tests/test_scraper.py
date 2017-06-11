from datetime import datetime
import os
import unittest

from ceeb.scraper import parse


TEST_DIR = os.path.dirname(__file__)


class ScraperTest(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_parser_with_highschool_html(self):
        data_file = os.path.join(TEST_DIR, 'fixtures', 'highschools.html')
        with open(data_file) as f:
            html = f.read()

        poll_time = datetime(2015, 10, 12)
        ceeb_codes = parse(html, poll_time, td_offset=1)

        self.assertEqual(29, len(ceeb_codes))
        obj = {
            'name': 'Young Mothers Education Devel',
            'ceeb_code': '335532',
            'address': {
                'city': 'Syracuse',
                'state': 'NY'
            },
            'date_created': poll_time,
            'date_modified': poll_time,
            'date_deleted': None
        }
        self.assertEqual(obj, ceeb_codes[28])

    def test_parser_with_college_html(self):
        data_file = os.path.join(TEST_DIR, 'fixtures', 'colleges.html')
        with open(data_file) as f:
            html = f.read()

        poll_time = datetime(2015, 10, 12)
        ceeb_codes = parse(html, poll_time)

        self.assertEqual(11, len(ceeb_codes))
        obj = {
            'name': 'SUNY Upstate Medical Univ',
            'ceeb_code': '2547',
            'address': {
                'city': 'Syracuse',
                'state': 'NY'
            },
            'date_created': poll_time,
            'date_modified': poll_time,
            'date_deleted': None
        }
        self.assertEqual(obj, ceeb_codes[6])

    def test_parser_when_no_results(self):
        """Should return an empty list."""
        data_file = os.path.join(TEST_DIR, 'fixtures', 'noresults.html')
        with open(data_file) as f:
            html = f.read()

        poll_time = datetime(2015, 10, 12)
        ceeb_codes = parse(html, poll_time)

        self.assertEqual(0, len(ceeb_codes))


if __name__ == '__main__':
    unittest.main()
