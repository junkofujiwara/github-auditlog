#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""common.py"""
import datetime
import getopt
import logging
import sys

def init():
    """init"""
    try:
        github_ent = None
        github_org = None
        github_token = None
        script = sys.argv[0]
        usage_text = (f"Usage: {script} "
                      "-t <github_personal_token> -e <enterprise_name> | -o <organization_name>")
        opts, _args = getopt.getopt(
            sys.argv[1:], "o:e:t:b:a:h", ["org=", "ent=", "token=", "help"]
        )
        for opt, arg in opts:
            if opt in ("-o", "--org"):
                github_org = arg
            elif opt in ("-e", "--ent"):
                github_ent = arg
            elif opt in ("-t", "--token"):
                github_token = arg
            elif opt in ("-h", "--help"):
                logging.info(usage_text)
                sys.exit()

        if github_org is None and github_ent is None:
            logging.info("Either -e <enterprise_name> or -o <organization_name> is required.")
            logging.info(usage_text)
            sys.exit()
        if github_token is None:
            logging.info("The -t <github_personal_token> parameter is required.")
            logging.info(usage_text)
            sys.exit()

        return github_org, github_ent, github_token
    except (getopt.GetoptError, IndexError) as exception:
        logging.error(exception)
        logging.info(usage_text)
        sys.exit(1)

def unix_time_to_isoformat(unix_time):
    """convert unix time to iso8601"""
    unix_time_seconds = int(unix_time) / 1000.0
    return datetime.datetime.fromtimestamp(unix_time_seconds).isoformat()
