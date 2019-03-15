""" Parameters of the model
"""

import numpy as np


def gen_distributions(p):
    rep_ideology = np.random.normal(p['mu'], p['sigma'], p['num_representatives'])
    rep_tolerance = np.random.uniform(size=p['num_representatives'])
    p['rep_ideology'] = rep_ideology
    p['rep_tolerance'] = rep_tolerance
    return p


def parameters():
    par = {'periods': 10, 'num_representatives': 503,
           # Government]
           'gov_ideology': .5, 'gov_tolerance': .1, 'num_g_projects': 8,
           # Representative
           'mu': .2, 'sigma': .1,
           # Tolerance is drawn from a uniform distribution
           'num_rep_projects': 1,
           # Legislative bodies
           'num_projects': 100}
    par = gen_distributions(par)
    return par
