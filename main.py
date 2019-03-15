""" Run the procedures of the model
"""

import numpy as np

from parameters import parameters
from government import Government
from projects import Projects
from representatives import Representative


def generate_population(p):
    g = Government(0, p['gov_ideology'], p['gov_tolerance'])
    reps = []
    for i in range(1, p['num_representatives'] + 1):
        reps.append(Representative(i, p['rep_ideology'][i - 1], p['rep_tolerance'][i - 1]))
    return g, reps


def create_projects(g, reps, p):
    # Creating projects
    projects = []
    protocol = 0
    for i in range(protocol, p['num_g_projects']):
        projects.append(Projects(i, g.ideology))
    protocol = i + 1
    for j in range(protocol, protocol + p['num_rep_projects']):
        for w in range(len(reps)):
            projects.append(Projects(protocol, reps[w].ideology))
            protocol += 1
    return projects


def projects_to_analyze(projs, p):
    order_day = np.random.choice(projs[p['num_g_projects']:], p['num_projects'], replace=False).tolist()
    for each in order_day:
        each.define_category('order of the day')
    return order_day


def voting(projs, repr):
    for p in projs:
        for r in repr:
            if (r.ideology - r.tolerance) < p.ideology < (r.ideology + r.tolerance):
                p.cast_vote()
    return projs


def approve(projs, p):
    approved = []
    for each in projs:
        # Majority rule for approval
        if each.vote > (p['num_representatives'] / 2) + 1:
            each.define_category('approved')
            approved.append(each)
        else:
            each.define_category('not approved')
    approved.sort(key=lambda x: x.vote, reverse=True)
    return approved


def government_decision(g, s):
    for p in s:
        if (g.ideology - g.tolerance) < p.ideology < (g.ideology + g.tolerance):
            p.define_category('sanctioned')
        else:
            p.define_category('not sanctioned')


def main(par):
    gov, rep = generate_population(par)
    projs = create_projects(gov, rep, par)

    # Separating government projects
    gov_projs = projs[:par['num_g_projects']]

    # Choosing a sample of projects. All government included
    to_vote = projects_to_analyze(projs, par)

    # Adding all of government projects
    to_vote.extend(gov_projs)
    print('There are {} projects, with average ideology of {:.4f}'.
          format(len(projs), sum([x.ideology for x in projs])/len(projs)))

    voted = voting(to_vote, rep)
    aprov = approve(voted, par)
    government_decision(gov, aprov)
    return projs, gov, rep


if __name__ == '__main__':
    parms = parameters()
    p, gov, rep = main(parms)
    print('Government: ')
    print(gov)
    # Sorting projects by number of votes
    p.sort(key=lambda x: x.vote, reverse=True)
    print('\nTop voted')
    [print(i) for i in p[:3]]
    print('\nLeast voted, but approved')
    [print(i) for i in p[-3:]]
