#!/usr/bin/env python3
# -*- coding: utf_8 -*-
'''github.py'''
import logging
import requests

class GitHub:
    '''GitHub class'''
    def __init__(self, config):
        self.config = config
        self.per_page = 100

    def list_events(self):
        """list events"""
        events = []
        endpoint_url = self.generate_endpoint()
        while endpoint_url:
            response = requests.get(endpoint_url, headers={'Authorization': f'bearer {self.config.token}'})
            if response.status_code == 200:
                response_json = response.json()
                for item in response_json:
                    events.append(item)
                if 'next' in response.links:
                    endpoint_url = response.links['next']['url']
                else:
                    endpoint_url = None
            else:
                logging.error("Error: %s", response.status_code)
                endpoint_url = None
        return events

    def generate_endpoint(self):
        '''generate endpoint'''
        endpoint_url = None
        params = []

        if self.config.ent:
            endpoint_url = f'{self.config.endpoint}/enterprises/{self.config.ent}/audit-log'
        if self.config.org:
            endpoint_url = f'{self.config.endpoint}/orgs/{self.config.org}/audit-log'
        if self.config.order:
            params.append(f'order={self.config.order}')
        if self.config.event_type:
            params.append(f'include={self.config.event_type}')
        if self.config.phrase:
            params.append(f'phrase={self.config.phrase}')
        if self.per_page:
            params.append(f'per_page={self.per_page}')
        if params:
            endpoint_url += '?' + '&'.join(params)
        logging.info("Endpoint URL: %s", endpoint_url)
        return endpoint_url
