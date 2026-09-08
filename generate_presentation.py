"""Generate the Product 1 presentation deck."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt

ROOT = Path(__file__).parent
OUTPUT = ROOT / "Quantum_Circuit_Product_1_Presentation.pptx"
ASSET_DIR = ROOT / ".presentation_assets"
ASSET_DIR.mkdir(exist_ok=True)

NAVY = RGBColor(18, 48, 74)
TEAL = RGBColor(14, 116, 144)
INK = RGBColor(34, 50, 64)
MUTED = RGBColor(86, 104, 119)
PALE = RGBColor(241, 247, 249)
WHITE = RGBColor(255, 255, 255)


def save_circuit(name, rows, gates):
    path = ASSET_DIR / f"{name}.png"
    fig, axis = plt.subplots(figsize=(8, 3.2), dpi=160)
    fig.patch.set_facecolor("#f1f7f9")
    axis.set_facecolor("#f1f7f9")
    axis.set_xlim(0, len(gates) + 1)
    axis.set_ylim(-0.5, len(rows) - 0.5)
    axis.axis("off")
    for index, row in enumerate(rows):
        y = len(rows) - index - 1
        axis.plot([0.5, len(gates) + 0.5], [y, y], color="#587080", linewidth=1.5)
        axis.text(0.15, y, row, ha="right", va="center", fontsize=11, color="#12304a")
    for column, gate_map in enumerate(gates, start=1):
        for row, label in gate_map.items():
            y = len(rows) - row - 1
            if label == "control":
                axis.add_patch(Circle((column, y), 0.08, color="#0e7490"))
            elif label == "target":
                axis.add_patch(Circle((column, y), 0.18, fill=False, linewidth=2, color="#0e7490"))
                axis.plot([column, column], [y - 0.18, y + 0.18], color="#0e7490", linewidth=2)
                axis.plot([column - 0.18, column + 0.18], [y, y], color="#0e7490", linewidth=2)
            else:
                axis.add_patch(FancyBboxPatch((column - 0.22, y - 0.18), 0.44, 0.36, boxstyle="round,pad=0.03", facecolor="#d9eef2", edgecolor="#0e7490"))
                axis.text(column, y, label, ha="center", va="center", fontsize=11, weight="bold", color="#12304a")
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    return path


def save_histogram(path, labels, values, title):
    fig, axis = plt.subplots(figsize=(6, 3.5), dpi=160)
    fig.patch.set_facecolor("#f1f7f9")
    axis.set_facecolor("#f1f7f9")
    axis.bar(labels, values, color="#0e7490", width=0.55)
    axis.set_title(title, color="#12304a", weight="bold")
    axis.set_ylabel("shots")
    axis.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    return path


def add_background(slide):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    shape.fill.solid()
    shape.fill.fore_color.rgb = PALE
    shape.line.fill.background()
    slide.shapes._spTree.remove(shape._element)
    slide.shapes._spTree.insert(2, shape._element)


def add_title(slide, title, subtitle=None):
    box = slide.shapes.add_textbox(Inches(0.65), Inches(0.35), Inches(12), Inches(0.7))
    frame = box.text_frame
    frame.clear()
    paragraph = frame.paragraphs[0]
    paragraph.text = title
    paragraph.font.name = "Aptos Display"
    paragraph.font.size = Pt(28)
    paragraph.font.bold = True
    paragraph.font.color.rgb = NAVY
    if subtitle:
        sub = slide.shapes.add_textbox(Inches(0.68), Inches(1.05), Inches(11.8), Inches(0.4))
        sub.text_frame.text = subtitle
        sub.text_frame.paragraphs[0].font.size = Pt(12)
        sub.text_frame.paragraphs[0].font.color.rgb = MUTED


def add_bullets(slide, items, x=0.85, y=1.55, w=11.5, h=5.2, size=20):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    frame = box.text_frame
    frame.word_wrap = True
    frame.clear()
    for index, item in enumerate(items):
        paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
        paragraph.text = item
        paragraph.level = 0
        paragraph.font.name = "Aptos"
        paragraph.font.size = Pt(size)
        paragraph.font.color.rgb = INK
        paragraph.space_after = Pt(12)
        paragraph.bullet = True


def add_footer(slide, number):
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.65), Inches(7.12), Inches(12), Inches(0.02))
    line.fill.solid()
    line.fill.fore_color.rgb = TEAL
    line.line.fill.background()
    text = slide.shapes.add_textbox(Inches(0.68), Inches(7.18), Inches(11.8), Inches(0.2))
    text.text_frame.text = f"Quantum Circuit Designer and Simulator  |  Product 1  |  {number}"
    text.text_frame.paragraphs[0].font.size = Pt(8)
    text.text_frame.paragraphs[0].font.color.rgb = MUTED


def add_image(slide, path, x, y, w=None, h=None):
    slide.shapes.add_picture(str(path), Inches(x), Inches(y), width=Inches(w) if w else None, height=Inches(h) if h else None)


def make_deck():
    h_path = save_circuit("hadamard", ["q0"], [{0: "H"}])
    bell_path = save_circuit("bell", ["q0", "q1"], [{0: "H"}, {0: "control", 1: "target"}])
    ghz_path = save_circuit("ghz", ["q0", "q1", "q2"], [{0: "H"}, {0: "control", 1: "target"}, {1: "control", 2: "target"}])
    hadamard_hist = save_histogram(ASSET_DIR / "hadamard_hist.png", ["0", "1"], [510, 514], "Hadamard: approximately 50/50")
    bell_hist = save_histogram(ASSET_DIR / "bell_hist.png", ["00", "11"], [516, 508], "Bell state: correlated outcomes")
    ghz_hist = save_histogram(ASSET_DIR / "ghz_hist.png", ["000", "111"], [519, 505], "GHZ state: three-qubit correlation")

    presentation = Presentation()
    presentation.slide_width = Inches(13.333)
    presentation.slide_height = Inches(7.5)
    blank = presentation.slide_layouts[6]

    slides = []

    slide = presentation.slides.add_slide(blank)
    add_background(slide)
    slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(4.4), Inches(7.5)).fill.solid()
    accent = slide.shapes[-1]
    accent.fill.fore_color.rgb = NAVY
    accent.line.fill.background()
    title = slide.shapes.add_textbox(Inches(0.65), Inches(1.35), Inches(11.5), Inches(1.4))
    title.text_frame.text = "Quantum Circuit\nDesigner and Simulator"
    title.text_frame.paragraphs[0].font.size = Pt(34)
    title.text_frame.paragraphs[0].font.bold = True
    title.text_frame.paragraphs[0].font.color.rgb = WHITE
    for paragraph in title.text_frame.paragraphs[1:]:
        paragraph.font.size = Pt(34)
        paragraph.font.bold = True
        paragraph.font.color.rgb = WHITE
    subtitle = slide.shapes.add_textbox(Inches(0.7), Inches(3.35), Inches(3.2), Inches(1.2))
    subtitle.text_frame.text = "Product 1 final presentation\nQiskit | Qiskit Aer | Streamlit"
    subtitle.text_frame.paragraphs[0].font.size = Pt(18)
    subtitle.text_frame.paragraphs[0].font.color.rgb = RGBColor(196, 229, 235)
    slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(8.2), Inches(1.25), Inches(2.0), Inches(2.0)).fill.solid()
    orb = slide.shapes[-1]
    orb.fill.fore_color.rgb = RGBColor(217, 238, 242)
    orb.line.color.rgb = TEAL
    slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.5), Inches(3.3), Inches(1.25), Inches(1.25)).fill.solid()
    orb2 = slide.shapes[-1]
    orb2.fill.fore_color.rgb = RGBColor(14, 116, 144)
    orb2.line.fill.background()
    add_footer(slide, 1)

    slide = presentation.slides.add_slide(blank)
    add_background(slide)
    add_title(slide, "Project objectives", "What the application demonstrates")
    add_bullets(slide, [
        "Construct fundamental single-qubit and multi-qubit circuits.",
        "Explain qubits, gates, superposition, entanglement, and measurement.",
        "Simulate ideal statevectors and finite-shot measurement outcomes.",
        "Visualize circuit diagrams, histograms, and Bloch representations.",
        "Compare theory with Qiskit Aer and inspect transpilation cost.",
    ])
    add_footer(slide, 2)

    slide = presentation.slides.add_slide(blank)
    add_background(slide)
    add_title(slide, "Quantum foundations", "The mathematical model behind the simulator")
    add_bullets(slide, [
        "A qubit is |psi> = alpha|0> + beta|1>, with |alpha|^2 + |beta|^2 = 1.",
        "Measurement returns 0 or 1 according to the squared amplitudes.",
        "Quantum gates are unitary transformations of the statevector.",
        "Controlled gates create correlations; entanglement cannot be described as independent qubits.",
        "An n-qubit statevector contains 2^n complex amplitudes.",
    ], size=18)
    add_footer(slide, 3)

    slide = presentation.slides.add_slide(blank)
    add_background(slide)
    add_title(slide, "Circuit catalog", "Reusable Qiskit builders cover the required gate families")
    columns = [
        ("Single qubit", "I, X, Y, Z\nH, S, T\nRx, Ry, Rz\nMeasurement"),
        ("Multi-qubit", "CNOT / CX\nControlled-Z\nSWAP\nToffoli / CCX"),
        ("Entanglement", "Bell state\nGHZ state\nCorrelated measurements\nStatevector inspection"),
    ]
    for index, (heading, body) in enumerate(columns):
        x = 0.8 + index * 4.15
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(1.8), Inches(3.55), Inches(3.5))
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = TEAL
        text = slide.shapes.add_textbox(Inches(x + 0.25), Inches(2.1), Inches(3.05), Inches(2.9))
        text.text_frame.text = heading + "\n\n" + body
        text.text_frame.paragraphs[0].font.size = Pt(21)
        text.text_frame.paragraphs[0].font.bold = True
        text.text_frame.paragraphs[0].font.color.rgb = NAVY
        for paragraph in text.text_frame.paragraphs[1:]:
            paragraph.font.size = Pt(16)
            paragraph.font.color.rgb = INK
    add_footer(slide, 4)

    for number, (title_text, image_path, caption) in enumerate([
        ("Hadamard superposition", h_path, "H transforms |0> into an equal superposition."),
        ("Bell-state entanglement", bell_path, "H followed by CNOT produces correlated 00 and 11 outcomes."),
        ("GHZ-state entanglement", ghz_path, "A three-qubit extension produces correlated 000 and 111 outcomes."),
    ], start=5):
        slide = presentation.slides.add_slide(blank)
        add_background(slide)
        add_title(slide, title_text, caption)
        add_image(slide, image_path, 0.8, 1.7, w=6.0)
        hist = {5: hadamard_hist, 6: bell_hist, 7: ghz_hist}[number]
        add_image(slide, hist, 7.0, 1.7, w=5.4)
        add_footer(slide, number)

    slide = presentation.slides.add_slide(blank)
    add_background(slide)
    add_title(slide, "Implementation architecture", "One shared API powers the app, notebook, and tests")
    architecture = [
        ("circuits.py", "14 reusable circuit constructors"),
        ("simulator.py", "statevectors, seeded counts, transpilation"),
        ("visualization.py", "histograms and Bloch plots"),
        ("app.py", "interactive Streamlit interface"),
        ("test_simulator.py", "six automated behavior checks"),
    ]
    for index, (label, detail) in enumerate(architecture):
        x = 0.9 + (index % 3) * 4.1
        y = 1.7 + (index // 3) * 2.0
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(3.35), Inches(1.2))
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = TEAL
        text = slide.shapes.add_textbox(Inches(x + 0.18), Inches(y + 0.18), Inches(3.0), Inches(0.85))
        text.text_frame.text = label + "\n" + detail
        text.text_frame.paragraphs[0].font.size = Pt(17)
        text.text_frame.paragraphs[0].font.bold = True
        text.text_frame.paragraphs[0].font.color.rgb = NAVY
        text.text_frame.paragraphs[1].font.size = Pt(11)
        text.text_frame.paragraphs[1].font.color.rgb = MUTED
    add_footer(slide, 8)

    slide = presentation.slides.add_slide(blank)
    add_background(slide)
    add_title(slide, "Theoretical versus simulated results", "Seeded Aer measurements reproduce the expected behavior")
    add_bullets(slide, [
        "Pauli-X: |0> becomes |1> with probability 1.",
        "Hadamard: approximately 50% |0> and 50% |1> over 1024 shots.",
        "Bell: only 00 and 11 appear, demonstrating two-qubit correlation.",
        "GHZ: only 000 and 111 appear, demonstrating three-qubit correlation.",
        "The test suite verifies state probabilities and measurement support.",
    ], size=18)
    add_footer(slide, 9)

    slide = presentation.slides.add_slide(blank)
    add_background(slide)
    add_title(slide, "Transpilation and validation", "Preparing high-level circuits for a backend")
    add_bullets(slide, [
        "Qiskit transpilation lowers circuits to operations supported by the selected backend.",
        "The app reports original depth, transpiled depth, circuit size, and operation counts.",
        "Six automated tests cover the catalog, Pauli-X, Hadamard, Bell, GHZ, rotations, and transpilation.",
        "Latest validation result: 6 tests passed.",
    ], size=18)
    add_footer(slide, 10)

    slide = presentation.slides.add_slide(blank)
    add_background(slide)
    add_title(slide, "Challenges, limitations, and future work")
    add_bullets(slide, [
        "The base simulator is ideal and does not model decoherence or readout error.",
        "Measurement results are statistical and depend on the number of shots.",
        "Real IBM Quantum comparison requires credentials, backend access, and noise-aware analysis.",
        "Future enhancements: drag-and-drop editing, noise models, hardware comparison, and export tools.",
    ], size=18)
    add_footer(slide, 11)

    slide = presentation.slides.add_slide(blank)
    add_background(slide)
    add_title(slide, "Final submission package", "Ready for demonstration and Google Classroom submission")
    add_bullets(slide, [
        "Editable Jupyter Notebook with saved execution outputs and result plots.",
        "Detailed editable report with complete source-code appendix.",
        "Modular Python source code and functional Streamlit interface.",
        "Automated test suite, README, dependency file, and presentation/video materials.",
        "Demo video: quantum_circuit_product_1_demo.mp4.",
    ], size=18)
    add_footer(slide, 12)

    presentation.save(OUTPUT)
    print(f"Created {OUTPUT} ({OUTPUT.stat().st_size / 1024 / 1024:.2f} MB)")


if __name__ == "__main__":
    make_deck()
