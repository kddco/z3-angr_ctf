import angr
import claripy

def main():
    project = angr.Project("/home/kddc/Downloads/liar")
    init_state = project.factory.entry_state("/home/kddc/Downloads/liar")
    sm = project.factory.simulation_manager(init_state)
    sm.explore(find=0x00000000000009B0)
    sm.run()
    return sm.found[0].state.posix.dumps(0)


if __name__ == '__main__':
    print(repr(main()))