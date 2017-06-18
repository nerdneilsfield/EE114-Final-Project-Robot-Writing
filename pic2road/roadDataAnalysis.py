import sys 





def roadreduce(inputData):
    """fuck"""
    dataInput = len(inputData)

    # print("Have Read %d data" % dataInput)

    data = []
    data2 = []

    # for i in inputData:
    #     tup = (int(i[1]), int(i[2]))
    #     if (inputData.index(i) >= 2):
    #         temp1 = data[-2]
    #         temp = data[-1]
    #         if((temp[0] - tup[0] < 2) and (temp[1] - tup[1] < 2) \
    #             and temp1[0] - tup[0] > 2 and temp1[1] - tup[1] > 2):
    #             del data[-1]
    #     data.append(tup)

    for i in inputData:
        ha = i.split()
        tup = (int(ha[0]), int(ha[1]))
        if (inputData.index(i) >= 2):
            temp1 = data2[-2]
            temp = data2[-1]
            if((temp[0] - tup[0] < 2) and (temp[1] - tup[1] < 2)):
                del data2[-1]
        data2.append(tup)

    # print(data2)
    # print(len(data))
    last = data2[0]
    for data in data2:
        maxTime = max(abs(last[0]-data[0]), abs(last[1] - data[1]))
        last = data
        print("%d %d %d" % (data[0], data[1], maxTime * 30+300))

inputData = sys.stdin.readlines()
roadreduce