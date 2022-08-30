import sys
print("sys.argv: ", len(sys.argv), " elements:")

for arg in sys.argv:
    print(" - ", arg)
print()
print("__name__: ", __name__)

