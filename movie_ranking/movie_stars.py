#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by C.L.Wang

import os

import pandas as pd

RATINGS = os.path.join(os.path.dirname(__file__), 'data', 'ratings.csv')


class Ratings(object):
    def __init__(self, path=RATINGS):
        self.path = path
        self.load()

    def load(self):
        self.data = pd.read_csv(self.path)

    def __str__(self):
        return str(self.data.head())


if __name__ == "__main__":
    ratings = Ratings()
    print ratings
