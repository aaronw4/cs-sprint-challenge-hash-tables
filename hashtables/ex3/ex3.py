def intersection(arrays):
    dic = {}

    for i in range(0, len(arrays)):
        index = 0
        while index != len(arrays[i]):
            if arrays[i][index] not in dic.keys():
                dic[arrays[i][index]] = 1
            else:
                number = dic[arrays[i][index]]
                number += 1
                dic[arrays[i][index]] = number
            index += 1
    
    num_list = list(dic.items())
    num_list.sort(reverse=True, key=lambda tupl: tupl[1])
    index = 0
    biggest = num_list[index][1]
    result = []

    while biggest == len(arrays):
        result.append(num_list[index][0])
        index += 1
        if index == len(num_list):
            break
        biggest = num_list[index][1]    

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
