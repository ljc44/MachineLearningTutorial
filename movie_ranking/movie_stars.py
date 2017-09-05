#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by C.L.Wang

import os

import pandas as pd
import matplotlib.pyplot as plt

RATINGS = os.path.join(os.path.dirname(__file__), 'data', 'ratings.csv')


class Ratings(object):
    def __init__(self, path=RATINGS):
        self.path = path
        self.load()

    def load(self):
        self.data = pd.read_csv(self.path)

    def __str__(self):
        return str(self.data.head())

    @property
    def movies(self):
        return self.data.groupby('title')

    def get_means(self):
        return self.movies['rating'].mean()

    def get_counts(self):
        return self.movies['rating'].count()

    def top_movies(self, n=-10):
        grid = pd.DataFrame({
            'mean': self.get_means(),
            'conut': self.get_counts()
        })
        return grid.ix[grid['mean'].argsort()[n:]]

    def plot_mean_frequency(self):
        grid = pd.DataFrame({
            'Mean Rating': self.movies['rating'].mean(),
            'Number of Reviewers': self.movies['rating'].count()
        })

        grid.plot(x='Number of Reviewers', y='Mean Rating', kind='hexbin',
                  xscale='log', cmap='BuGn', gridsize=12, mincnt=1,
                  title="Star Ratings by Simple Mean")
        plt.show()


if __name__ == '__main__':
    ratings = Ratings()
    print ratings.top_movies()
    ratings.plot_mean_frequency()
