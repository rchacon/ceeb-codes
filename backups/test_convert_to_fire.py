import json
import unittest

from convert_to_fire import convert_schools


testdata = [
    json.dumps({'address': {'city': 'Oakland', 'state': 'CA'},
                'name': 'Skyline', 'ceeb_code': '123'}),
    json.dumps({'address': {'city': 'Oakland', 'state': 'CA'},
                'name': 'Oakland High', 'ceeb_code': '456'}),
    json.dumps({'address': {'city': 'Alameda$   ', 'state': 'CA'},
                'name': 'Alameda High', 'ceeb_code': '789'}),
    json.dumps({'address': {'city': 'St. Paul', 'state': 'NY'},
                'name': 'Syracuse High', 'ceeb_code': '10'}),
    json.dumps({'address': {'city': '', 'state': 'CA'},
                'name': 'St. Joseph Notre Dame', 'ceeb_code': '10'})
]


class TestConvertToFire(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_convert_schools(self):
        result = convert_schools(testdata, 'college')

        self.assertEqual(result, {
            'CA_college': {
                u'Oakland': [
                    {'name': u'Skyline', 'code': u'123'},
                    {'name': u'Oakland High', 'code': u'456'}
                ],
                u'Alameda': [
                    {'name': u'Alameda High', 'code': u'789'}
                ]
            },
            'NY_college': {
                u'St Paul': [
                    {'name': u'Syracuse High', 'code': u'10'}
                ]
            },
            'states': {
                'college': [u'CA', u'NY']
            }
        })


if __name__ == '__main__':
    unittest.main()
