
class CellularAutomaton(object):

    def __init__(self, cell_count, init_pattern, rule, iterations, on_change):

        self.cell_count = cell_count
        self.init_pattern = init_pattern
        self.rule = rule
        self.iterations = iterations
        self.on_change = on_change
        self.iteration = 0
        self.cells = []
        self.__next_state = []
        self.rule_binary = format(self.rule, '08b')

        for c in self.init_pattern:

            if c == "0":
                self.cells.append("0")
            elif c == "1":
                self.cells.append("1")

            self.__next_state.append("0")
        self.on_change(self)

    def start(self):


        neighbourhood = ""

        for i in range(0, self.iterations):

            self.iteration += 1

            self.__calculate_next_state()

            self.on_change(self)

# calculating next state
    def __calculate_next_state(self):

#0 is the first index
#self.cell_count -1 is the last index
        for c in range(0, self.cell_count - 1):

            if c == 0:
                prev_index = self.cell_count - 1
            else:
                prev_index = c - 1

            if c == (self.cell_count - 1):
                next_index = 0
            else:
                next_index = c + 1

# setting neighbourhood according to the rule stated by the user
            neighbourhood = self.cells[prev_index] + self.cells[c] + self.cells[next_index]

            if neighbourhood == "111":
                self.__next_state[c] = self.rule_binary[0]
            elif neighbourhood == "110":
                self.__next_state[c] = self.rule_binary[1]
            elif neighbourhood == "101":
                self.__next_state[c] = self.rule_binary[2]
            elif neighbourhood == "100":
                self.__next_state[c] = self.rule_binary[3]
            elif neighbourhood == "011":
                self.__next_state[c] = self.rule_binary[4]
            elif neighbourhood == "010":
                self.__next_state[c] = self.rule_binary[5]
            elif neighbourhood == "001":
                self.__next_state[c] = self.rule_binary[6]
            elif neighbourhood == "000":
                self.__next_state[c] = self.rule_binary[7]

        for c in range(0, self.cell_count):
            self.cells[c] = self.__next_state[c]
