#!/usr/bin/env python
"""
========================
Polynomial interpolation
========================

This example demonstrates how to approximate a function with a polynomial of
degree n_degree by using ridge regression. Concretely, from n_samples 1d
points, it suffices to build the Vandermonde matrix, which is n_samples x
n_degree+1 and has the following form:

[[1, x_1, x_1 ** 2, x_1 ** 3, ...],
 [1, x_2, x_2 ** 2, x_2 ** 3, ...],
 ...]

Intuitively, this matrix can be interpreted as a matrix of pseudo features (the
points raised to some power). The matrix is akin to (but different from) the
matrix induced by a polynomial kernel.

This example shows that you can do non-linear regression with a linear model,
by manually adding non-linear features. Kernel methods extend this idea and can
induce very high (even infinite) dimensional feature spaces.
"""
print __doc__

# Author: Mathieu Blondel
# License: BSD Style.

import numpy as np
import pylab as pl

from scikits.learn.linear_model import Ridge

np.random.seed(0)


def f(x):
    """ function to approximate by polynomial interpolation"""
    return x * np.sin(x)


def vandermonde(x, degree=1):
    """ build vandermonde matrix from 1d points"""
    X = [np.ones(len(x))]
    for n in range(degree):
        X.append(x ** (n + 1))
    return np.array(X).T

# generate points used to plot
x_plot = np.linspace(0, 10, 100)

# generate points and keep a subset of them
x = np.linspace(0, 10, 100)
np.random.shuffle(x)
x = np.sort(x[:20])
y = f(x)

pl.plot(x_plot, f(x_plot), label="ground truth")
pl.scatter(x, y, label="training points")

for degree in [3, 4, 5]:
    ridge = Ridge()
    ridge.fit(vandermonde(x, degree), y)
    pl.plot(x_plot, ridge.predict(vandermonde(x_plot, degree)),
            label="degree %d" % degree)

pl.legend(loc='lower left')

pl.show()
