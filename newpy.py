#!/usr/bin/env python
if __name__ == "__main__":
    fn = input("Name of new python file (minus .py): ")
    fn += ".py"
    with open(fn, "w") as f:
        f.write("#!/usr/bin/env python")
