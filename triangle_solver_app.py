import streamlit as st
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

st.set_page_config(page_title="SSS Triangle Solver", layout="centered")

st.title("Triangle Solver (SSS)")

# User Inputs
a = st.number_input("Enter side a:", min_value=0.01)
b = st.number_input("Enter side b:", min_value=0.01)
c = st.number_input("Enter side c:", min_value=0.01)

def solve_triangle(a, b, c):
    # Check triangle inequality
    if a + b <= c or a + c <= b or b + c <= a:
        st.error("Invalid triangle: Triangle inequality not satisfied.")
        return

    # Law of Cosines
    A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    C = math.pi - A - B

    # Display results
    st.subheader("Results")
    st.write(f"Angle A: {math.degrees(A):.2f}°")
    st.write(f"Angle B: {math.degrees(B):.2f}°")
    st.write(f"Angle C: {math.degrees(C):.2f}°")

    # Optional plot
    fig, ax = plt.subplots()
    A_x, A_y = 0, 0
    B_x, B_y = c, 0
    C_x = b * math.cos(A)
    C_y = b * math.sin(A)
    ax.plot([A_x, B_x, C_x, A_x], [A_y, B_y, C_y, A_y], 'k-')
    ax.text(A_x, A_y, 'A', color='red')
    ax.text(B_x, B_y, 'B', color='red')
    ax.text(C_x, C_y, 'C', color='red')
    ax.set_aspect('equal')
    ax.grid(True)
    st.pyplot(fig)

if st.button("Solve"):
    solve_triangle(a, b, c)