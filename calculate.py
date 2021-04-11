import random, math, sys

# being able to get a random value between 0 and 1
# calculate the value of pi

def calculate_pi(n):
    inside_circle = 0.
    inside_square = 0.
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        dist_to_origin = x**2 + y**2
        if dist_to_origin < 1:
            inside_circle = inside_circle + 1
        inside_square = inside_square + 1
    
    # 4 is the calculated ratio between the area of a semi-circle with r = 1
    # that exists inside a 1*1 square 
    return 4 * inside_circle/inside_square

if __name__ == "__main__":
    iterations = int(sys.argv[1])
    pi = calculate_pi(iterations)
    print(pi)
    print("e: " + str(abs(math.pi - pi)))