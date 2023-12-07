class Solution:

    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        start = self.toMinutes(loginTime)
        end = self.toMinutes(logoutTime)

        roundedStart = self.toNextQuarter(start)
        roundedEnd = self.toPreviousQuarter(end)

        if (start < end):
            return max(0, (roundedEnd - roundedStart) // 15)

        return (24 * 60 - roundedStart + roundedEnd) // 15

    def toMinutes(self, time):
        return 60 * int(time[:2]) + int(time[-2:])

    def toNextQuarter(self, time):
        return ((time + 14) // 15) * 15

    def toPreviousQuarter(self, time):
        return (time // 15) * 15
