from collections import Counter

s = "aab"

s_lst = Counter(list(s))

print(s_lst.values())

a_set = set(s_lst.values())

counter = 0

for item in s_lst.values():
  while item in a_set and len(a_set) <= len(s_lst.values()):
    item = item-1
    counter += 1
    if item not in a_set:
      a_set.add(item)
      print(item,a_set)
    break

print(counter)
