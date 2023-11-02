#!/usr/bin/python3
import dis
import imp
if __name__ == '__main__':
    module = imp.load_source("hidden_4", "hidden_4.pyc")
    inst = dis.get_instructions(module)
    names = set()
    for ins in inst:
        if ins.opcod == dis.opmap["LOAD_NAME"]:
            name = ins.arg
            if not name.startswith("__"):
                names.add(name)
    for name in sorted(names):
        print(name)
