def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    ans = []
    for p in points:
        best_dist = float('inf')
        best_idx=0
        for c in range(len(centroids)):
            q = centroids[c]
            sums = 0
            for i in range(len(q)):
                sums+=(p[i]-q[i])**2
            if sums<best_dist:
                best_dist = sums
                best_idx = c
        ans.append(best_idx)
    return ans
