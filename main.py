import cellularAutomaton
import cellularAutomatonSimulation


def main():

    cs = cellularAutomatonSimulation.CellularAtomatonSimulation("47", "40")

    ca = cellularAutomaton.CellularAutomaton(cell_count = 41,
                   init_pattern = "00000000000000000000100000000000000000000",
                   rule = 222,
                   iterations = 20,
                   on_change = cs.print_ca)

    ca.start()


main()
