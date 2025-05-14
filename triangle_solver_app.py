import streamlit as st
import math
import matplotlib.pyplot as plt

# Degree-radian conversion
def radians(deg):
    return math.radians(deg)

def degrees(rad):
    return math.degrees(rad)

# Triangle plotting
def plot_triangle(a, b, c, A, B, C):
    A_x, A_y = 0, 0
    B_x, B_y = c, 0
    C_x = b * math.cos(A)
    C_y = b * math.sin(A)

    fig, ax = plt.subplots()
    ax.plot([A_x, B_x], [A_y, B_y], 'k-')
    ax.plot([B_x, C_x], [B_y, C_y], 'k-')
    ax.plot([C_x, A_x], [C_y, A_y], 'k-')
    ax.text(A_x, A_y, 'A', color='red')
    ax.text(B_x, B_y, 'B', color='red')
    ax.text(C_x, C_y, 'C', color='red')
    ax.set_aspect('equal')
    ax.grid(True)
    st.pyplot(fig)

# Display triangle result
def display_triangle(a, b, c, A, B, C):
    st.markdown("### Solved Triangle")
    st.write(f"Side a = {a:.2f}")
    st.write(f"Side b = {b:.2f}")
    st.write(f"Side c = {c:.2f}")
    st.write(f"Angle A = {degrees(A):.2f}°")
    st.write(f"Angle B = {degrees(B):.2f}°")
    st.write(f"Angle C = {degrees(C):.2f}°")
    plot_triangle(a, b, c, A, B, C)

# Solvers
def solve_sss(a, b, c):
    A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    C = math.pi - A - B
    display_triangle(a, b, c, A, B, C)

def solve_sas(b, c, A_deg):
    A = radians(A_deg)
    a = math.sqrt(b**2 + c**2 - 2 * b * c * math.cos(A))
    B = math.asin(b * math.sin(A) / a)
    C = math.pi - A - B
    display_triangle(a, b, c, A, B, C)

def solve_asa(A_deg, C_deg, b):
    A = radians(A_deg)
    C = radians(C_deg)
    B = math.pi - A - C
    a = b * math.sin(A) / math.sin(B)
    c = b * math.sin(C) / math.sin(B)
    display_triangle(a, b, c, A, B, C)

def solve_aas(A_deg, B_deg, a):
    A = radians(A_deg)
    B = radians(B_deg)
    C = math.pi - A - B
    b = a * math.sin(B) / math.sin(A)
    c = a * math.sin(C) / math.sin(A)
    display_triangle(a, b, c, A, B, C)

def solve_ssa(a, b, A_deg):
    A = radians(A_deg)
    sinB = b * math.sin(A) / a
    if sinB < -1 or sinB > 1:
        st.error("Invalid triangle. No solution.")
        return
    B = math.asin(sinB)
    C = math.pi - A - B
    c = a * math.sin(C) / math.sin(A)
    display_triangle(a, b, c, A, B, C)

# Streamlit UI
st.title("Triangle Solver")

method = st.selectbox(
    "Select the known elements",
    ("SSS (3 sides)", "SAS (2 sides + included angle)", "ASA (2 angles + included side)",
     "AAS (2 angles + non-included side)", "SSA (2 sides + non-included angle)")
)

if method == "SSS (3 sides)":
    a = st.number_input("Side a", min_value=0.0)
    b = st.number_input("Side b", min_value=0.0)
    c = st.number_input("Side c", min_value=0.0)
    if st.button("Solve"):
        if a + b > c and a + c > b and b + c > a:
            solve_sss(a, b, c)
        else:
            st.error("Invalid triangle: triangle inequality violated.")

elif method == "SAS (2 sides + included angle)":
    b = st.number_input("Side b", min_value=0.0)
    c = st.number_input("Side c", min_value=0.0)
    A = st.number_input("Included angle A (degrees)", min_value=0.0, max_value=180.0)
    if st.button("Solve"):
        solve_sas(b, c, A)

elif method == "ASA (2 angles + included side)":
    A = st.number_input("Angle A (degrees)", min_value=0.0, max_value=180.0)
    C = st.number_input("Angle C (degrees)", min_value=0.0, max_value=180.0)
    b = st.number_input("Side b", min_value=0.0)
    if st.button("Solve"):
        if A + C < 180:
            solve_asa(A, C, b)
        else:
            st.error("Invalid triangle: angles must add to less than 180°.")

elif method == "AAS (2 angles + non-included side)":
    A = st.number_input("Angle A (degrees)", min_value=0.0, max_value=180.0)
    B = st.number_input("Angle B (degrees)", min_value=0.0, max_value=180.0)
    a = st.number_input("Side a", min_value=0.0)
    if st.button("Solve"):
        if A + B < 180:
            solve_aas(A, B, a)
        else:
            st.error("Invalid triangle: angles must add to less than 180°.")

elif method == "SSA (2 sides + non-included angle)":
    a = st.number_input("Side a", min_value=0.0)
    b = st.number_input("Side b", min_value=0.0)
    A = st.number_input("Angle A (degrees)", min_value=0.0, max_value=180.0)
    if st.button("Solve"):
        solve_ssa(a, b, A)