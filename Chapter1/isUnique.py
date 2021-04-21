import collections

def isUnique(str):
    letters_dict = collections.defaultdict(int)
    for characters in str:
        letters_dict[characters] += 1

    print(letters_dict)
    for key, value in letters_dict.items():
        if value > 1:
            return False

    return True

if __name__ == "__main__":
    print(isUnique('thisissparta'))
    print(isUnique('Unique'))
    print(ord('b'))