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
b = marshal.loads


def hello(*aa):
    __ = b(*aa)
    dis.dis(__)
    return __
    __import__("sys").exit


def kontol(*aa):
    __ = b(*aa)
    # print(f"{aa[0]}") # Simple Code for Dump Marshal
    print(f"exec(__import__('marshal').loads({aa[0]}))")  # Just understand it yourself
    return __


if mode == 1:
    marshal.loads = hello
else:
    marshal.loads = kontol
# exec(__)
