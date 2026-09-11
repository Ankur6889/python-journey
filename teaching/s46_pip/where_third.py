import sys
import json
import numpy
import rclpy

print(json.__file__)
print(numpy.__file__)
print(rclpy.__file__)
print()
for i, folder in enumerate(sys.path):
    print(i, folder)
