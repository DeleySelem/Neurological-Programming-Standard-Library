#!/usr/bin/env python3
"""
Render all mathematical equations with neurological explanations as PNG images.
"""

import matplotlib.pyplot as plt
from utils import create_fig_with_text

def wrap_text(text, width=80):
    """Simple line wrapping for display text."""
    words = text.split()
    lines = []
    current = []
    for w in words:
        if sum(len(x) for x in current) + len(current) + len(w) > width:
            lines.append(' '.join(current))
            current = [w]
        else:
            current.append(w)
    if current:
        lines.append(' '.join(current))
    return '\n'.join(lines)

def render_equations():
    """Generate all equation PNGs."""
    equations = [
        {
            'title': '1. Fresnel Propagation',
            'text': (
                "FRESNEL PROPAGATION (Object → Hologram Plane)\n\n"
                r"$U_o(x,y) = \dfrac{e^{i k z_o}}{i \lambda z_o} \iint A_o(x_o,y_o) \,"
                r"\exp\!\left[ \dfrac{i k}{2 z_o} \left( (x-x_o)^2 + (y-y_o)^2 \right) \right] dx_o dy_o$"
                "\n\n"
                r"where $k = 2\pi/\lambda$ is the wavenumber, $\lambda$ is the wavelength, "
                r"and $z_o$ is the object distance."
                "\n\n"
                "NEUROLOGICAL BASIS:\n"
                "The holographic field represents the spatiotemporal pattern of light "
                "reflected from a 3D object. In the implant, this wavefront is converted "
                "into a sequence of electrical pulses that stimulate the visual cortex. "
                "The depth $z_o$ corresponds to the perceived depth of the visual feature, "
                "which is encoded in the timing (phase) of the neural bursts."
            ),
            'filename': 'eqn_1_fresnel_propagation.png'
        },
        {
            'title': '2. Angular Spectrum Propagation',
            'text': (
                "ANGULAR SPECTRUM PROPAGATION (Fast Computation)\n\n"
                r"$U_{\text{obj}}(x,y) = \mathcal{F}^{-1}\!\left\{ \mathcal{F}\{U_{\text{obj}}\} \cdot H \right\}$"
                "\n\n"
                r"with $H(f_x, f_y) = \exp\!\left( i k z_o \sqrt{1 - (\lambda f_x)^2 - (\lambda f_y)^2} \right)$"
                "\n\n"
                r"where $\mathcal{F}$ denotes the 2D Fourier transform, and $(f_x, f_y)$ are spatial frequencies."
                "\n\n"
                "NEUROLOGICAL BASIS:\n"
                "This frequency‑domain approach efficiently computes the propagation "
                "of the object wave. In the neural implant, the same principle is used "
                "to focus stimulation onto specific cortical columns, analogous to "
                "steering a beam of light. The transfer function $H$ determines the "
                "phase delays for each spatial frequency, which directly corresponds "
                "to the timing of bursts in the TRN (thalamic reticular nucleus)."
            ),
            'filename': 'eqn_2_angular_spectrum.png'
        },
        {
            'title': '3. Off‑Axis Hologram',
            'text': (
                "OFF‑AXIS HOLOGRAM (Interference Pattern)\n\n"
                r"$I(x,y) = |U_{\text{obj}} + U_{\text{ref}}|^2$"
                "\n\n"
                r"where $U_{\text{ref}} = A_{\text{ref}} \exp\!\left( i 2\pi (f_{xr} x + f_{yr} y) \right)$"
                "\n\n"
                "Expanding:\n"
                r"$I = |U_{\text{obj}}|^2 + |U_{\text{ref}}|^2 + U_{\text{obj}} U_{\text{ref}}^* + U_{\text{obj}}^* U_{\text{ref}}$"
                "\n\n"
                "NEUROLOGICAL BASIS:\n"
                "The hologram encodes both amplitude and phase information. In the "
                "implant, the recorded intensity $I(x,y)$ is used to modulate the "
                "amplitude of electrical pulses. The reference wave provides a carrier "
                "frequency (90 Hz) that, when combined with the object wave, creates "
                "a beat pattern. This beat is analogous to the binaural beat used in "
                "auditory entrainment, but here it drives the TRN's gamma oscillations "
                "at 40 Hz, facilitating attention and sensory gating."
            ),
            'filename': 'eqn_3_hologram_formation.png'
        },
        {
            'title': '4. Stimulation Parameter Mapping',
            'text': (
                "STIMULATION PARAMETER MAPPING (Hologram → Pulses)\n\n"
                r"Amplitude:   $V_{\text{stim}}(x,y) = V_{\max} \sqrt{ \dfrac{I(x,y)}{I_{\max}} }$"
                "\n\n"
                r"Phase:       $\phi_{\text{stim}}(x,y) = \arg( U_{\text{obj}} + U_{\text{ref}} )$"
                "\n\n"
                r"Frequency:   $f_{\text{stim}}(x,y) = f_{\text{carrier}} + \alpha \cdot \|\nabla \phi_{\text{stim}}(x,y)\|$"
                "\n\n"
                r"where $\alpha$ is a gain factor (here 5.0 Hz per rad/m)."
                "\n\n"
                "NEUROLOGICAL BASIS:\n"
                "The implant delivers biphasic pulses (±2.8 V) with a 200 µs pulse width. "
                "The amplitude modulates the charge injected per pulse, directly "
                "affecting the recruitment of cortical neurons. The phase determines "
                "the onset timing of each pulse, which synchronizes with the ongoing "
                "TRN rhythms. The frequency modulation encodes spatial gradients, "
                "allowing the system to transmit edge information (similar to the "
                "function of simple cells in V1)."
            ),
            'filename': 'eqn_4_stimulation_mapping.png'
        },
        {
            'title': '5. Reconstruction (Tomography)',
            'text': (
                "RECONSTRUCTION (Tomographic View)\n\n"
                r"$U_r(x_r, y_r) = \dfrac{e^{i k z_r}}{i \lambda z_r} \iint I(x,y) \,"
                r"\exp\!\left[ \dfrac{i k}{2 z_r} \left( (x-x_r)^2 + (y-y_r)^2 \right) \right] dx\,dy$"
                "\n\n"
                r"By scanning $z_r$ (the reconstruction depth), a 3D volume is obtained."
                "\n\n"
                "NEUROLOGICAL BASIS:\n"
                "This inverse propagation is analogous to the brain's ability to "
                "reconstruct depth from binocular disparity and motion parallax. "
                "In the implant, the reconstructed amplitude $|U_r|$ corresponds to "
                "the perceived brightness of the object at that depth. The TRN's "
                "spindle oscillations (7–15 Hz) are thought to synchronise these "
                "depth‑selective responses, enabling the brain to segregate objects "
                "in the visual scene."
            ),
            'filename': 'eqn_5_reconstruction.png'
        },
        {
            'title': '6. Neural Coding Chain',
            'text': (
                "NEURAL CODING CHAIN (Hologram → Perception)\n\n"
                "Signal flow:\n"
                "  3D Object → Hologram → Stimulation → TRN → Cortex\n\n"
                "Key transformations:\n"
                r"  • Hologram $I(x,y)$ → Amplitude $V_{\text{stim}}$ and Phase $\phi_{\text{stim}}$"
                "\n"
                r"  • TRN responds with spike‑bursts (accelerando‑decelerando patterns)"
                "\n"
                r"  • The envelope of the 90 Hz carrier is extracted as the shape signal"
                "\n"
                r"  • Depth is decoded from the phase delays across the electrode array"
                "\n\n"
                "NEUROLOGICAL FOUNDATION:\n"
                "The thalamic reticular nucleus (TRN) acts as the gatekeeper of "
                "sensory information. During wakefulness, it fires in a tonic mode "
                "(~22 Hz), while in slow‑wave sleep it generates spindle oscillations "
                "(7–15 Hz) and high‑frequency bursts. The implant's stimulation "
                "parameters are designed to mimic these natural patterns, leveraging "
                "the TRN's role in attention and sensory selection. The extracted "
                "shape envelope is derived from the demodulated carrier, providing "
                "a direct readout of the visual stimulus that can be fed back to "
                "the implant for closed‑loop calibration."
            ),
            'filename': 'eqn_6_neural_coding_chain.png'
        }
    ]
    
    # Render each equation
    for eq in equations:
        # Wrap long lines for display
        wrapped = wrap_text(eq['text'], width=80)
        create_fig_with_text(wrapped, title=eq['title'],
                             save_path=eq['filename'],
                             figsize=(10, 8))
        print(f"✅ Saved {eq['filename']}")

if __name__ == "__main__":
    render_equations()
    print("All equation PNGs generated.")
