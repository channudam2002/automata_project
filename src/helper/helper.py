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
    

    
# NFA to DFA
class NFA:
    def __init__(self, states, alphabet, transitions, initial_state, accepting_states):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = set(accepting_states)

    def epsilon_closure(self, states):
        """
        Returns the epsilon closure of the given set of states.
        """
        closure = set(states)
        stack = list(states)
        while stack:
            state = stack.pop()
            for epsilon_transition in self.transitions.get((state, None), []):
                if epsilon_transition not in closure:
                    closure.add(epsilon_transition)
                    stack.append(epsilon_transition)
        return closure

    def to_dfa(self):
        """
        Converts the NFA to a DFA using the subset construction algorithm.
        """
        dfa_states = []
        dfa_transitions = {}
        dfa_initial_state = frozenset(self.epsilon_closure([self.initial_state]))
        dfa_accepting_states = set()
        unmarked_states = [dfa_initial_state]

        while unmarked_states:
            state_set = unmarked_states.pop()
            dfa_states.append(state_set)

            for symbol in self.alphabet:
                next_states = set()
                for state in state_set:
                    for transition in self.transitions.get((state, symbol), []):
                        next_states |= self.epsilon_closure([transition])
                if next_states:
                    next_state_set = frozenset(next_states)
                    dfa_transitions[(state_set, symbol)] = next_state_set
                    if next_state_set not in dfa_states:
                        unmarked_states.append(next_state_set)

            if any(state in self.accepting_states for state in state_set):
                dfa_accepting_states.add(state_set)

        return DFA(
            alphabet=self.alphabet,
            states=dfa_states,
            transitions=dfa_transitions,
            initial_state=dfa_initial_state,
            accepting_states=dfa_accepting_states
        )

class DFA:
    def __init__(self, alphabet, states, transitions, initial_state, accepting_states):
        self.alphabet = alphabet
        self.states = states
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def accepts(self, input_string):
        """
        Determines whether the DFA accepts the given input string.
        """
        current_state = self.initial_state
        for symbol in input_string:
            current_state = self.transitions.get((current_state, symbol))
            if current_state is None:
                return False
        return current_state in self.accepting_states

# Define the NFA from the given example
states = ["q1", "q2", "q3"]
alphabet = ["a", "b"]
transitions = {
    ("q1", "a"): {"q1", "q2"},
    ("q1", "b"): {"q1"},
    ("q2", "a"): set(),
    ("q2", "b"): {"q3"}
}
initial_state = "q1"
accepting_states = ["q2"]
nfa = NFA(states, alphabet, transitions, initial_state, accepting_states)

# Convert NFA to DFA
dfa = nfa.to_dfa()


# Print the resulting DFA
print("\n_____Here we have our DFA_____\n")
print("Alphabet: ", dfa.alphabet)
print("States: ", dfa.states)
print("Transitions: ", dfa.transitions)
print("Initial state: ", dfa.initial_state)
print("Accepting states: ", dfa.accepting_states)