import math

people = int(input("Input the number of people: "))

# get the highest power of 2 below the input number
power = math.floor(math.log2(people))
power_of_two = 2**power

# get the difference between the input number and the aformentioned power of 2
number = people-power_of_two

# work out the position in the ring of n people to be the last person standing
# (this works out to be 2x the difference between n and 2^x plus 1, where 2^x < n)
position = str((2*number)+1)

#here's the maths stuff all in 1 line just for the fun of it:
position_in_1 = str((2*(people-(2**(math.floor(math.log2(people))))))+1)

print(f"The optimal position is {position}")
