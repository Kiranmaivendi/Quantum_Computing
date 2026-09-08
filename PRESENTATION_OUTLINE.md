# Product 1 Presentation Outline

## Slide 1: Title

Quantum Circuit Designer and Simulator  
Product 1 final submission  
Qiskit, Qiskit Aer, Python, and Streamlit

## Slide 2: Problem and Objectives

- Design fundamental single- and multi-qubit circuits.
- Simulate statevectors and finite-shot measurements.
- Visualize circuits, histograms, and Bloch representations.
- Compare theory with simulation and inspect transpilation.

## Slide 3: Quantum Foundations

- Qubit state: |psi> = alpha|0> + beta|1>.
- Measurement probabilities are squared amplitudes.
- Gates are unitary transformations.
- Controlled gates create correlations and entanglement.

## Slide 4: Circuit Catalog

Identity, X, Y, Z, H, S, T, Rx, Ry, Rz, measurement, CNOT, CZ, SWAP, Toffoli, Bell, and GHZ examples are implemented through reusable builders.

## Slide 5: System Architecture

- `circuits.py`: circuit constructors.
- `simulator.py`: statevector, measurement, and transpilation.
- `visualization.py`: histogram and Bloch plots.
- `app.py`: Streamlit interface.
- `test_simulator.py`: automated verification.

## Slide 6: Demonstration

1. Open the Streamlit app.
2. Select Hadamard and show approximately balanced counts.
3. Select Bell state and show only 00 and 11.
4. Select GHZ state and show only 000 and 111.
5. Show the transpilation summary.

## Slide 7: Results

The ideal Qiskit Aer simulation agrees with the theoretical Pauli-X, Hadamard, Bell, and GHZ predictions. The notebook contains saved circuit diagrams, statevectors, count outputs, histograms, Bloch plots, and transpilation results.

## Slide 8: Limitations and Future Work

The current version is an ideal simulator. Future work includes noise models, real IBM Quantum hardware comparison, drag-and-drop editing, export tools, and larger-circuit analysis.

## Slide 9: Submission Package

Editable notebook, modular source, Streamlit interface, final report, test suite, README, requirements file, and this presentation/video script.
