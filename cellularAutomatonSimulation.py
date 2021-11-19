class CellularAtomatonSimulation(object):


    def __init__(self, dead_cell, alive_cell):


        self.dead_cell = "\033[0;" + dead_cell + "m \033[0m"
        self.alive_cell = "\033[0;" + alive_cell + "m \033[0m"

    def print_ca(self, ca):

        if ca.iteration == 0:
            self.show_properties(ca)

        print(str(ca.iteration).ljust(2) + " ", end='')

        for c in ca.cells:

            if c == "0":
                print(self.dead_cell, end='')
            else:
                print(self.alive_cell, end='')

        print("")

    def show_properties(self, ca):

        print("number of cells:   " + str(ca.cell_count))
        print("initial pattern: " + ca.init_pattern)
        print("rule:         " + str(ca.rule))
        print("iterations:   " + str(ca.iterations) + "\n")
