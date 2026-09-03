# Neurological Programming

### Extra‑Sensory Vision Implant · Holographic Tomography · TRN Stimulation

## Overview

This repository contains the **theoretical foundation, mathematical models, and simulation software** for a next‑generation brain‑computer interface (BCI) – a fully implantable, bi‑directional neural prosthesis capable of **restoring or augmenting human vision** through direct cortical stimulation.

At its core, the system uses **computer‑generated holography (CGH)** to encode 3D visual scenes into spatiotemporal neural stimulation patterns. These patterns are delivered to the **thalamic reticular nucleus (TRN)** and primary visual cortex (V1), leveraging the brain's natural plasticity to create a **perceptually seamless visual experience**.

The framework is scientifically grounded in:
- **Thalamocortical electrophysiology** (TRN burst/tonic firing modes)
- **Fourier optics & holography** (Fresnel propagation, angular spectrum method)
- **Neural coding theory** (rate coding, phase coding, population coding)
- **Organoid intelligence** (3D neural cultures for closed‑loop calibration)

## Core Concepts

### 1. Thalamic Reticular Nucleus (TRN)
The TRN acts as the **gatekeeper of sensory information**. It regulates the flow of visual, auditory, and somatosensory signals to the cortex. The implant modulates TRN activity using:
- **Tonic stimulation** (~22 Hz) for wakeful attention
- **Burst stimulation** (~10 Hz intra‑burst) for sensory gating
- **Spindle oscillations** (7–15 Hz) for sleep/wake transitions

### 2. Holographic Tomography
A 3D object is encoded as a **holographic interference pattern** using:
- **Fresnel diffraction** for propagation from object to hologram plane
- **Angular spectrum method** for fast, FFT‑based computation
- **Off‑axis reference wave** to separate real and virtual images

### 3. Neural Stimulation Mapping
The hologram is mapped to electrical stimulation parameters:
- **Amplitude** → charge per pulse (0–2.8 V)
- **Phase** → pulse timing (synchronised with TRN rhythms)
- **Frequency** → spatial gradient encoding (edge detection)

## Mathematical Framework

| **Component** | **Equation** |
| :--- | :--- |
| Fresnel Propagation | \( U_o(x,y) = \dfrac{e^{i k z_o}}{i \lambda z_o} \iint A_o(x_o,y_o) \, \exp\!\left[ \dfrac{i k}{2 z_o} \left( (x-x_o)^2 + (y-y_o)^2 \right) \right] dx_o dy_o \) |
| Angular Spectrum | \( H(f_x, f_y) = \exp\!\left( i k z_o \sqrt{1 - (\lambda f_x)^2 - (\lambda f_y)^2} \right) \) |
| Hologram Intensity | \( I(x,y) = |U_{\text{obj}} + U_{\text{ref}}|^2 \) |
| Stimulation Amplitude | \( V_{\text{stim}}(x,y) = V_{\max} \sqrt{ I(x,y) / I_{\max} } \) |
| Stimulation Phase | \( \phi_{\text{stim}}(x,y) = \arg( U_{\text{obj}} + U_{\text{ref}} ) \) |
| Stimulation Frequency | \( f_{\text{stim}}(x,y) = f_{\text{carrier}} + \alpha \cdot \|\nabla \phi_{\text{stim}}(x,y)\| \) |

## Neural Coding Chain

3D object → Hologram → Stimulation parameters → Electrode Array → TRN → Visual Cortex → Perception

The **closed‑loop architecture** allows the system to:
1. **Record** neural responses during stimulation
2. **Decode** the perceived shape from TRN spike trains
3. **Adapt** stimulation parameters in real time to improve fidelity

## Simulation Software

### Included Scripts

| **Script** | **Description** |
| :--- | :--- |
| `hologram_generator.py` | Generates a holographic stimulus from a 3D shape (circle, square, triangle) |
| `trn_simulator.py` | Simulates realistic TRN spike trains (wake, SWS, REM states) |
| `stimulus_mapper.py` | Maps hologram intensity to stimulation parameters (V, φ, f) |
| `pixel_visualizer.py` | Animated pixel‑wise stimulation sequence (16×16 grid) |
| `equation_renderer.py` | Creates publication‑ready PNGs of all equations and explanations |

### Requirements

- Python 3.9+
- NumPy 1.24+
- Matplotlib 3.7+

Install dependencies:
```bash
pip install numpy matplotlib


