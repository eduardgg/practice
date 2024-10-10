def trap(h):
    max_esquerra = [0]*len(h)
    max_dreta = [0]*len(h)
    for i in range(1,len(h)):
        max_esquerra[i] = max(max_esquerra[i-1],h[i-1])
        max_dreta[len(h)-1-i] = max(max_dreta[len(h)-i],h[len(h)-i])
    aigua = 0
    for i in range(1,len(h)-1):
        alt_max = min(max_esquerra[i],max_dreta[i])
        aigua += max(alt_max-h[i],0)
    return aigua

height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
height2 = [4,2,0,3,2,5]
print(trap(height1))
print(trap(height2))