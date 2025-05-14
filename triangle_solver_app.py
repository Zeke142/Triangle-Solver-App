import streamlit as st
import math
import matplotlib
matplotlib.use("Agg")  # Ensure non-GUI backend
import matplotlib.pyplot as plt

st.set_page_config(page_title="Triangle Solver", layout="centered")

def radians(deg): return math.radians(deg)
def degrees(rad): return math.degrees(rad)

def display_triangle(a, b, c, A, B, C):
    st.subheader("Solved Triangle")
    st.write(f"Side a = {a:.2f}")
    st.write(f"Side b = {b:.2f}")
    st.write(f"Side c = {c:.2f}")
    st.write(f"Angle A = {degrees(A):.2f}°")
    st.write(f"Angle B = {degrees(B):.2f}°")
    st.write(f"Angle C = {degrees(C):.2f}°")

def plot_triangle(a, b, c, A, B, C):
    A_x, A_y = 0, 0
    B_x, B_y = c, 0
    C_x = b * math.cos(A)
    C_y = b * math.sin(A)

    fig, ax = plt.subplots()
    ax.plot([A_x, B_x, C_x, A_x], [A_y, B_y, C_y, A_y], 'k-')
    ax.text(A_x, A_y, 'A', fontsize=12, color='red')
    ax.text(B_x, B_y, 'B', fontsize=12, color='red')
    ax.text(C_x, C_y, 'C', fontsize=12, color='red')
    ax.set_aspect('equal')
    ax.grid(True)
    st.pyplot(fig)

def solve_sss(a, b, c):
    A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    C = math.pi - A - B
    display_triangle(a, b, c, A, B, C)
    plot_triangle(a, b, c, A, B, C)

def solve_sas(b, c, A_deg):
    A = radians(A_deg)
    a = math.sqrt(b**2 + c**2 - 2 * b * c * math.cos(A))
    B = math.asin(b * math.sin(A) / a)
    C = math.pi - A - B
    display_triangle(a, b, c, A, B, C)
    plot_triangle(a, b, c, A, B, C)

def solve_asa(A_deg, C_deg, b):
    A = radians(A_deg)
    C = radians(C_deg)
    B = math.pi - A - C
    a = b * math.sin(A) / math.sin(B)
    c = b * math.sin(C) / math.sin(B)
    display_triangle(a, b, c, A, B, C)
    plot_triangle(a, b, c, A, B, C)

def solve_aas(A_deg, B_deg, a):
    A = radians(A_deg)
    B = radians(B_deg)
    C = math.pi - A - B
    b = a * math.sin(B) / math.sin(A)
    c = a * math.sin(C) / math.sin(A)
    display_triangle(a, b, c, A, B, C)
    plot_triangle(a, b, c, A, B, C)

def solve_ssa(a, b, A_deg):
    A = radians(A_deg)
    sinB = b * math.sin(A) / a
    if not (-1 <= sinB <= 1):
        st.error("No solution: invalid triangle.")
        return
    B = math.asin(sinB)
    C = math.pi - A - B
    c = a * math.sin(C) / math.sin(A)
    display_triangle(a, b, c, A, B, C)
    plot_triangle(a, b, c, A, B, C)

# Streamlit App UI
st.title("Triangle Solver App")
option = st.selectbox("Select known elements:", [
    "SSS (3 sides)",
    "SAS (2 sides + included angle)",
    "ASA (2 angles + included side)",
    "AAS (2 angles + non-included side)",
    "SSA (2 sides + non-included angle)"
])

if option == "SSS (3 sides)":
    a = st.number_input("Enter side a:", min_value=0.01)
    b = st.number_input("Enter side b:", min_value=0.01)
    c = st.number_input("Enter side c:", min_value=0.01)
    if st.button("Solve Triangle"):
        if a + b > c and a + c > b and b + c > a:
            solve_sss(a, b, c)
        else:
            st.error("Invalid triangle: triangle inequality not satisfied.")

elif option == "SAS (2 sides + included angle)":
    b = st.number_input("Enter side b:", min_value=0.01)
    c = st.number_input("Enter side c:", min_value=0.01)
    A_deg = st.number_input("Enter angle A (degrees):", min_value=0.1, max_value=179.9)
    if st.button("Solve Triangle"):
        solve_sas(b, c, A_deg)

elif option == "ASA (2 angles + included side)":
    A_deg = st.number_input("Enter angle A (degrees):", min_value=0.1, max_value=179.9)
    C_deg = st.number_input("Enter angle C (degrees):", min_value=0.1, max_value=179.9)
    b = st.number_input("Enter side b:", min_value=0.01)
    if st.button("Solve Triangle"):
        if A_deg + C_deg < 180:
            solve_asa(A_deg, C_deg, b)
        else:
            st.error("Angles must sum to less than 180°.")

elif option == "AAS (2 angles + non-included side)":
    A_deg = st.number_input("Enter angle A (degrees):", min_value=0.1, max_value=179.9)
    B_deg = st.number_input("Enter angle B (degrees):", min_value=0.1, max_value=179.9)
    a = st.number_input("Enter side a:", min_value=0.01)
    if st.button("Solve Triangle"):
        if A_deg + B_deg < 180:
            solve_aas(A_deg, B_deg, a)
        else:
            st.error("Angles must sum to less than 180°.")

elif option == "SSA (2 sides + non-included angle)":
    a = st.number_input("Enter side a:", min_value=0.01)
    b = st.number_input("Enter side b:", min_value=0.01)
    A_deg = st.number_input("Enter angle A (degrees):", min_value=0.1, max_value=179.9)
    if st.button("Solve Triangle"):
        solve_ssa(a, b, A_deg)