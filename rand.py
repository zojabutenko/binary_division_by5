def prime(fn):
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper


class Divisibility5FSM:
    def __init__(self):
        self.q0 = self._create_q0()
        self.q1 = self._create_q1()
        self.q2 = self._create_q2()
        self.q3 = self._create_q3()
        self.q4 = self._create_q4()

        self.current_state = self.q0

    def send(self, digit):
        self.current_state.send(digit)

    def is_divisible(self):
        return self.current_state == self.q0

    @prime
    def _create_q0(self):
        while True:
            digit = yield
            if digit == 0:
                self.current_state = self.q0
            elif digit == 1:
                self.current_state = self.q1


    @prime
    def _create_q1(self):
        while True:
            digit = yield
            if digit == 1:
                self.current_state = self.q3
            elif digit == 0:
                self.current_state = self.q2


    @prime
    def _create_q2(self):
        while True:
            digit = yield
            if digit == 1:
                self.current_state = self.q0
            elif digit == 0:
                self.current_state = self.q4


    @prime
    def _create_q3(self):
        while True:
            digit = yield
            if digit == 1:
                self.current_state = self.q2
            elif digit == 0:
                self.current_state = self.q1


    @prime
    def _create_q4(self):
        while True:
            digit = yield
            if digit == 1:
                self.current_state = self.q4
            elif digit == 0:
                self.current_state = self.q3


class matchNumber:
    def __init__(self):
        self.match = self.match

    def match(number):
        evaluator = Divisibility5FSM()
        for i in number:
            evaluator.send(int(i))
        if evaluator.is_divisible():
            return 'true'
        else:
            return 'false'

PATTERN = matchNumber
string = input('input binary number: ')
print(PATTERN.match(string))

# PATTERN = '0+$+1((1+(0+11)(01*01)*01*0)0)*(0+11)(01*01)*1+(0+$+1((1+(0+11)(01*01)*01*0)0)*(0+11)(01*01)*1)(0+1((1+(0+11)(01*01)*01*0)0)*(0+11)(01*01)*1)*(0+$+1((1+(0+11)(01*01)*01*0)0)*(0+11)(01*01)*1)'
# PATTERN = '(0|1(((0|1{2})(01*01)*01*0|1)0)*(0|1{2})(01*01)*1)*'
# PATTERN = '0|1((1+(0+11)(01*01)*01*0)0)*(0+11)(01*01)*1+(0|1((1+(0+11)(01*01)*01*0)0)*(0+11)(01*01)*1)(0+1((1+(0+11)(01*01)*01*0)0)*(0+11)(01*01)*1)*(0+|1((1+(0+11)(01*01)*01*0)0)*(0+11)(01*01)*1)'
