import collections
from typing import List


class TweetCounts:

    def __init__(self):
        self.tweetMap = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweetMap[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str,
                                   startTime: int, endTime: int) -> List[int]:
        if freq == "minute": seconds = 60
        elif freq == "hour": seconds = 3600
        else: seconds = 86400

        res = [0] * (((endTime - startTime) // seconds) + 1)
        for t in self.tweetMap[tweetName]:
            if startTime <= t <= endTime:
                res[(t - startTime) // seconds] += 1

        return res
