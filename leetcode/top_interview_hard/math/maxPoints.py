
class Solution(object):

    def maxPoints(self, points):

        maxim = 0
        for i in range(len(points)):
            dic = {}
            for j in range(i+1,len(points)):
                # Seria més correcte trobant el vector director,
                # i emmagatzemar-lo considerant la seva reducció
                # al dividir pel gcd. Però aquest procediment
                # acaba sent bastant menys eficient.
                if points[j][0] == points[i][0]:
                    slope = 10**8
                elif points[j][1] == points[i][1]:
                    slope = 0
                else:
                    slope = (points[j][1]-points[i][1])/float(points[j][0]-points[i][0])
                    slope = round((10**6)*slope)/(10**6)
                dic[slope] = dic.get(slope,0) + 1
            for k in dic.keys():
                if dic[k] > maxim:
                    maxim = dic[k]
                    
        return maxim+1


sol = Solution()
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(sol.maxPoints(points))
points = [[1,1],[2,2],[3,3]]
print(sol.maxPoints(points))
points = [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]
print(sol.maxPoints(points))
points = [[5151,5150],[0,0],[5152,5151]]
print(sol.maxPoints(points))
[[-424,-512],[-4,-47],[0,-23],[-7,-65],[7,138],[0,27],[-5,-90],[-106,-146],[-420,-158],[-7,-128],[0,16],[-6,9],[-34,26],[-9,-166],[-570,-69],[-665,-85],[560,248],[1,-17],[630,277],[1,-7],[-287,-222],[30,250],[5,5],[-475,-53],[950,187],[7,-6],[-700,-274],[3,62],[-318,-390],[7,19],[-285,-21],[-5,4],[53,37],[-5,-1],[-2,-33],[-95,11],[4,1],[8,25],[700,306],[1,24],[-2,-6],[-35,-387],[-630,-245],[-328,-260],[-350,-129],[35,299],[-380,-37],[-9,-9],[210,103],[7,-5],[-3,-52],[-51,23],[-8,-147],[-371,-451],[-1,-14],[-41,6],[-246,-184],[350,161],[-212,-268],[-140,-42],[-9,-4],[-7,5],[10,6],[-15,-191],[-7,-4],[318,342],[-8,-71],[-68,20],[6,119],[6,13],[-280,-100],[140,74],[-760,-101],[0,-24],[-70,-13],[0,2],[0,-9],[106,98]]
print(sol.maxPoints(points))