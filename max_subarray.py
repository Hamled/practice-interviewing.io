#!/usr/bin/env python3

def max_subarray(ns):
    sums = []
    current = 0  # Current subarray sum
    cost = 0  # Cost to merge w/ last subarray sum
    for n in ns:
        if n < 0:  # end of a positive subarray
            cost -= n
            continue

        if current > 0:
            sums.append(current)

        if current - cost < 0:  # cannot merge
            current = n
        else:  # merge positive subarrays
            current += n - cost

        cost = 0

    if current > 0:
        sums.append(current)

    # No positive subarrays, so the max is
    # the single entry with highest value
    if len(sums) == 0:
        return max(ns)

    return max(sums)
