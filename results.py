from collections import defaultdict

import main

p, gov, rep = main.main()

print('Government ideology {:.3f}'.format(gov.ideology))
print('House ideology {:.3f}'.format(sum([x.ideology for x in rep])/len(rep)))

res = defaultdict(lambda: defaultdict(float))
for each in p:
    res[each.category]['num'] += 1
    res[each.category]['ideology'] += each.ideology
    res[each.category]['votes'] += each.vote

for key in res.keys():
    print('Total projects {} {:.0f}. Average ideology {:.3f}. Average votes received {:.1f}'.
          format(key, res[key]['num'], res[key]['ideology'] / res[key]['num'], res[key]['votes'] / res[key]['num']))
