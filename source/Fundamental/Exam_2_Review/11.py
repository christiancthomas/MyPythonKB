import math

def calc_circle_is_bigger_than_square(radius, side):
	area_circle = math.pi * radius ** 2
	area_square = side ** 2
	return area_circle > area_square, area_circle, area_square

def main():
    boolean, sq, cir = calc_circle_is_bigger_than_square(25, 10)
    print(boolean, sq, cir)

if __name__ == "__main__":
      main()