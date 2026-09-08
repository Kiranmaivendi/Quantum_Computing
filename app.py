import streamlit as st
from qiskit import QuantumCircuit

from circuits import catalog, rotation
from simulator import measure, statevector, transpilation_summary
from visualization import bloch, histogram

st.set_page_config(page_title="Quantum Circuit Designer", page_icon="⚛️", layout="wide")
st.title("Quantum Circuit Designer and Simulator")
st.caption("Product 1 | Ideal Qiskit simulation of fundamental quantum circuits")

catalogue = catalog()
example = st.selectbox("Circuit example", list(catalogue) + ["Rotation"])
shots = st.slider("Measurement shots", 128, 4096, 1024, step=128)

if example == "Rotation":
    axis = st.selectbox("Rotation axis", ["x", "y", "z"])
    theta = st.slider("Angle (radians)", 0.0, 6.2832, 1.5708)
    qc = rotation(axis, theta)
else:
    qc = catalogue[example]()

st.subheader("Circuit diagram")
st.code(qc.draw(output="text"), language="text")

ideal_state = statevector(qc)
counts = measure(qc, shots=shots)
summary = transpilation_summary(qc)

left, middle, right = st.columns(3)
with left:
    st.subheader("Statevector")
    st.write(ideal_state)
with middle:
    st.subheader("Measurement counts")
    st.write(counts)
    st.pyplot(histogram(counts), clear_figure=False)
with right:
    st.subheader("Transpilation")
    st.json(summary)

st.subheader("Bloch representation")
st.pyplot(bloch(ideal_state), clear_figure=False)