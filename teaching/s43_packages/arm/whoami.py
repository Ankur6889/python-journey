import sys
print("my __name__ is:", __name__)
print("__main__" in sys.modules, "arm.whoami" in sys.modules)
