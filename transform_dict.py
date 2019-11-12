# Distance between two words
def distance(a, b):
    return sum([int(ord(ac) == ord(bc)) for ac, bc in zip(list(a), list(b))])


# Create a map for each word with the list of other words in the set
# which are the given distance from the key word
def dist_map(words, dist):
    dist_map = {}
    for w in words:
        dist_map[w] = [y for y in words if distance(w, y) == dist]

    return dist_map


# Shortest path? Technically we only need to find if there *is* a path
# so there might be a simpler way to do this.

# For shortest path, should use something like A* with the edge weight
# being the relative difference in distance from current word to the
# target word

# But I don't know A* actually, so I'm going to just try a DFS that
# prioritizes in order of the edge weight, hopefully that's close
# I think the real thing might use the sum of all the edge weights from
# the word on the other side of each edge, when calculating the weights
# of that edge. I also think they might say 'cost' instead of 'weight' --
# either way we want to minimize that value for the shortest path.

# So lets find any path at all
def has_path(start, end, dist, dmap, visited):
    if dist < 2:
        return True

    visited.add(start)
    words = dmap[start]
    dists = [(w, distance(w, end)) for w in words]
    for w, d in sorted(dists, key=lambda t: t[1] - dist):
        if w in visited:
            continue
        if has_path(w, end, d, dmap, visited):
            return True
    return False


def is_transformable(start, end, d):
    dmap = dist_map(d + [start, end], 1)
    return has_path(start, end, distance(start, end), dmap, set())
