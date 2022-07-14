import sys


def getPairs(num_arr, sum):
    hash_map, pairs = {}, []
    for i in range(len(num_arr)):
        if sum - num_arr[i] in hash_map:
            pairs.append(str(num_arr[i]) + ',' + str(sum-num_arr[i]))
        if num_arr[i] in hash_map:
            hash_map[num_arr[i]] += 1
        else:
            hash_map[num_arr[i]] = 1
    return pairs


int_array = []
for e in sys.argv[1].split(","):
    int_array.append(int(e))
print('Pairs are', getPairs(int_array, int(sys.argv[2])))
