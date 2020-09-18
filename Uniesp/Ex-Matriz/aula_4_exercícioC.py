def main():

    array = [[39, 14, 27],
             [21, 83, 92],
             [31, 12, 43]]

    for i in range(0, len(array)):
        array[i].remove(array[i][2])
        print(array[i])


main()