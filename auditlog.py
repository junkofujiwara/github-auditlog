#!/usr/bin/env python3
# -*- coding: utf_8 -*-
'''list-pr.py'''
import csv
import logging
import settings
from util import config
from util import github as github_util
from util import util

def write_to_csv(events, output_file):
    '''write to csv'''
    with open(output_file, 'w', encoding='utf-8') as csvfile:
        fieldnames = ['timestamp_isoformat',
                      '@timestamp',
                      'action',
                      'actor',
                      'created_at',
                      'org',
                      'repo']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for event in events:
            actor = event.get('actor', '')
            created_at = event.get('created_at', '')
            org = event.get('org', '')
            repo = event.get('repo', '')
            timestamp_isoformat = util.unix_time_to_isoformat(event['@timestamp'])
            writer.writerow({
                'timestamp_isoformat': timestamp_isoformat,
                '@timestamp': event['@timestamp'],
                'action': event['action'],
                'actor': actor,
                'created_at': created_at,
                'org': org,
                'repo': repo
            })

def main():
    '''main function'''
    # set up logging
    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s [%(levelname)s] %(message)s",
        handlers = [
            logging.FileHandler(settings.LOG_FILE),
            logging.StreamHandler()
        ])

    # initialize
    github_org, github_ent, github_token = util.init()
    github_config = config.Config(settings.API_ENDPOINT,
                                           github_ent,
                                           github_org,
                                           github_token,
                                           settings.SORT_ORDER,
                                           settings.EVENT_TYPE,
                                           settings.SEARCH_PHRASE)
    github = github_util.GitHub(github_config)

    # get audit log events
    logging.info("Getting audit log events (ent: %s, org: %s, phrase: %s)",
                 github_ent, github_org, settings.SEARCH_PHRASE)
    events = github.list_events()
    write_to_csv(events, settings.OUTPUT_FILE)

if __name__ == "__main__":
    main()
