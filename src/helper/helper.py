class FiniteAutomata:

    def __init__(self, alphaArr, stateNum, stateArr, finalStateArr, startStateArr, tranFuncObj) -> None:
        self.stateNum = stateNum
        self.stateArr = stateArr
        self.finalStateArr = finalStateArr
        self.startStateArr = startStateArr
        self.tranFuncObj = tranFuncObj
        self.alphaArr = alphaArr

    def processString(self, stateArr, stringArr, firstState, finalStateArr):
        # Make first state become the first element in list states
        stateArr.remove(firstState)
        stateArr.insert(0, firstState)
        stringggg = ''
        count = 0
        K = [0 for i in range(len(stateArr))]  # k = [0, 0, 0]
        # input transition
        for i in range(len(stateArr)):
            K[i] = [0 for j in range(len(stringArr))]  # k[i] = [0, 0]
            for j in range(len(stringArr)):
                K[i][j] = input('From ' + stateArr[i] + ' by ' + stringArr[j] + ' go: ')

        def spot(q, w):
            lis.append(K[stateArr.index(q)][stringArr.index(w)])
            return K[stateArr.index(q)][stringArr.index(w)]
        while True:
            lis = []
            str = stateArr[0]
            w = input('Input string to check: ')
            for i in w:
                str = spot(str, i)
            if len(finalStateArr) == 1:
                for i in finalStateArr:
                    stringOfFinalState = i
                if lis[-1] == stringOfFinalState:
                    stringggg = 'STRING ACCEPT BY DFA (' + stateArr[0] + '-->' + '-->'.join(lis) +')'
                else:
                    stringggg = 'STRING NOT ACCEPT BY DFA'
            else:
                for i in finalStateArr:
                    if (lis[-1] == i):
                        count = count + 1
                if (count == 0):
                    stringggg = 'STRING NOT ACCEPT BY DFA'
                    count = 0
                else:
                    stringggg = 'STRING ACCEPT BY DFA (' + stateArr[0] + '-->' + '-->'.join(lis) +')'
                    count = 0
        return stringggg

    def minFa(self):
        accessableStateCollection = self.accessableStateFilter()
        pairStateArr = self.paringState()
        newPairStateArr = []
        disStateArr = self.paireStateContainFinalFilter()
        for pairState in pairStateArr:
            iter = 0
            for alpha in self.alphaArr:
                arr = []
                for state in pairState:
                    arr.append(accessableStateCollection.accessableStateObj[state][alpha])
                for disState in disStateArr:
                    if arr == disState:
                        disStateArr.append(pairState)
                        pairState_re = pairState.copy()
                        pairState_re.reverse()
                        iter_0 = 0
                        for disState_1 in disStateArr:
                            if disState_1 == pairState_re:
                                iter_0 = 1
                                break
                        if iter_0 == 0:
                            disStateArr.append(pairState_re)
                        iter = 1
                        break
                if iter == 1: break
        for pairState in pairStateArr:
            if pairState in disStateArr:
                pairStateArr.remove(pairState)
        for pairState in pairStateArr:
            isFinal = 0
            for state in pairState:
                for finalState in self.finalStateArr:
                    if state == finalState:
                        isFinal = 1
            if isFinal == 0:
                newPairStateArr.append(pairState)
        for pairState in newPairStateArr:
            if pairState[0] == pairState[1]:
                newPairStateArr.remove(pairState)
        for state in newPairStateArr:
            state_re = state.copy()
            state_re.reverse()
            for state_0 in newPairStateArr:
                if state_re == state_0:
                    newPairStateArr.remove(state_0)
                    break
        return newPairStateArr

    def accessableStateFilter(self):
        alphaArr = self.alphaArr
        tranFuncObj = self.tranFuncObj
        statStateArr = self.startStateArr
        accessableStateArr = []
        accessableStateObj = {}
        flag = 1
        for state in tranFuncObj:
            tempStateArr = []
            for alpha in alphaArr:
                tempStateArr.append(tranFuncObj[state][alpha])
            for tempState in tempStateArr:
                if len(tempStateArr) > 0:
                    for accessableState in accessableStateArr:
                        if accessableState == tempState:
                            flag = 0
                            break
                        else: flag = 1
                    if flag == 1: accessableStateArr.append(tempState)
                else: accessableStateArr.append(tempState)
        for startState in statStateArr:
            accessableStateArr.append(startState)
        for accessableState in accessableStateArr:
            for stateObj in tranFuncObj:
                if accessableState == stateObj:
                    accessableStateObj[accessableState] = tranFuncObj[stateObj]
        return {
            "accessableStateArr": accessableStateArr,
            "accessableStateObj": accessableStateObj
        }
    
    def paringState(self):
        accessableStateCollection = self.accessableStateFilter()
        pairStateArr = []
        for rowState in accessableStateCollection.accessableStateArr:
            for colState in accessableStateCollection.accessableStateArr:
                pairState = []
                pairState.append(rowState)
                pairState.append(colState)
                pairStateArr.append(pairState)
        return pairStateArr

    def paireStateContainFinalFilter(self):
        pairStateArr = self.paringState()
        finalStateArr = self.finalStateArr
        disStateArr = []
        isFinal = 0
        for index in range(len(pairStateArr)):
            for state in pairStateArr[index]:
                for finalState in finalStateArr:
                    if state == finalState:
                        isFinal = 1
                    else: isFinal = 0
                if isFinal == 1 :
                    disStateArr.append(pairStateArr[index])
                    break
        return disStateArr
    

    