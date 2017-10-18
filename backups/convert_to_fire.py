"""
Denormalize mongo data for firebase.

Usage:
    $ python convert_to_fire.py -o 'firebase.json'
"""
import argparse
import codecs
from curses import ascii
import json


def sanitize(val):
    """
    Remove ., $, #, [, ], /, or ASCII control characters 0-31 or 127.
    """
    for char in val:
        if ascii.isctrl(char) or ord(char) == 127:
            print('%s has invalid ascii char: %s' % (val, char))
            val = val.replace(char, '')

    for invalid in ['$', '#', '[', ']', '.', '/']:
        if invalid in val:
            print('%s has invalid char: %s' % (val, invalid))
            val = val.replace(invalid, '')

    return val.strip()


def convert_schools(schools, school_type):
    results = {'states': {school_type: []}}
    for school in schools:
        school = json.loads(school)

        # Add state
        if school['address']['state'] not in results['states'][school_type]:
            results['states'][school_type].append(school['address']['state'])

        # Add school
        city = sanitize(school['address']['city'])
        if not city:
            print('City is missing for {school}'.format(school=school['name']))
            continue

        state = '{state}_{type}'.format(state=school['address']['state'], type=school_type)
        ceeb = {
            'name': school['name'].strip(),
            'code': school['ceeb_code']
        }

        if state not in results:
            results[state] = {
                sanitize(city): [ceeb]
            }
        else:
            if city in results[state]:
                results[state][sanitize(school['address']['city'])].append(ceeb)
            else:
                results[state][sanitize(school['address']['city'])] = [ceeb]

    return results


def get_schools():
    schools = {}
    with open('data/colleges.json') as f:
        schools.update(convert_schools(f, 'college'))

    with open('data/highschools.json') as f:
        schools.update(convert_schools(f, 'highschool'))

    return schools


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output_file', required=True, help='Output file')
    args = parser.parse_args()

    schools = get_schools()
    with codecs.open(args.output_file, 'w', 'utf-8') as f:
        f.write(json.dumps(schools, indent=2))


if __name__ == '__main__':
    main()
