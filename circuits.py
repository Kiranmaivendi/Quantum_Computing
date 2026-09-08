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