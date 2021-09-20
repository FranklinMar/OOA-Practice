import sys


def max_weight(capacity, weights, index=0):
    if capacity == 0 or index >= len(weights):
        return 0
    elif int(weights[index]) > capacity:
        return max_weight(capacity, weights, index + 1)
    else:
        return max(max_weight(capacity, weights, index + 1),
                   int(weights[index]) + max_weight(capacity - int(weights[index]), weights, index + 1))


boolean = 1
for string in sys.argv[1:]:
    if not string.isdigit():
        boolean = 0
        break

if boolean:
    print("Capacity: ", sys.argv[1])
    print("Max Weight: ", max_weight(int(sys.argv[1]), sys.argv[2:]))
