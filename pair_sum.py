def pair_sum(arr, k):

    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:

        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target,num),max(target,num)))

    return '\n'.join(map(str,list(output)))

print pair_sum([1,3,2,2],4)
