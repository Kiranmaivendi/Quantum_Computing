# Demonstration Script

1. Start with `streamlit run app.py` and introduce the Product 1 objective.
2. Select **Hadamard (H)**. Show the circuit, statevector, approximately equal counts, Bloch representation, and transpilation summary.
3. Select **Bell state**. Explain that H creates superposition and CNOT creates entanglement. Point out that only 00 and 11 appear.
4. Select **GHZ state**. Explain the three-qubit extension and correlated 000/111 outcomes.
5. Select **Toffoli (CCX)** and show the multi-qubit circuit diagram.
6. Open `Quantum_Circuit_Product_1.ipynb` and run the theory, catalog, comparison, and transpilation cells.
7. Run `python -m unittest -v test` to show the automated test evidence.
8. Close with limitations: ideal simulation, finite shots, and no real-device noise in the base submission.
