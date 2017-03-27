#http://stackoverflow.com/questions/30802269/merging-2d-slices-into-3d-volume-in-python
#You should evaluate distance and angle between every dot at first slice and every dot at the last, when for every step you should linear decrease distance with constant angle.
A = np.zeros((100,100,100))
A[0,25:75,25:75] = 1
A[99,50,50] = 1

from math import sin, cos, atan2
dim = 100
for i99,j99 in np.swapaxes(np.where(A[dim-1]==1),0,1):
    for i0,j0 in np.swapaxes(np.where(A[0]==1),0,1):
        di = (i0-i99)
        dj = (j0-j99)
        dist = (di**2 + dj**2)**0.5
        ang = atan2(dj,di)
        for t in range(1,dim-1):
            ndist = dist * (1 - t/dim)
            pi = round(sin(ang)*ndist) + i99
            pj = round(cos(ang)*ndist) + j99
            A[t][pi][pj] = 1