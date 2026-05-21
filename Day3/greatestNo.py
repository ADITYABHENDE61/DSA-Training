def findBiggestNumber(SampleArray):      #==========
    biggestNumber = SampleArray[0]        #==========O(1)
    for i in range(1,len(SampleArray)):      #==========O(n)
        if SampleArray[i]>biggestNumber:       #==========O(1)
            biggestNumber = SampleArray[i]        #==========O(1)
    print(biggestNumber)                             #==========O(1)

SampleArray = [5,3,7,9,2]
findBiggestNumber(SampleArray)