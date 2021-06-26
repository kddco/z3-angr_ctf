import angr
import claripy

def main():
    project = angr.Project("/home/kddc/Downloads/liar")
    init_state = project.factory.entry_state()
    sm = project.factory.simulation_manager(init_state)
    sm.explore(find=0x00000000000009B0)
    found = sm.found[0]
    solution = found.solver.eval(cast_to=bytes)
    return solution


if __name__ == '__main__':
    print(repr(main()))