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
