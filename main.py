import cellularAutomaton
import cellularAutomatonSimulation


def main():

    cs = cellularAutomatonSimulation.CellularAtomatonSimulation("47", "40")

    ca = cellularAutomaton.CellularAutomaton(cell_count = 41,
                   init_pattern = "10100000000000000000100000000000000000011",
                   rule = 129,
                   iterations = 30,
                   on_change = cs.print_ca)

    ca.start()


main()
