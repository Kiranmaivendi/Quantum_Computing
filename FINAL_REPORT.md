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

The complete editable source is provided in `app.py`, `circuits.py`, `simulator.py`, `visualization.py`, and `../test.py`. The notebook contains executable examples for the full circuit catalog.
