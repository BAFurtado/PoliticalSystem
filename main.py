""" Run the procedures of the model
"""

from government import Government
import parameters
from representatives import Representative
from outputs import Projects

import numpy as np


def voting(projs, repr):
    for each in projs:
        for r in repr:
            if (r.ideology - r.tolerance) < each.ideology < (r.ideology + r.tolerance):
                each.cast_vote()


def projects_to_analyze(projs):
    return np.random.choice(projs[parameters.num_g_projects:], parameters.num_projects, replace=False).tolist()


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


def generate_population():
    g = Government(0)
    reps = []
    for i in range(1, parameters.num_representatives + 1):
        reps.append(Representative(i))
    return g, reps


if __name__ == '__main__':
    G, R = generate_population()
    p = create_projects(G, R)
    # Separating government projects
    g = p[:parameters.num_g_projects]
    # Choosing a sample of projects
    p = projects_to_analyze(p)
    # Adding all of government projects
    p.extend(g)
    print('There are {} projects, with average ideology of {:.4f}'.format(len(p), sum([x.ideology for x in p])/len(p)))
    voting(p, R)
    p.sort(key=lambda x: x.vote, reverse=True)

    print('Top voted')
    [print(i) for i in p[:5]]

    print('Least voted')
    [print(i) for i in p[-5:]]
