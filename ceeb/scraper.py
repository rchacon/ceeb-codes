import os
from datetime import datetime

from lxml.html import document_fromstring
from pymongo import MongoClient
import requests

from .settings import get_logger, STATES


BASE_URL = 'https://www.suny.edu/attend/ceeb-codes'

TIMEOUT = 20


def parse(html, poll_time, td_offset=0):
    """Parse html for highschool/college ceeb codes.

    Args:
        td_offset: offset after header row for processing <td> tags.

    Returns:
        a list of dictionaries.
    """
    root = document_fromstring(html)

    try:
        table = root.get_element_by_id('linksTable')
    except KeyError:
        return []

    schools = []
    # Add 1 to offset for header row.
    index = td_offset + 1
    for row in table[index:]:
        school = {
            'ceeb_code': row[3].text_content(),
            'name': row[0].text_content(),
            'address': {
                'city': row[1].text_content(),
                'state': row[2].text_content()
            },
            'date_created': poll_time,
            'date_modified': poll_time,
            'date_deleted': None,
        }
        schools.append(school)

    return schools


def get_html(url, form=None):
    session = requests.Session()

    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    })

    data = {
        'pageId': 'search',
        'Search': 'Search'
    }

    if form:
        data.update(form)

    resp = session.post(url, data=data, timeout=TIMEOUT)

    return resp.text


def scrape_highschools(state, city='', name=''):
    form = {
        'HSName': name,
        'State': STATES[state],
        'City': city
    }

    url = '{}/search_highschool/hs_searchaction.cfm?popUp=false&year='.format(BASE_URL)
    html = get_html(url, form=form)

    poll_time = datetime.utcnow()
    highschools = parse(html, poll_time, td_offset=1)

    return highschools


def scrape_colleges(state, city='', name=''):
    form = {
        'collName': name,
        'state': STATES[state],
        'city': city
    }

    url = '{}/search_colleges/college_searchaction.cfm?popUp=false&year='.format(BASE_URL)
    html = get_html(url, form=form)

    poll_time = datetime.utcnow()
    colleges = parse(html, poll_time)

    return colleges


def main(save):
    """Scrape ceeb codes and insert them into mongo."""
    logger = get_logger('ceeb')
    logger.debug('*' * 79)

    if save:
        client = MongoClient(os.getenv('MONGO_URI'))
        db = client.get_default_database()

    states = STATES.keys()

    # Process highschools
    hs_found = 0
    hs_saved = 0
    for state in states:
        logger.info('Processing %s highschools' % state)
        highschools = scrape_highschools(state)

        logger.info('Found %s highschools' % len(highschools))
        hs_found += len(highschools)

        # Insert highschools into mongo
        if len(highschools) > 0 and save:
            hs_result = db.highschools.insert_many(highschools)
            logger.info('Highschools records inserted: %s' % len(hs_result.inserted_ids))

            if len(hs_result.inserted_ids) != len(highschools):
                diff = len(highschools) - len(hs_result.inserted_ids)
                logger.error('Error inserting %s of the highschools' % diff)
            hs_saved += len(hs_result.inserted_ids)

    logger.info('Total highschools found: %s' % hs_found)
    logger.info('Total highschools saved: %s' % hs_saved)

    # Process colleges
    coll_found = 0
    coll_saved = 0
    for state in states:
        logger.info('Processing %s colleges' % state)
        colleges = scrape_colleges(state)

        logger.info('Found %s colleges' % len(colleges))
        coll_found += len(colleges)

        # Insert colleges into mongo
        if len(colleges) > 0 and save:
            coll_result = db.colleges.insert_many(colleges)
            logger.info('College records inserted: %s' % len(coll_result.inserted_ids))

            if len(coll_result.inserted_ids) != len(colleges):
                diff = len(colleges) - len(coll_result.inserted_ids)
                logger.error('Error inserting %s of the colleges' % diff)
            coll_saved += len(coll_result.inserted_ids)

    logger.info('Total colleges found: %s' % coll_found)
    logger.info('Total colleges saved: %s' % coll_saved)

    if save:
        client.close()


if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--save', action='store_true', help='Save to mongo')
    args = parser.parse_args()

    if args.save and os.getenv('MONGO_URI') is None:
        sys.exit('Environment Variable MONGO_URI must be set.')

    main(args.save)
