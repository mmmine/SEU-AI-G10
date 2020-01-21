import Util

x = Util.getCategory()

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


if next(x):
    print("true")
else:
    print("false")

try:
    print(next(x))
except StopIteration:
    print("stop")

try:
    print(next(x))
except StopIteration:
    print("stop")
