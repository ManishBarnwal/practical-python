# bounce.py
#
# Exercise 1.5
height = 100  # metres
num_bounces = 10
i = 1

while i <= num_bounces:
    height = height * 3/5
    print(i, round(height, 4))
    i = i + 1
