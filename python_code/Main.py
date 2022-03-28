import sys
import time
from ClosestPair import ClosestPair
#'''
print("test1")
fp = open("test1.txt", 'r')
lines = fp.readlines()
points = []
for line in lines:
    points.append(line.strip())


# Call the closest_pair function passing in the
# contents of the file
start = time.time()
cp = ClosestPair()
print(cp.compute(points))
end = time.time()
print("time: "+ str(end-start))

print("test2")
fp = open("test2.txt", 'r')
lines = fp.readlines()
points = []
for line in lines:
    points.append(line.strip())


# Call the closest_pair function passing in the
# contents of the file
start = time.time()
cp = ClosestPair()
print(cp.compute(points))
end = time.time()
print("time: "+ str(end-start))

print("20s")
fp = open("20s.txt", 'r')
lines = fp.readlines()
points = []
for line in lines:
    points.append(line.strip())


# Call the closest_pair function passing in the
# contents of the file
start = time.time()
cp = ClosestPair()
print(cp.compute(points))
end = time.time()
print("time: "+ str(end-start))


print("horizontal")
fp = open("horizontal.txt", 'r')
lines = fp.readlines()
points = []
for line in lines:
    points.append(line.strip())


# Call the closest_pair function passing in the
# contents of the file
start = time.time()
cp = ClosestPair()
print(cp.compute(points))
end = time.time()
print("time: "+ str(end-start))

print("median not in list")
fp = open("median not in list.txt", 'r')
lines = fp.readlines()
points = []
for line in lines:
    points.append(line.strip())


# Call the closest_pair function passing in the
# contents of the file
start = time.time()
cp = ClosestPair()
print(cp.compute(points))
end = time.time()
print("time: "+ str(end-start))

print("duplicate median")
fp = open("duplicate median.txt", 'r')
lines = fp.readlines()
points = []
for line in lines:
    points.append(line.strip())


# Call the closest_pair function passing in the
# contents of the file
start = time.time()
cp = ClosestPair()
print(cp.compute(points))
end = time.time()
print("time: "+ str(end-start))
#'''
print("basic")
fp = open("basic.txt", 'r')
lines = fp.readlines()
points = []
for line in lines:
    points.append(line.strip())


# Call the closest_pair function passing in the
# contents of the file
start = time.time()
cp = ClosestPair()
print(cp.compute(points))
end = time.time()
print("time: "+ str(end-start))
#'''
print("80k vertical")
fp = open("80k vertical.txt", 'r')
lines = fp.readlines()
points = []
for line in lines:
    points.append(line.strip())


# Call the closest_pair function passing in the
# contents of the file
start = time.time()
cp = ClosestPair()
print(cp.compute(points))
end = time.time()
print("time: "+ str(end-start))
#'''