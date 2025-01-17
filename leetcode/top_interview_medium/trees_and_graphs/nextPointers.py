
# Definition for a Node
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# Construct a Perfect Binary Tree from its Vector
def constructPBT(v):
    nodes = [Node(v[i]) for i in range(len(v))]
    for j in range((len(v)-1)//2):
        nodes[j].left = nodes[2*j+1]
        nodes[j].right = nodes[2*j+2]
    return nodes[0]

def connect(root):
    if not root:
        return
    queue = [root]
    v = []
    while len(queue) > 0:
        l = len(queue)
        for i in range(l):
            node = queue[0]
            if len(queue) > 1:
                node.next = queue[1]
            if node.left:
                queue.append(node.left)
                queue.append(node.right)
            v.append(node.val)
            queue.pop(0)
        v.append('#')
    print(v)
    return

v = [-43,77,96,-77,88,-22,-1,-69,95,-45,23,70,-8,49,-24,-98,8,
    -75,5,-39,-34,67,-25,68,31,25,-80,-48,-32,-83,-4,91,-31,-48,
    -68,-60,24,30,-42,-14,-44,-62,53,45,74,84,9,32,67,19,21,38,
    55,-83,-18,-93,-90,-78,-88,-7,43,-10,-79,-99,-55,-93,-4,-71,
    8,-54,75,66,-60,-26,-29,-63,-87,22,-9,-1,97,-48,-47,70,40,5,
    -51,35,-13,-90,-46,33,-95,62,54,90,27,-6,56,-91,-44,-83,-2,
    25,89,-21,81,92,-8,69,23,-52,17,-19,-38,1,-16,29,-69,56,97,
    32,-68,-89,-83,47,45,3,-83,-70,-86,68,84,-29,-8,-13,-21,32,
    100,-38,49,-30,-35,-64,80,11,97,-8,-60,-6,-64,76,18,-37,-99,
    -17,-97,85,98,-4,-61,-76,96,99,-37,-63,51,-60,23,-37,12,31,
    -82,50,-58,-93,18,-1,79,-1,19,64,76,-9,-26,66,-96,55,74,-25,
    -75,-33,-40,64,-2,-2,-82,46,87,-33,-32,40,-51,-80,-46,51,36,
    -39,-1,-51,-78,-90,46,-2,-33,-100,30,18,81,-55,30,-3,-88,-54,
    -82,36,69,100,-33,24,75,12,40,-41,0,18,-2,16,34,-35,-67,16,
    32,-82,-30,49,61,15,11,35,80,26,-57,-43,-6,19,-61,-30,36,52,
    -33,48,76,44,-21,93,48,-42,-34,-3,15,74,-73,91,-57,86,-41,-92,
    36,99,-31,87,98,8,-24,-78,72,25,41,-12,-91,28,-92,76,13,71,
    -33,24,77,-3,54,63,-45,33,-11,-17,-42,-15,-34,-20,-81,4,-19,
    -42,19,-11,-95,-10,67,47,9,14,83,7,23,-53,20,63,53,66,41,-98,
    89,77,-92,-92,11,24,80,61,-31,-30,-38,-87,84,-39,-99,-30,66,4,
    0,-77,-27,-96,-28,16,-47,81,-14,44,69,-36,-87,26,17,87,-76,31,
    22,-45,-48,-26,81,-2,-57,96,32,-15,-76,99,88,61,96,38,-34,42,
    41,-33,100,83,84,82,18,-33,65,-36,-19,-11,-16,-99,-89,20,-37,
    12,-49,-60,-18,-75,-23,80,-21,-29,-1,49,65,32,-93,53,86,-82,
    -88,-16,91,2,28,-47,-7,45,-49,5,-44,4,28,-67,-11,65,-75,-88,
    -18,3,-47,-62,-88,-30,89,19,-11,52,2,-16,-34,-100,-100,-91,44,
    -37,48,-7,-10,-79,61,-48,-65,-5,34,7,-18,21,-100,83,-65,19,-23,
    20,-9,1,83,22,5,1,-83,9,-70,-86,62,11,25,-58,36,-21,-18,-58,
    -64,97,-53,32,-79,-7,1,40,-33,-76,38,-45,-63,6,-33,74,52,-71,
    -95,74,-58,-77,82,0,18,-10,-25,43,-57,42,87,-93,77,-90,-27,48,
    57,-52,65,96,7,-53,-21,39,47,-11,-63,-51,-66,66,-54,-92,31,-96,
    -14,34,86,11,40,-32,-58,-20,6,-9,66,49,-92,-23,-33,4,88,11,94,
    12,-45,35,-28,47,-18,-41,55,34,-69,-69,27,7,-18,-56,-25,47,-36,
    73,68,18,-99,25,-1,-44,-86,18,54,-73,8,47,-46,-100,69,74,19,-58,
    -32,23,14,72,74,-24,-54,-49,0,42,-32,82,57,-77,-6,-4,-97,35,91,
    51,77,-23,-15,63,5,35,-73,84,92,68,60,-32,-74,78,-35,19,87,75,
    89,17,-76,-10,59,13,-27,-44,26,-41,63,-99,-33,-80,64,8,-18,-42,
    -43,-77,27,-43,-71,-30,61,11,34,-32,67,90,-43,49,3,-58,-2,87,79,
    87,-73,-94,-61,-97,99,-24,82,-17,-38,87,-87,55,-30,-8,-4,-59,-21,
    92,31,89,-4,100,-76,-93,-100,-51,87,78,-53,69,-29,20,51,-69,-7,8,
    23,-31,69,65,-56,-32,-5,-22,29,-55,-77,-78,-20,65,-73,-50,-14,
    -15,80,-44,49,89,94,-13,-66,-36,0,-17,4,7,-99,88,-62,59,-55,-90,
    -60,-57,42,-13,88,-89,-93,-31,-39,46,-17,-25,100,43,43,-36,31,-44,
    44,7,80,-25,93,-86,-28,97,87,-93,-12,86,-81,-64,40,-74,-30,-58,34,
    85,-57,-77,-15,-22,-92,-89,65,7,-25,23,-66,-77,97,-12,18,-43,26,21,
    -24,-78,-12,-59,28,-94,-7,-24,-48,58,69,-75,34,-97,-89,62,53,-20,21,
    50,25,19,-1,18,-60,90,48,-74,34,50,72,-26,-37,-80,44,10,89,-94,86,
    81,-19,100,-96,-43,-75,-68,81,-1,72,96,-30,68,-45,22,34,-11,-70,-30,
    83,-82,39,-73,-30,68,68,40,-96,52,-73,-68,-44,-55,24,39,-57,85,52,
    92,-32,77,-1,36,55,72,-3,-76,-27,-46,-14,23,28,31,-73,-21,51,15,77,
    -10,50,-27,-99,-67,43,17,70,-35,83,-83,-51,-50,78,86,-91,39,-52,7,
    95,77,35,30,98,-88,-82,43,62,-81,29,-51,-33,48,58,-88,-13,-90,29,31,
    88,43,90,2,-83,35,64,63,24,-45,19,3,-4,52,35,-31,-41,-61,-20,32,-34,
    29,-72,30,47,-56,96,82,-48,-4,45,29,-29,1,-93,10,-66,-41,-32,-78,4,
    -45,38,43,61,-87,-7,-17,-75,-34,73,-64,96,40,96,-23,-75,1,3,-54,-13,
    -96,82,39,-63,-68,-94,30,-53,-62,-45,39,-31,95,-40,-63,-79,-76,10,
    -20,-48]
    
v = [1,2,3,4,5,6,7]
root = constructPBT(v)
connect(root)
print(root.left.right.next.val)      