"""Plotting helpers for circuit results."""

from qiskit.visualization import plot_bloch_multivector, plot_histogram


def histogram(counts):
    return plot_histogram(counts)


def bloch(state):
    return plot_bloch_multivector(state)