from re import I


def hashList(list):
    list.sort()

    s = "_"

    for item in list:
        s += item + '_'

    # print('Hash for' + str(list) + ':' + s)

    return s


def intersect(l1, l2):
    l = []

    for item in l1:
        if item in l2:
            l += [item]

    return l


def mapper(person: str, friendList: list):
    result = {}

    for friend in friendList:
        key = [person, friend]
        value = []

        if hashList(key) in result:
            continue

        for f in friendList:
            if f != friend:
                value += [f]

        result[hashList(key)] = value

    return result


def reducer(d1: dict, d2: dict) -> dict:
    result = {}

    for key in d1.keys():
        if key not in d2:
            result[key] = d1[key]
        else:
            result[key] = intersect(d1[key], d2[key])

    return result


if __name__ == '__main__':
    data = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D']
    }

    maps = []

    for person in data.keys():
        tmp = mapper(person, data[person])
        maps += [tmp]

    print(maps)

    while len(maps) > 1:
        m1 = maps.pop(0)
        m2 = maps.pop(0)
        maps.append(reducer(m1, m2))

    if maps:
        for key in maps[0]:
            substrs = key.split('_')

            for s in substrs:
                if len(s) == 0:
                    substrs.remove(s)

            print(str(substrs) + ' <--> ' + str(maps[0][key]))
