def get_indices_of_item_weights(weights, length, limit):    
    index = 0
    value_1 = -1
    value_2 = -1
    dic = {}

    for i in range(0, length):
        if weights[i] not in dic.keys():
            dic[weights[i]] = [i]
        else:
            dic[weights[1]].append(i)
    
    while value_2 not in weights:
        index += 1
        if index >= length:
            return None
        value_1 = weights[index]
        value_2 = limit - value_1

    if value_1 == value_2:
        return((dic[value_1][1], dic[value_1][0]))
    else:
        return((dic[value_2][0], dic[value_1][0]))
