# bad bad code

def read_two_numbers():
    return [int(num_string) for num_string in raw_input().split()]


def update_id_set(id_sets, first_id, second_id):
    first = -1
    for first_index in xrange(len(id_sets)):
        id_set = id_sets[first_index]
        if first_id in id_set:
            id_set.add(first_id)
            first = first_index
            break

    second = -1
    for second_index in xrange(len(id_sets)):
        id_set = id_sets[second_index]
        if second_id in id_set:
            id_set.add(second_id)
            second = second_index
            break

    if first == -1 and second == -1:
        id_sets.append(set([first_id, second_id]))
    elif first == -1:
        id_sets[second].add(first_id)
    elif second == -1:
        id_sets[first].add(second_id)
    elif first != second:
        if len(id_sets[first]) > len(id_sets[second]):
            id_sets[first].update(id_sets[second])
            del id_sets[second]
        else:
            id_sets[second].update(id_sets[first])
            del id_sets[first]

            
def choose_two(n):
    return n * (n-1) / 2;            
            

def calculate_num_ways(lengths, indexes_not_mentioned, indexes_mentioned, num_astronauts):
    num_not_mentioned = len(indexes_not_mentioned)
    if num_not_mentioned > 3000 and num_not_mentioned >= num_astronauts * 0.99:
        num_ways = 0
        #print indexes_mentioned
        for i in indexes_mentioned:
            for j in indexes_mentioned:
                if i > j:
                    #print 'dd', indexes_mentioned, lengths[i], lengths[j]
                    num_ways += lengths[i] * lengths[j]
        #print 'fuck', num_ways
        num_ways += num_not_mentioned * 1 * sum([length for length in lengths if length != 1])
        num_ways += choose_two(num_not_mentioned) * 1 * 1
            
        return num_ways
    else:
        num_ways = 0
        for i in xrange(len(lengths)):
            for j in xrange(i+1, len(lengths)):
                num_ways += lengths[i] * lengths[j]
        #print num_ways, id_sets
        return num_ways


def solve(num_astronauts, num_groups):
    id_sets = []
    ids_mentioned = [False] * num_astronauts
    for i in xrange(num_groups):
        first_id, second_id = read_two_numbers()
        update_id_set(id_sets, first_id, second_id)
        ids_mentioned[first_id] = True
        ids_mentioned[second_id] = True

    num_not_mentioned = 0
    indexes_not_ones = []
    indexes_ones = []
    for astronaut_id in xrange(len(ids_mentioned)):
        if not ids_mentioned[astronaut_id]:
            id_sets.append(set([astronaut_id]))
            num_not_mentioned += 1

    lengths = map(len, id_sets)
    for index in xrange(len(lengths)):
        if lengths[index] == 1:
            indexes_ones.append(index)
        else:
            indexes_not_ones.append(index)
    
    return calculate_num_ways(lengths, indexes_ones, indexes_not_ones, num_astronauts)


num_astronauts, num_groups = read_two_numbers()
print solve(num_astronauts, num_groups)
