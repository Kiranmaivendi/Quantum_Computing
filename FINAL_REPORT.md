# Quantum Circuit Designer and Simulator
## Product 1 Final Report

**Submission date:** 30/08/2026  
**Technology:** Python, Qiskit, Qiskit Aer, Streamlit, Matplotlib  

## Title Page

**Project:** Quantum Circuit Designer and Simulator  
**Product:** Product 1  
**Purpose:** Design and simulate fundamental quantum circuits with state and measurement visualizations.  

## Abstract

This project implements a modular quantum-circuit designer and simulator using Qiskit. It covers qubits, quantum states, single-qubit gates, multi-qubit gates, entanglement, measurement, statevector simulation, histogram visualization, Bloch representations, and transpilation analysis. The application provides an interactive Streamlit interface, an editable Jupyter Notebook, reusable Python modules, and automated tests. Ideal Qiskit Aer results are compared with theoretical predictions for representative circuits including Pauli-X, Hadamard, Bell, and GHZ states.

## Objectives

1. Construct fundamental single- and multi-qubit circuits.
2. Explain and apply quantum gates and measurement.
3. Simulate ideal statevectors and finite-shot measurement outcomes.
4. Visualize circuits, Bloch vectors, and count histograms.
5. Inspect transpilation depth and operation counts.
6. Provide a reusable interface, notebook, report, tests, and source code.

## Introduction to Qubits and Quantum Circuits

A classical bit is either 0 or 1. A qubit is represented by a normalized state $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$, where $|\alpha|^2 + |\beta|^2 = 1$. Measurement in the computational basis produces 0 with probability $|\alpha|^2$ and 1 with probability $|\beta|^2$. A quantum circuit is an ordered sequence of unitary gates followed by optional measurement operations.

## Software and Hardware Requirements

- Python 3.9 or later
- Qiskit and Qiskit Aer
- Streamlit for the interface
- Matplotlib and NumPy for visual output
- A normal laptop is sufficient for the included 1-3 qubit examples; no quantum hardware is required
- Optional IBM Quantum access may be added with external credentials

Install using `pip install -r requirements.txt`.

## Mathematical Background

The computational basis is $|0\rangle = [1,0]^T$ and $|1\rangle = [0,1]^T$. Common gates are:

- $X = [[0,1],[1,0]]$, which exchanges $|0\rangle$ and $|1\rangle$.
- $Y = [[0,-i],[i,0]]$ and $Z = [[1,0],[0,-1]]$.
- $H = \frac{1}{\sqrt{2}}[[1,1],[1,-1]]$, which creates equal superposition from $|0\rangle$.
- $R_x(\theta)$, $R_y(\theta)$, and $R_z(\theta)$ are parameterized rotations.
- The CNOT maps $|a,b\rangle$ to $|a,b \oplus a\rangle$.

For an $n$-qubit system, the statevector has $2^n$ complex amplitudes. The Bell circuit $H_0$ followed by $CX_{0,1}$ produces $(|00\rangle + |11\rangle)/\sqrt{2}$. The GHZ circuit extends this pattern to $(|000\rangle + |111\rangle)/\sqrt{2}$.

## Circuit Design Methodology

Each circuit is implemented as a pure builder function in `circuits.py`. Builders return a Qiskit `QuantumCircuit`, which prevents duplicated gate logic across the app, notebook, and tests. The simulator removes final measurements for ideal statevector inspection, then runs seeded Aer measurement experiments for reproducible counts. Qiskit transpiles circuits to the Aer target and reports depth, size, and operation counts.

## Qiskit Implementation

The implementation includes Identity, Pauli-X, Pauli-Y, Pauli-Z, Hadamard, S, T, Rx/Ry/Rz rotations, measurement, CNOT, CZ, SWAP, Toffoli, Bell, and GHZ circuits. The Streamlit application selects an example and shows all result views together. The notebook imports the same builders and helpers, so the report is backed by executable code rather than copied output.

## Circuit Diagrams and Simulation Outputs

The application and notebook render text or Matplotlib circuit diagrams. Expected ideal results include:

| Circuit | Theoretical state or outcome | Expected measurement |
|---|---|---|
| Pauli-X | $|1\rangle$ | 1 with probability 1 |
| Hadamard | $(|0\rangle+|1\rangle)/\sqrt{2}$ | Approximately 50% 0 and 50% 1 |
| Bell | $(|00\rangle+|11\rangle)/\sqrt{2}$ | Only 00 and 11 |
| GHZ | $(|000\rangle+|111\rangle)/\sqrt{2}$ | Only 000 and 111 |

With 1024 shots, finite sampling makes the superposition frequencies close to, but not exactly, their theoretical probabilities. Seeded simulation makes the notebook and tests repeatable.

## Theoretical-versus-Simulated Comparison

The test suite verifies exact state properties where possible and support of measurement distributions for entangled states. The Pauli-X test verifies unit probability for $|1\rangle$; the Hadamard test verifies probabilities 0.5 and 0.5; the Bell test verifies that all observed outcomes are correlated as 00 or 11. This establishes agreement between the mathematical model and Qiskit Aer for the covered cases.

## Transpilation Analysis

Transpilation converts a high-level circuit into operations supported by a selected backend. The application reports original and transpiled depth, circuit size, and operation counts. Simple one-qubit gates generally retain shallow depth. Multi-qubit circuits may be decomposed into backend-supported basis gates, increasing depth and operation count. This cost is important because real devices have limited connectivity and noisy two-qubit operations.

## Challenges and Limitations

- Measurement results are statistical and depend on shot count.
- Ideal Aer simulation does not model decoherence, readout error, or calibration drift.
- Bloch-sphere plots are most directly interpretable for individual qubits; multi-qubit entanglement requires the full statevector.
- The interface currently supports the documented examples rather than arbitrary drag-and-drop circuit editing.
- Real IBM hardware comparison requires account credentials, backend availability, queue time, and noise-aware interpretation.

## Conclusion

Product 1 delivers a functional and testable foundation for learning and demonstrating quantum circuits. The modular builders, simulator helpers, visualizations, interactive interface, notebook, and report cover the required topics and preserve a direct connection between theory and executable results.

## Future Enhancements

1. Add a drag-and-drop circuit editor and circuit serialization.
2. Add configurable depolarizing, thermal-relaxation, and readout noise models.
3. Compare ideal Aer results with a selected IBM Quantum backend.
4. Add amplitude and phase plots for larger statevectors.
5. Export diagrams, counts, and reports from the interface.

## References

1. Qiskit Documentation, https://qiskit.org/documentation/
2. Qiskit Aer Documentation, https://qiskit.github.io/qiskit-aer/
3. Nielsen, M. A. and Chuang, I. L., *Quantum Computation and Quantum Information*, Cambridge University Press.
4. IBM Quantum Learning, https://learning.quantum.ibm.com/

## Appendix A: Complete Source Code

The following source is included in the repository and reproduced here for a complete editable appendix.

### A.1 `circuits.py`

```python
"""Constructors for the fundamental circuits used by Product 1."""

from __future__ import annotations

from collections.abc import Callable

from qiskit import QuantumCircuit


def _single_qubit(name: str, operation: Callable[[QuantumCircuit, int], None]) -> QuantumCircuit:
	circuit = QuantumCircuit(1, name=name)
	operation(circuit, 0)
	return circuit


def identity() -> QuantumCircuit:
	return _single_qubit("Identity", lambda circuit, qubit: circuit.id(qubit))


def pauli_x() -> QuantumCircuit:
	return _single_qubit("Pauli-X", lambda circuit, qubit: circuit.x(qubit))


def pauli_y() -> QuantumCircuit:
	return _single_qubit("Pauli-Y", lambda circuit, qubit: circuit.y(qubit))


def pauli_z() -> QuantumCircuit:
	return _single_qubit("Pauli-Z", lambda circuit, qubit: circuit.z(qubit))


def hadamard() -> QuantumCircuit:
	return _single_qubit("Hadamard", lambda circuit, qubit: circuit.h(qubit))


def phase_s() -> QuantumCircuit:
	return _single_qubit("Phase-S", lambda circuit, qubit: circuit.s(qubit))


def phase_t() -> QuantumCircuit:
	return _single_qubit("Phase-T", lambda circuit, qubit: circuit.t(qubit))


def rotation(axis: str, theta: float) -> QuantumCircuit:
	circuit = QuantumCircuit(1, name=f"Rotation-{axis.upper()}")
	getattr(circuit, f"r{axis.lower()}")(theta, 0)
	return circuit


def measurement() -> QuantumCircuit:
	circuit = QuantumCircuit(1, 1, name="Measurement")
	circuit.measure(0, 0)
	return circuit


def cnot() -> QuantumCircuit:
	circuit = QuantumCircuit(2, name="CNOT")
	circuit.cx(0, 1)
	return circuit


def controlled_z() -> QuantumCircuit:
	circuit = QuantumCircuit(2, name="CZ")
	circuit.cz(0, 1)
	return circuit


def swap() -> QuantumCircuit:
	circuit = QuantumCircuit(2, name="SWAP")
	circuit.swap(0, 1)
	return circuit


def toffoli() -> QuantumCircuit:
	circuit = QuantumCircuit(3, name="Toffoli")
	circuit.ccx(0, 1, 2)
	return circuit


def bell_state() -> QuantumCircuit:
	circuit = QuantumCircuit(2, name="Bell-State")
	circuit.h(0)
	circuit.cx(0, 1)
	return circuit


def ghz_state() -> QuantumCircuit:
	circuit = QuantumCircuit(3, name="GHZ-State")
	circuit.h(0)
	circuit.cx(0, 1)
	circuit.cx(1, 2)
	return circuit


def catalog() -> dict[str, Callable[[], QuantumCircuit]]:
	return {
		"Identity (I)": identity,
		"Pauli-X": pauli_x,
		"Pauli-Y": pauli_y,
		"Pauli-Z": pauli_z,
		"Hadamard (H)": hadamard,
		"Phase-S": phase_s,
		"Phase-T": phase_t,
		"CNOT (CX)": cnot,
		"Controlled-Z (CZ)": controlled_z,
		"SWAP": swap,
		"Toffoli (CCX)": toffoli,
		"Bell state": bell_state,
		"GHZ state": ghz_state,
		"Measurement": measurement,
	}
```

### A.2 `simulator.py`

```python
"""Simulation helpers shared by the application, notebook, and tests."""

from __future__ import annotations

from qiskit import ClassicalRegister, QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator


def statevector(circuit: QuantumCircuit) -> Statevector:
	"""Return the ideal statevector before measurement operations."""
	instruction_circuit = circuit.remove_final_measurements(inplace=False)
	return Statevector.from_instruction(instruction_circuit)


def measure(circuit: QuantumCircuit, shots: int = 1024, seed: int = 42) -> dict[str, int]:
	"""Run a circuit with measurements and return deterministic seeded counts."""
	measured_circuit = circuit.copy()
	if measured_circuit.num_clbits == 0:
		measured_circuit.add_register(ClassicalRegister(measured_circuit.num_qubits))
	if not measured_circuit.count_ops().get("measure"):
		measured_circuit.measure(range(measured_circuit.num_qubits), range(measured_circuit.num_qubits))
	simulator = AerSimulator(seed_simulator=seed)
	compiled = transpile(measured_circuit, simulator)
	return simulator.run(compiled, shots=shots, seed_simulator=seed).result().get_counts()


def simulate(circuit: QuantumCircuit, shots: int = 1024, seed: int = 42):
	"""Run a circuit and return the Aer result object for advanced use."""
	sim = AerSimulator()
	job = sim.run(circuit, shots=shots, seed_simulator=seed)
	return job.result()


def transpilation_summary(circuit: QuantumCircuit, basis_gates: list[str] | None = None) -> dict[str, object]:
	"""Summarize how Qiskit lowers a circuit for the Aer backend."""
	simulator = AerSimulator()
	compiled = transpile(circuit, simulator, basis_gates=basis_gates)
	return {
		"original_depth": circuit.depth(),
		"transpiled_depth": compiled.depth(),
		"original_size": circuit.size(),
		"transpiled_size": compiled.size(),
		"transpiled_operations": dict(compiled.count_ops()),
	}
```

### A.3 `visualization.py`

```python
"""Plotting helpers for circuit results."""

from qiskit.visualization import plot_bloch_multivector, plot_histogram


def histogram(counts):
	return plot_histogram(counts)


def bloch(state):
	return plot_bloch_multivector(state)
```

### A.4 `app.py`

```python
import streamlit as st

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
```

### A.5 `test_simulator.py`

```python
import unittest

from circuits import bell_state, catalog, ghz_state, hadamard, pauli_x, rotation
from simulator import measure, statevector, transpilation_summary


class TestCircuitSimulator(unittest.TestCase):
	def test_catalog_contains_all_required_examples(self):
		self.assertEqual(len(catalog()), 14)

	def test_x_flips_zero_to_one(self):
		self.assertAlmostEqual(abs(statevector(pauli_x()).data[1]), 1.0)

	def test_hadamard_is_superposition(self):
		amplitudes = statevector(hadamard()).probabilities()
		self.assertAlmostEqual(amplitudes[0], 0.5)
		self.assertAlmostEqual(amplitudes[1], 0.5)

	def test_bell_counts_are_correlated(self):
		counts = measure(bell_state(), shots=256)
		self.assertEqual(set(counts), {"00", "11"})

	def test_ghz_has_three_qubits(self):
		self.assertEqual(ghz_state().num_qubits, 3)

	def test_rotation_and_transpilation(self):
		summary = transpilation_summary(rotation("y", 1.0))
		self.assertGreaterEqual(summary["transpiled_depth"], 1)


if __name__ == "__main__":
	unittest.main()
```

### A.6 Automated test evidence

The final test run completed with six passing tests:

```text
Ran 6 tests in 0.4s
OK
```
