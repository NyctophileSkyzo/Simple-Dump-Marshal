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
    __ = b(aa[0])
    dis.dis(__)
    __import__("sys").exit()


def kontol(*aa):
    __ = b(aa[0])
    marshalled_code = marshal.dumps(__)
    for _ in range(150):
        print(f"exec(__import__('marshal').loads({repr(marshalled_code)}))")
    dis.dis(__)
    __import__("sys").exit()


if mode == 1:
    marshal.loads = hello
else:
    marshal.loads = kontol
exec(__)
