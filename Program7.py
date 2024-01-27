#Python Program  to find area of a circle?
import math

def calculate_circle_area(radius):
    # Area of a circle formula: A = π * r^2
    area = math.pi * radius**2
    return area

# Example usage:
radius = float(input("Enter the radius of the circle: "))

circle_area = calculate_circle_area(radius)

print(f"The area of the circle with radius {radius} is: {circle_area}")

