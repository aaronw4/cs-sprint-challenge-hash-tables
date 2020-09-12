def finder(files, queries):
    dic = {}

    for i in range(0, len(files)):
        split_file = files[i].split('/')
        if split_file[-1] not in dic.keys():
            dic[split_file[-1]] = [files[i]]
        else:
            dic[split_file[-1]].append(files[i])
    
    result = []
    
    for i in range(0, len(queries)):
        if queries[i] not in dic.keys():
            pass
        else:
            for index in range(0, len(dic[queries[i]])):
                result.append(dic[queries[i]][index])
    
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
