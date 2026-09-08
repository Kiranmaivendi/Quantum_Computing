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