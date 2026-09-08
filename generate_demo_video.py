"""Generate the Product 1 demonstration video as an MP4."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter, FuncAnimation
from matplotlib.patches import FancyBboxPatch
from imageio_ffmpeg import get_ffmpeg_exe

from circuits import bell_state, ghz_state, hadamard
from simulator import measure, transpilation_summary


OUTPUT = Path(__file__).with_name("quantum_circuit_product_1_demo.mp4")
FPS = 24
SCENE_SECONDS = 3


def draw_circuit(axis, circuit):
    axis.axis("off")
    axis.text(
        0.02,
        0.5,
        circuit.draw(output="text"),
        family="monospace",
        fontsize=13,
        va="center",
        color="#17324d",
    )


def draw_counts(axis, counts):
    labels = list(counts)
    values = [counts[label] for label in labels]
    axis.bar(labels, values, color="#0e7490", width=0.6)
    axis.set_ylabel("shots")
    axis.set_title("Measurement outcomes")
    axis.grid(axis="y", alpha=0.2)


def make_video():
    bell_counts = measure(bell_state(), shots=1024)
    ghz_counts = measure(ghz_state(), shots=1024)
    hadamard_counts = measure(hadamard(), shots=1024)
    summary = transpilation_summary(bell_state())
    scenes = [
        ("title", None, None),
        ("Hadamard superposition", hadamard(), hadamard_counts),
        ("Bell-state entanglement", bell_state(), bell_counts),
        ("GHZ three-qubit entanglement", ghz_state(), ghz_counts),
        ("Reusable Qiskit architecture", None, None),
        ("Transpilation analysis", bell_state(), summary),
    ]

    plt.rcParams["animation.ffmpeg_path"] = get_ffmpeg_exe()
    figure = plt.figure(figsize=(12.8, 7.2), facecolor="#f5f7f9")
    frames_per_scene = FPS * SCENE_SECONDS

    def update(frame):
        scene_index = min(frame // frames_per_scene, len(scenes) - 1)
        scene, circuit, result = scenes[scene_index]
        figure.clear()
        figure.patch.set_facecolor("#f5f7f9")
        if scene == "title":
            figure.text(0.08, 0.64, "Quantum Circuit Designer", fontsize=34, weight="bold", color="#12304a")
            figure.text(0.08, 0.53, "and Simulator", fontsize=34, weight="bold", color="#0e7490")
            figure.text(0.08, 0.39, "Product 1 demonstration | Qiskit + Aer + Streamlit", fontsize=17, color="#425466")
            figure.text(0.08, 0.25, "Qubits  |  gates  |  entanglement  |  measurement  |  visualization", fontsize=14, color="#425466")
        elif scene == "Reusable Qiskit architecture":
            figure.text(0.08, 0.84, scene, fontsize=28, weight="bold", color="#12304a")
            modules = [
                (0.08, 0.52, "circuits.py", "14 reusable circuit builders"),
                (0.38, 0.52, "simulator.py", "statevectors, counts, transpilation"),
                (0.68, 0.52, "app.py", "interactive Streamlit designer"),
                (0.23, 0.22, "visualization.py", "histograms and Bloch plots"),
                (0.53, 0.22, "test_simulator.py", "six automated tests"),
            ]
            for x, y, label, detail in modules:
                axis = figure.add_axes([x, y, 0.22, 0.16])
                axis.axis("off")
                axis.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.03", facecolor="#d9eef2", edgecolor="#0e7490"))
                axis.text(0.5, 0.65, label, ha="center", weight="bold", color="#12304a")
                axis.text(0.5, 0.35, detail, ha="center", fontsize=8, color="#425466", wrap=True)
        elif scene == "Transpilation analysis":
            figure.text(0.08, 0.84, scene, fontsize=28, weight="bold", color="#12304a")
            axis = figure.add_axes([0.08, 0.18, 0.84, 0.52])
            axis.axis("off")
            axis.text(0.02, 0.78, "Bell-state circuit", fontsize=17, weight="bold", color="#0e7490")
            axis.text(0.02, 0.58, circuit.draw(output="text"), family="monospace", fontsize=13, color="#17324d")
            axis.text(0.52, 0.78, "Aer transpilation summary", fontsize=17, weight="bold", color="#0e7490")
            axis.text(0.52, 0.62, f"Original depth:   {result['original_depth']}", fontsize=14, color="#17324d")
            axis.text(0.52, 0.50, f"Transpiled depth: {result['transpiled_depth']}", fontsize=14, color="#17324d")
            axis.text(0.52, 0.38, f"Original size:    {result['original_size']}", fontsize=14, color="#17324d")
            axis.text(0.52, 0.26, f"Transpiled size:  {result['transpiled_size']}", fontsize=14, color="#17324d")
        else:
            figure.text(0.08, 0.86, scene, fontsize=28, weight="bold", color="#12304a")
            left = figure.add_axes([0.08, 0.18, 0.42, 0.54])
            right = figure.add_axes([0.60, 0.18, 0.32, 0.54])
            draw_circuit(left, circuit)
            draw_counts(right, result)
            figure.text(0.08, 0.08, "Ideal Qiskit Aer simulation with 1024 seeded shots", fontsize=13, color="#425466")

    animation = FuncAnimation(figure, update, frames=frames_per_scene * len(scenes), interval=1000 / FPS)
    writer = FFMpegWriter(fps=FPS, bitrate=1800, metadata={"title": "Quantum Circuit Product 1 Demo"})
    animation.save(OUTPUT, writer=writer, dpi=100)
    plt.close(figure)
    print(f"Created {OUTPUT} ({OUTPUT.stat().st_size / 1024 / 1024:.2f} MB)")


if __name__ == "__main__":
    make_video()