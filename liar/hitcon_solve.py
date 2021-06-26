import angr
p = angr.Project("/home/kddc/Downloads/liar")
ex = p.surveyors.Explorer(find=(0x00000000000009B0, ))
ex.run()
print (ex.found[0].state.posix.dumps(0))