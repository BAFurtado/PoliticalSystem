""" Run the procedures of the model
"""

from government import Government
import parameters
from representatives import Representative
from outputs import Projects


def main(g, reps):
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
    print(G)
    [print(i) for i in R[-3:]]
    p = main(G, R)
    [print(i) for i in p[-3:]]
    print('There are {} projects, with average ideology of {:.4f}'.format(len(p), sum([x.ideology for x in p])/len(p)))
