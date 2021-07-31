import random, math, sys

# being able to get a random value between 0 and 1
# calculate the value of pi

def calculate_pi(n):
    inside_circle = 0.
    inside_square = 0.
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        # pithagoras theorem, no need to square root
        # if value is <1 its square root is also <1
        # and the square root for values >1 are >1
        dist_to_origin = x**2 + y**2
        if dist_to_origin < 1:
            inside_circle = inside_circle + 1
        inside_square = inside_square + 1
    
    # 4 is the calculated ratio between the area of a
    # quarter-circle with r = 1 that exists inside a 1*1 square
    # eg. pi*r**2/4 / r**2 (area of circle divided by 4
    # because this represents 1/4 of a circle)
    # given that equation we can isolate pi which is equal to 4 
    return 4 * inside_circle/inside_square

if __name__ == "__main__":
    iterations = int(sys.argv[1])
    pi = calculate_pi(iterations)
    print(pi)
    print("e: " + str(abs(math.pi - pi)))