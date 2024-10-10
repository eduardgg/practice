class Solution(object):
    def reconstructQueue(self, people):
        people.sort()
        output = []
        i = len(people) - 1
        ultim = i+1
        while i >= 0:
            height = people[i][0]
            i -= 1
            while i >= 0 and people[i][0] == height:
                i -= 1
            for p in people[i+1:ultim]:
                output.insert(p[1], p)
            ultim = i+1
        return output

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(Solution().reconstructQueue(people))
people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
print(Solution().reconstructQueue(people))