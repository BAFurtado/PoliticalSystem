""" Run the procedures of the model
"""

from government import Government
import parameters
from representatives import Representative
from outputs import Projects

import numpy as np


def generate_population():
    g = Government(0, parameters.gov_ideology, parameters.gov_tolerance)
    reps = []
    for i in range(1, parameters.num_representatives + 1):
        reps.append(Representative(i, parameters.rep_ideology[i - 1], parameters.rep_tolerance[i - 1]))
    return g, reps


def create_projects(g, reps):
    # Creating projects
    projects = []
    protocol = 0
    for i in range(protocol, parameters.num_g_projects):
        projects.append(Projects(i, g.ideology))
    protocol = i + 1
    for j in range(protocol, protocol + parameters.num_rep_projects):
        for w in range(len(reps)):
            projects.append(Projects(protocol, reps[w].ideology))
            protocol += 1
    return projects


def projects_to_analyze(projs):
    return np.random.choice(projs[parameters.num_g_projects:], parameters.num_projects, replace=False).tolist()


def voting(projs, repr):
    for p in projs:
        for r in repr:
            if (r.ideology - r.tolerance) < p.ideology < (r.ideology + r.tolerance):
                p.cast_vote()
    return projs


def approve(projs, threshold):
    approved = []
    for each in projs:
        if each.vote > threshold:
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
    return s


def main():
    gov, rep = generate_population()
    projs = create_projects(gov, rep)
    # Separating government projects
    gov_projs = projs[:parameters.num_g_projects]
    # Choosing a sample of projects. All government included
    to_vote = projects_to_analyze(projs)
    # Adding all of government projects
    to_vote.extend(gov_projs)
    print('There are {} projects, with average ideology of {:.4f}'.
          format(len(projs), sum([x.ideology for x in projs])/len(projs)))
    voted = voting(to_vote, rep)
    aprov = approve(voted, parameters.limit)
    sanction = government_decision(gov, aprov)
    return aprov, projs, gov_projs, voted, sanction


if __name__ == '__main__':
    a, p, g, v, s = main()
    # Sorting projects by number of votes
    p.sort(key=lambda x: x.vote, reverse=True)
    print('Top voted')
    [print(i) for i in p[:3]]
    print('Least voted, but approved')
    [print(i) for i in a[-3:]]
    print('Proposed, not voted')
    [print(i) for i in p[-3:]]
    print('Government projects')
    [print(i) for i in g[-3:]]

