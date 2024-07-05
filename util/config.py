#!/usr/bin/env python3
# -*- coding: utf_8 -*-
'''config.py'''
class Config:
    """Configuration settings"""
    def __init__(self, endpoint, ent, org, token, order, event_type, phrase):
        self.endpoint = endpoint
        self.ent = ent
        self.org = org
        self.token = token
        self.order = order
        self.event_type = event_type
        self.phrase = phrase