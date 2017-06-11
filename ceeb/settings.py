import os

from pymongo import MongoClient


def get_mongo_client():
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/schools')
    client = MongoClient(mongo_uri)

    return client


def get_logger(name):
    import logging

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger


# Constants

BASE_URL = 'https://www.suny.edu/attend/ceeb-codes'

TIMEOUT = 20

STATES = {
    'Alabama': 2,
    'Alaska': 1,
    'American Samoa': 4,
    'Arizona': 5,
    'Arkansas': 3,
    'Armed Forces Europe': 64,
    'Armed Forces Pacific': 65,
    'Armed Forces the Americas': 63,
    'California': 6,
    'Colorado': 7,
    'Connecticut': 8,
    'Delaware': 11,
    'Dist. Of Columbia': 10,
    'Florida': 12,
    'Georgia': 14,
    'Guam': 15,
    'Hawaii': 16,
    'Idaho': 18,
    'Illinois': 19,
    'Indiana': 20,
    'Iowa': 17,
    'Kansas': 21,
    'Kentucky': 22,
    'Louisiana': 23,
    'Maine': 26,
    'Marshall Islands': 27,
    'Maryland': 25,
    'Massachusetts': 24,
    'Michigan': 28,
    'Micronesia': 13,
    'Minnesota': 29,
    'Mississippi': 32,
    'Missouri': 30,
    'Montana': 33,
    'Nebraska': 36,
    'Nevada': 40,
    'New Hampshire': 37,
    'New Jersey': 38,
    'New Mexico': 39,
    'New York': 41,
    'North Carolina': 34,
    'North Dakota': 35,
    'Northern Mariana Islands': 31,
    'Ohio': 42,
    'Oklahoma': 43,
    'Oregon': 44,
    'Palau': 49,
    'Pennsylvania': 46,
    'Puerto Rico': 48,
    'Rhode Island': 50,
    'South Carolina': 51,
    'South Dakota': 52,
    'Tennessee': 53,
    'Texas': 54,
    'Utah': 55,
    'Vermont': 58,
    'Virgin Islands': 57,
    'Virginia': 56,
    'Washington': 59,
    'West Virginia': 61,
    'Wisconsin': 60,
    'Wyoming': 62
}
