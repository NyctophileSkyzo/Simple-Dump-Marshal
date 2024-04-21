import marshal
import dis

__import__("os").system("cls" if "win" in __import__("sys").platform.lower() else "clear")

print(
    f"""# Simple Code for Dump Marshal
# Coded by: Denventa Khurayra X.\n"""
)
a = input(f"File path: ")
mode = int(input(f"Mode 1\\2: "))
with open(a, "r") as tai:
    __ = tai.read()
x = marshal.loads
xx = exec


def dump(*aa):
    __ = x(aa[0])
    dis.dis(__)
    print(f"{aa[0]}")
    return __  # or (#) return __
    __import__("sys").exit()


def print_dump(*bb):
    __ = x(bb[0])
    dis.dis(__)
    marshalled_code = marshal.dumps(__)
    print(f"exec(__import__('marshal').loads({repr(marshalled_code)}))")
    return __
    __import__("sys").exit()


if mode == 1:
    marshal.loads = dump
else:
    marshal.loads = print_dump
exec(__)
