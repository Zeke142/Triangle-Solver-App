import math
import matplotlib.pyplot as plt

def menu():
    print("\nTriangle Solver App")
    print("Select the known elements:")
    print("1. SSS (3 sides)")
    print("2. SAS (2 sides and included angle)")
    print("3. ASA (2 angles and included side)")
    print("4. AAS (2 angles and non-included side)")
    print("5. SSA (2 sides and angle NOT between them)")
    print("0. Exit")
    return input("Enter your choice: ")

def radians(deg):
    return math.radians(deg)

def degrees(rad):
    return math.degrees(rad)

def plot_triangle(a, b, c, A, B, C):
    # Using coordinates based on known side lengths and angles
    A_x, A_y = 0, 0
    B_x, B_y = c, 0
    C_x = b * math.cos(A)
    C_y = b * math.sin(A)

    plt.figure()
    plt.plot([A_x, B_x], [A_y, B_y], 'k-')
    plt.plot([B_x, C_x], [B_y, C_y], 'k-')
    plt.plot([C_x, A_x], [C_y, A_y], 'k-')
    
    plt.text(A_x, A_y, 'A', fontsize=12, color='red')
    plt.text(B_x, B_y, 'B', fontsize=12, color='red')
    plt.text(C_x, C_y, 'C', fontsize=12, color='red')

    plt.title("Triangle Visualization")
    plt.axis('equal')
    plt.grid(True)
    plt.show()

def solve_sss():
    print("\n--- SSS: Solve triangle with 3 known sides ---")
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid triangle: triangle inequality not satisfied.")
        return

    A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    C = math.pi - A - B

    display_triangle(a, b, c, A, B, C)
    plot_triangle(a, b, c, A, B, C)

def solve_sas():
    print("\n--- SAS: Solve triangle with 2 sides and included angle ---")
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    A = radians(float(input("Enter included angle A (in degrees): ")))

    a = math.sqrt(b**2 + c**2 - 2 * b * c * math.cos(A))
    B = math.asin(b * math.sin(A) / a)
    C = math.pi - A - B

    display_triangle(a, b, c, A, B, C)
    plot_triangle(a, b, c, A, B, C)

def solve_asa():
    print("\n--- ASA: Solve triangle with 2 angles and included side ---")
    A = radians(float(input("Enter angle A (degrees): ")))
    C = radians(float(input("Enter angle C (degrees): ")))
    b = float(input("Enter side b (between angles): "))
    
    B = math.pi - A - C
    a = b * math.sin(A) / math.sin(B)
    c = b * math.sin(C) / math.sin(B)

    display_triangle(a, b, c, A, B, C)
    plot_triangle(a, b, c, A, B, C)

def solve_aas():
    print("\n--- AAS: Solve triangle with 2 angles and one non-included side ---")
    A = radians(float(input("Enter angle A (degrees): ")))
    B = radians(float(input("Enter angle B (degrees): ")))
    a = float(input("Enter side a (opposite angle A): "))

    C = math.pi - A - B
    b = a * math.sin(B) / math.sin(A)
    c = a * math.sin(C) / math.sin(A)

    display_triangle(a, b, c, A, B, C)
    plot_triangle(a, b, c, A, B, C)

def solve_ssa():
    print("\n--- SSA: Solve triangle with 2 sides and angle NOT between them ---")
    a = float(input("Enter side a (opposite known angle A): "))
    b = float(input("Enter side b: "))
    A_deg = float(input("Enter angle A (degrees): "))
    A = radians(A_deg)

    sinB = b * math.sin(A) / a
    if sinB < -1 or sinB > 1:
        print("No solution: invalid triangle.")
        return

    B = math.asin(sinB)
    C = math.pi - A - B
    c = a * math.sin(C) / math.sin(A)

    display_triangle(a, b, c, A, B, C)
    plot_triangle(a, b, c, A, B, C)

def display_triangle(a, b, c, A, B, C):
    print("\nSolved Triangle:")
    print(f"Side a = {a:.2f}")
    print(f"Side b = {b:.2f}")
    print(f"Side c = {c:.2f}")
    print(f"Angle A = {degrees(A):.2f}°")
    print(f"Angle B = {degrees(B):.2f}°")
    print(f"Angle C = {degrees(C):.2f}°")

def main():
    while True:
        choice = menu()
        if choice == '1':
            solve_sss()
        elif choice == '2':
            solve_sas()
        elif choice == '3':
            solve_asa()
        elif choice == '4':
            solve_aas()
        elif choice == '5':
            solve_ssa()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()