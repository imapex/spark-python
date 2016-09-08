import requests
import logging
import os

logging.getLogger()


class Session(object):

    def __init__(self, url=None, token=None):

        if not url:
            try:
                token = os.environ["SPARK_URL"]
            except KeyError:
                pass

        if not token:
            try:
                token = os.environ["SPARK_TOKEN"]
            except KeyError:
                pass

        self.base_url = url + '/v1'
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'Bearer {}'.format(token)}

    def get(self, url):
        url = self.base_url + url
        resp = requests.get(url, headers=self.headers)

        return resp

    def post(self, url, payload):
        url = self.base_url + url

        try:

            resp = requests.post(url, headers=self.headers, data=payload)
            logging.debug('Posting {} to {}'.format(payload, self.base_url))
            if resp.ok:
                logging.debug(resp.text)

            return resp

        except requests.exceptions.ConnectionError:
            logging.error('Connection Timed out to %s' % self.base_url)

    def delete(self, url):
        url = self.base_url + url

        try:

            resp = requests.delete(url, headers=self.headers)
            logging.debug('Deleting {}'.format(url))
            if resp.ok:
                logging.debug(resp.text)

            return resp

        except requests.exceptions.ConnectionError:
            logging.error('Connection Timed out to %s' % self.base_url)
