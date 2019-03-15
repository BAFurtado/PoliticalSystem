import itertools

from numpy import linspace as lp
import main
from results import plotting, results
from parameters import parameters, gen_distributions

par = parameters()

for each in list(itertools.permutations(lp(.25, .75, 5), r=2)):
    par['gov_ideology'] = each[0]
    par['mu'] = each[1]
    par = gen_distributions(par)
    p, gov, rep = main.main(par)
    r = results(p)
    plotting(p, r, 'run_{:.3f}_{:.3f}'.format(each[0], each[1]))
