
def nums(low, high):
    final = [i for i in range(low, high, 1) if (i % 2 == 0 and i % 3 != 0) or (i % 3 == 0 and i % 2 != 0)]
    return final


if __name__ == '__main__':
    print(nums(1,10))
