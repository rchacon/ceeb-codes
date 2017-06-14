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

STATES = {
    'Alabama': {'id': 2, 'abbr': 'AL'},
    'Alaska': {'id': 1, 'abbr': 'AK'},
    'American Samoa': {'id': 4, 'abbr': 'AS'},
    'Arizona': {'id': 5, 'abbr': 'AZ'},
    'Arkansas': {'id': 3, 'abbr': 'AR'},
    'Armed Forces Europe': {'id': 64, 'abbr': 'AE'},
    'Armed Forces Pacific': {'id': 65, 'abbr': 'AP'},
    'Armed Forces the Americas': {'id': 63, 'abbr': 'AA'},
    'California': {'id': 6, 'abbr': 'CA'},
    'Colorado': {'id': 7, 'abbr': 'CO'},
    'Connecticut': {'id': 8, 'abbr': 'CT'},
    'Delaware': {'id': 11, 'abbr': 'DE'},
    'Dist. Of Columbia': {'id': 10, 'abbr': 'DC'},
    'Florida': {'id': 12, 'abbr': 'FL'},
    'Georgia': {'id': 14, 'abbr': 'GA'},
    'Guam': {'id': 15, 'abbr': 'GU'},
    'Hawaii': {'id': 16, 'abbr': 'HI'},
    'Idaho': {'id': 18, 'abbr': 'ID'},
    'Illinois': {'id': 19, 'abbr': 'IL'},
    'Indiana': {'id': 20, 'abbr': 'IN'},
    'Iowa': {'id': 17, 'abbr': 'IA'},
    'Kansas': {'id': 21, 'abbr': 'KS'},
    'Kentucky': {'id': 22, 'abbr': 'KY'},
    'Louisiana': {'id': 23, 'abbr': 'LA'},
    'Maine': {'id': 26, 'abbr': 'ME'},
    'Marshall Islands': {'id': 27, 'abbr': 'MH'},
    'Maryland': {'id': 25, 'abbr': 'MD'},
    'Massachusetts': {'id': 24, 'abbr': 'MA'},
    'Michigan': {'id': 28, 'abbr': 'MI'},
    'Micronesia': {'id': 13, 'abbr': 'FM'},
    'Minnesota': {'id': 29, 'abbr': 'MN'},
    'Mississippi': {'id': 32, 'abbr': 'MS'},
    'Missouri': {'id': 30, 'abbr': 'MO'},
    'Montana': {'id': 33, 'abbr': 'MT'},
    'Nebraska': {'id': 36, 'abbr': 'NE'},
    'Nevada': {'id': 40, 'abbr': 'NV'},
    'New Hampshire': {'id': 37, 'abbr': 'NH'},
    'New Jersey': {'id': 38, 'abbr': 'NJ'},
    'New Mexico': {'id': 39, 'abbr': 'NM'},
    'New York': {'id': 41, 'abbr': 'NY'},
    'North Carolina': {'id': 34, 'abbr': 'NC'},
    'North Dakota': {'id': 35, 'abbr': 'ND'},
    'Northern Mariana Islands': {'id': 31, 'abbr': 'MP'},
    'Ohio': {'id': 42, 'abbr': 'OH'},
    'Oklahoma': {'id': 43, 'abbr': 'OK'},
    'Oregon': {'id': 44, 'abbr': 'OR'},
    'Palau': {'id': 49, 'abbr': 'PW'},
    'Pennsylvania': {'id': 46, 'abbr': 'PA'},
    'Puerto Rico': {'id': 48, 'abbr': 'PR'},
    'Rhode Island': {'id': 50, 'abbr': 'RI'},
    'South Carolina': {'id': 51, 'abbr': 'SC'},
    'South Dakota': {'id': 52, 'abbr': 'SD'},
    'Tennessee': {'id': 53, 'abbr': 'TN'},
    'Texas': {'id': 54, 'abbr': 'TX'},
    'Utah': {'id': 55, 'abbr': 'UT'},
    'Vermont': {'id': 58, 'abbr': 'Vt'},
    'Virgin Islands': {'id': 57, 'abbr': 'VI'},
    'Virginia': {'id': 56, 'abbr': 'VA'},
    'Washington': {'id': 59, 'abbr': 'WA'},
    'West Virginia': {'id': 61, 'abbr': 'WV'},
    'Wisconsin': {'id': 60, 'abbr': 'WI'},
    'Wyoming': {'id': 62, 'abbr': 'WY'}
}
