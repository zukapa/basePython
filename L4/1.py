from sys import argv
script_name, time, rate, reward = argv
print((float(time) * int(rate)) + int(reward))
