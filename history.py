
class History(object):
    def __init__(self): #초기화 함수!
        self._stack_undo = [] #스택 두개를 초기화
        self._stack_redo = []
        pass
    
    def __str__(self):
        pass

    @property
    def current_state(self): #현재상태 반환하는데 그중에서도
        if self._stack_undo: #이 스택안의 최상단 객체를 반환
            return self._stack_undo[-1]
        else:
            return None
        pass

    def append(self, state): #스택안에 새로운 상태를 추가하는데
        self._stack_undo.append(state) #undo스택에 state를 추가하고
        self._stack_redo=[] #redo스택을 비운다!
        pass

    def undo(self): #이전으로 되돌리는 함수!!
        if self._stack_undo: #이 undo 스택에서 최상단 객체를
            state = self._stack_undo.pop() #꺼내서
            self._stack_redo.append(state) #이 redo스택에 state를 추가!
        pass
    
    def redo(self): #취소했던 작업을 다시 실행하는 함수!
        if self._stack_redo: #redo스택에서 최상단객체를
            state = self._stack_redo.pop() #꺼내서!!
            self._stack_undo.append(state) #undo스택에 state를 추가추가!!
        pass
    
    def clear(self): #스택을 비우는 함수
        self._stack_undo.clear()
        self._stack_redo.clear()
        pass