"""
You are given two parallel arrays of equal length:

names - An array of strings where each element represents a person's name (e.g., "Sarah", "John").
actions - An array of strings where each element is either "enter" or "exit", indicating whether the
corresponding person entered or exited the building at that point in time.
You must determine:

People who entered without ever exiting by the end of the logs.
People who exited without ever having entered (i.e., they show an exit action before any corresponding enter).

names   = ["Sarah", "John", "Sarah", "Mike", "Abdul", "Sarah"]
actions = ["enter", "exit",  "enter", "enter", "enter", "exit"]

[
  ["Sarah", "Mike", "Abdul"],   # entered without exit
  ["John"]                      # exit without enter
]


"""

from collections import defaultdict

entry_dict = defaultdict(int)
exit_dict = defaultdict(int)
names   = ["Sarah", "John", "Sarah", "Mike", "Abdul", "Sarah"]
actions = ["enter", "exit",  "enter", "enter", "enter", "exit"]

for index in range(len(names)):
  if actions[index]=="enter":
    entry_dict[names[index]] += 1
  else:
    exit_dict[names[index]] +=1
entered_without_exit =[]
exit_without_entry = []

for name,count in entry_dict.items():
  if name not in exit_dict or count > exit_dict[name]:
    entered_without_exit.append(name)

for name,count in exit_dict.items():
  if name not in entry_dict or count > entry_dict[name]:
    exit_without_entry.append(name)

print(entered_without_exit)
print(exit_without_entry)