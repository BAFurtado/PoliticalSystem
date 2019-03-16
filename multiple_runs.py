import itertools
from collections import defaultdict
import pandas as pd
from numpy import linspace as lp
import main
from results import plotting, results
from parameters import parameters, gen_distributions

par = parameters()

res = pd.DataFrame()
run = 0

for each in list(itertools.permutations(lp(.25, .75, 5), r=2)):
    par['gov_ideology'] = each[0]
    par['mu'] = each[1]
    par = gen_distributions(par)
    p, gov, rep = main.main(par)
    r = results(p)
    for i in r.keys():
        res.loc[run, i] = r[i]
        res.loc[run, 'num_p_{}'.format(i)] = len([x for x in p if x.category == i])
    res.loc[run, 'gov_ideology'] = each[0]
    res.loc[run, 'mu'] = each[1]
    run += 1
    plotting(p, 'run_{:.3f}_{:.3f}'.format(each[0], each[1]))

res.to_csv('results.csv', sep=';')
