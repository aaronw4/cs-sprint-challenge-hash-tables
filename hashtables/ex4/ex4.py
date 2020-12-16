def has_negatives(a):
    dic = {}

    for i in range(0, len(a)):
        number = abs(a[i])
        if number not in dic.keys():
            dic[number] = False
        else:
            dic[number] = True
    
    num_list = list(dic.items())
    num_list.sort(reverse=True, key=lambda tupl: tupl[1])
    index = 0
    result = []

    while num_list[index][1] is True:
        result.append(num_list[index][0])
        index += 1
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
