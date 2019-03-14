""" Parameters of the model
"""

import numpy as np

periods = 10
num_representatives = 503
# Government
gov_ideology = .5
gov_tolerance = .1
num_g_projects = 8
# Representative
mu = .5
sigma = .1
# Initially, ideology is drawn from a Normal distribution with mu and sigma values
rep_ideology = np.random.normal(mu, sigma, num_representatives)
# Tolerance is drawn from a uniform distribution
rep_tolerance = np.random.uniform(size=num_representatives)
num_rep_projects = 1
# Legislative bodies
num_projects = 100
