def steps(full, goal, start_bucket, not_start_bucket, guiding, buckets, actions):
    starting_index = guiding.index(start_bucket)
    not_starting_index = guiding.index(not_start_bucket)
    if buckets[starting_index] == 0:
        buckets[starting_index] = full[starting_index]
        actions.append(list(buckets))
    if buckets[not_starting_index] == full[not_starting_index]:
        buckets[not_starting_index] = 0
        actions.append(list(buckets))
    if buckets[not_starting_index] != full[not_starting_index]:
        buckets[not_starting_index] = buckets[not_starting_index] + buckets[starting_index]
        if buckets[not_starting_index] > full[not_starting_index]:
            spare = buckets[not_starting_index] - full[not_starting_index]
            buckets[not_starting_index] = full[not_starting_index]
            buckets[starting_index] = spare
        else:
            buckets[starting_index] = 0
        actions.append(list(buckets))
        if goal in buckets:
            which_bucket = guiding[buckets.index(goal)]
            buckets.remove(goal)
            return (len(actions), which_bucket, buckets[0])
    if buckets in actions[:-1]:
        raise ValueError("It's not possible to reach the goal!")
    return steps(full, goal, start_bucket, not_start_bucket, guiding, buckets, actions)

def measure(bucket_one, bucket_two, goal, start_bucket):
    actions = []
    buckets = [0, 0]
    if goal > bucket_one and goal > bucket_two:
        raise ValueError("Goal is larger than both buckets!")
    if bucket_one > bucket_two:
        guiding = ["one", "two"]
        full = [bucket_one, bucket_two]
    else:
        guiding = ["two", "one"]
        full = [bucket_two, bucket_one]
    if start_bucket == "one":
        not_start_bucket = "two"
        buckets[guiding.index("one")] = bucket_one
        actions.append(list(buckets))
        if goal in buckets:
            return (1, start_bucket, 0)
        if goal == bucket_two:
            buckets[guiding.index("two")] = bucket_two
            actions.append(list(buckets))
            return (2, "two", bucket_one)
        return steps(full, goal, start_bucket, not_start_bucket, guiding, buckets, actions)
    else:
        not_start_bucket = "one"
        buckets[guiding.index("two")] = bucket_two
        actions.append(list(buckets))
        if goal in buckets:
            return (1, start_bucket, 0)
        if goal == bucket_one:
            buckets[guiding.index("one")] = bucket_one
            actions.append(list(buckets))
            return (2, "one", bucket_two)
        return steps(full, goal, start_bucket, not_start_bucket, guiding, buckets, actions)