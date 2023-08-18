class Solution:

    def reformatDate(self, date: str) -> str:
        monthMap = {
            "Jan": '01',
            "Feb": '02',
            "Mar": '03',
            "Apr": '04',
            "May": '05',
            "Jun": '06',
            "Jul": '07',
            "Aug": '08',
            "Sep": '09',
            "Oct": '10',
            "Nov": '11',
            "Dec": '12'
        }

        date = date.split(' ')
        result = date[2] + '-' + monthMap[date[1]] + '-'

        if len(date[0]) == 3:
            result += '0' + date[0][0]
        else:
            result += date[0][:2]

        return result
