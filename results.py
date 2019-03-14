from collections import defaultdict

import main

p, gov, rep = main.main()

res = defaultdict(lambda: defaultdict(float))
for each in p:
    res[each.category]['num'] += 1
    res[each.category]['ideology'] += each.ideology
    res[each.category]['votes'] += each.vote

for key in res.keys():
    print('Total projects {} {:.0f}. Average ideology {:.3f}. Average votes received {:.1f}'.
          format(key, res[key]['num'], res[key]['ideology'] / res[key]['num'], res[key]['votes'] / res[key]['num']))
