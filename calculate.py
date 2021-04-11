import random, math, sys

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
    return 4 * inside_circle/inside_square

if __name__ == "__main__":
    iterations = int(sys.argv[1])
    pi = calculate_pi(iterations)
    print(pi)
    print("e: " + str(abs(math.pi - pi)))