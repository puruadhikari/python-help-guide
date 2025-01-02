"""
LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card,
the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses
the key-card three or more times in a one-hour period.

You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and
the time when their key-card was used in a single day.

Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.

Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.



Example 1:

Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
Output: ["daniel"]
Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").
Example 2:

Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
Output: ["bob"]
Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").
"""
from datetime import datetime, timedelta


class Solution(object):
    def _has_three_swipes(self, time_entries):
        time_entries.sort()
        time_series = [datetime.strptime(en, "%H:%M") for en in time_entries]
        for index in range(len(time_series) - 2):
            if time_series[index + 2] - time_series[index] <= timedelta(hours=1):
                return True
        return False

    def alert_names(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """

        employee_dict = {}
        result = []
        for index, name in enumerate(keyName):
            if name not in employee_dict:
                employee_dict[name] = [keyTime[index]]
            else:
                employee_dict[name].append(keyTime[index])

        for key, value in employee_dict.items():
            if self._has_three_swipes(value):
                result.append(key)

        result.sort()

        return result


keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
sol = Solution()

print(sol.alert_names(keyName,keyTime))