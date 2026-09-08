# Quantum Circuit Designer and Simulator

Product 1 final submission package, prepared through 30/08/2026.

## Contents

- `app.py`: Streamlit circuit-designer interface.
- `circuits.py`: reusable constructors for 14 fundamental circuits.
- `simulator.py`: statevector, seeded measurement, and transpilation helpers.
- `visualization.py`: histogram and Bloch-sphere plotting helpers.
- `Quantum_Circuit_Product_1.ipynb`: editable Jupyter Notebook with theory, circuits, results, and comparisons.
- `FINAL_REPORT.md`: editable final report.
- `DEMO_SCRIPT.md`: presentation/video demonstration script.
- `PRESENTATION_OUTLINE.md`: presentation-ready slide outline.
- `Quantum_Circuit_Product_1_Presentation.pptx`: editable 12-slide project presentation.
- `generate_presentation.py`: reproducible PowerPoint generator.
- `quantum_circuit_product_1_demo.mp4`: generated demonstration video.
- `generate_demo_video.py`: reproducible video generator.
- `test_simulator.py`: automated tests.

## Installation

Python 3.9+ is recommended.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the interface

```powershell
streamlit run app.py
```

The interface displays circuit diagrams, ideal statevectors, seeded measurement counts, Bloch representations, and transpilation summaries.

## Run tests

From this project directory:

```powershell
python -m unittest -v test_simulator
```

## Run the notebook

Open `Quantum_Circuit_Product_1.ipynb` in VS Code or Jupyter after installing the requirements, then run all cells. The notebook uses the same modules as the interface so the documented results remain reproducible.

## Optional extensions

The simulator currently uses Qiskit Aer for ideal simulation. A noise model or IBM Quantum backend can be added later by replacing the backend in `simulator.py` and recording credentials outside source control.
