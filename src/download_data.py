import configparser
import json
import logging
import urllib.request

import helper

config = configparser.ConfigParser(allow_no_value=True)
config.read(helper.config_file)


def get_data_from_website(url):
    logging.info('try get info from website')
    try:
        response = urllib.request.urlopen(url, timeout=5).read().decode('utf-8')
        j = json.loads(response)
        return j

    except Exception as e:
        logging.exception(e)
        raise


if __name__ == '__main__':
    pass