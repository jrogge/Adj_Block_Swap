import time

perm_bests = {}
solns = {}
iso_classes = []
def perform_swap(perm, operation):
    ''' swap the blocks [a:b] and [b:c] '''
    a = operation[0]
    b = operation[1]
    c = operation[2]
    before = perm[:a]
    first = perm[a:b]
    second = perm[b:c]
    after = perm[c:]
    return before + second + first + after

def check_perm(perm, len_ops):
    str_literal = str(perm)
    if not(str_literal in perm_bests):
        perm_bests[str_literal] = len_ops
        return True

    if len_ops < perm_bests[str_literal]:
        perm_bests[str_literal] = len_ops
        return True

    #print("We did something useful!")
    return False

def is_reversed(perm):
    for ind, elem in enumerate(perm):
        if elem != ind:
            return False
    return True

def rev_ops(operations, length):
    revd = []
    for op in operations:
        new_op = [length - op[0], length - op[1], length - op[2]]
        new_op.sort()
        revd.append(new_op)

    return revd

def test_swaps(depth, perm):
    height, route = test_swaps_helper(depth, perm, [], depth + 1)
    #print("================================")
    #print(height, route)
    return height

def test_swaps_helper(depth, perm, operations, curr_min):
    if depth <= 0:
        # failure placeholder
        return -1, []

    n = len(perm)
    # first and middle indices cannot be too close to end of list
    max_first = n-1
    max_middle = n
    max_last = n + 1
    # +1 as depth may in fact be the best we can do
    #curr_min = depth + len(operations) + 1
    best_ops = []

    for a in range(max_first):
        for b in range(a+1, max_middle):
            for c in range(b+1, max_last):
                op = [a,b,c]
                new_perm = perform_swap(perm, op)
                new_operations = operations + [op]
                # detect identity
                if is_reversed(new_perm):
                    height = len(new_operations)
                    print(height, new_operations)
                    if height < curr_min:
                        curr_min = height
                        best_ops = new_operations
                        solns[height] = []
                    if not (new_operations in solns[height]):
                        iso_classes[height] += 1
                        solns[height].append(new_operations)
                        reversed_ops = rev_ops(new_operations, len(new_perm))
                        #print("reversed:", reversed_ops)
                        solns[height].append(reversed_ops)
                    #print()
                elif check_perm(new_perm, len(new_operations)):
                #else:
                    poss_min, poss_ops = test_swaps_helper(depth - 1, new_perm,
                            new_operations, curr_min)
                    if poss_min == -1:
                        pass
                    elif poss_min < curr_min:
                        curr_min = poss_min
                        best_ops = poss_ops
    return curr_min, best_ops

num = 10
depth = 6

# reversed list of numbers from 0 to num - 1
test_list = list(range(num))[::-1]
iso_classes = [0] * (depth + 1)

start = time.time()
min_height = test_swaps(depth, test_list)
end = time.time()

print()
for op in solns[min_height]:
    print(op)
print("iso classes:", iso_classes[min_height])

#print("elapsed:", end - start)
