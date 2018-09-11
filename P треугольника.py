def dist(x1, y1, x2, y2, x3, y3):
    dist1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    dist2 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** (1 / 2)
    dist3 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** (1 / 2)
    return dist1, dist2, dist3


def perim(dist1, dist2, dist3):
    p = dist1 + dist2 + dist3
    return p


dists = dist(float(input()), float(input()), float(input()),
             float(input()), float(input()), float(input()))

print(perim(dists[0], dists[1], dists[2]))
