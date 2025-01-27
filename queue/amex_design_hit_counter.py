"""
Description
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are
being made to the system in chronological order (i.e., timestamp is monotonically increasing).
Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).

Example 1:
Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]
"""

from collections import deque


class HitCounter:

    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int):
        self.queue.append(timestamp)

    def getHits(self, timestamp: int):
        while self.queue and self.queue[0] < timestamp - 299:
            self.queue.popleft()

        return len(self.queue)


input_val = ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
times = [[], [1], [2], [3], [4], [300], [300], [301]]
ht = HitCounter()
output = []

for index, value in enumerate(input_val):
    if value == "HitCounter":
        output.append(None)

    if value == "hit":
        ht.hit(times[index][0])
        output.append(None)

    if value == "getHits":
        output.append(ht.getHits(times[index][0]))

print(output)