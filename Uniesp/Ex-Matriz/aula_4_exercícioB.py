def main():

    array = [[39, 14, 27],
             [21, 83, 92],
             [31, 12, 43]]

    for i in range(len(array)):
        for j in range(len(array[i])):
            print("{} * 7 = {}".format(array[i][j],array[i][j]*7))
            #print(array[i][j]*7)

main()