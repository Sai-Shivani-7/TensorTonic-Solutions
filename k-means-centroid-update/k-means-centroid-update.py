def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    
    d = {}

    for i in range(k):
        d[i] = []
    for j in range(len(points)):
        x = assignments[j]
        d[x].append(points[j])

    l=[]
    for v in d.values():
        if len(v) == 0:
            l.append([0.0] * len(points[0]))
            continue
        b = [0.0]*len(v[0])
        for p in v:
            for c in range(len(p)):
                b[c]+=p[c]
        for c in range(len(b)):
            b[c] /= len(v)
        l.append(b)
    return l

        