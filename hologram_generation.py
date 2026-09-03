#!/usr/bin/env python3
"""
Generate holographic stimulus from a 3D shape and map to stimulation parameters.
"""

import numpy as np
import matplotlib.pyplot as plt
from utils import fft_shift_2d, ifft_shift_2d

def generate_hologram(shape='circle', N=128, wavelength=0.5e-6, pitch=5e-6, z_obj=0.15, ref_freq=1e5):
    """
    Generate off-axis hologram of a 2D shape at distance z_obj.
    
    Args:
        shape (str): 'circle', 'square', 'triangle'
        N (int): grid size (power of 2)
        wavelength (float): optical wavelength in meters
        pitch (float): pixel pitch in meters
        z_obj (float): object distance in meters
        ref_freq (float): reference spatial frequency (1/m)
    
    Returns:
        dict: containing hologram, object amplitude, stimulation parameters
    """
    # Coordinate grid
    x = np.linspace(-N/2, N/2, N, endpoint=False) * pitch
    X, Y = np.meshgrid(x, x)
    
    # Object amplitude
    radius = 20 * pitch
    if shape == 'circle':
        A_obj = np.sqrt(X**2 + Y**2) < radius
    elif shape == 'square':
        A_obj = (np.abs(X) < radius) & (np.abs(Y) < radius)
    elif shape == 'triangle':
        # Simple isosceles triangle
        A_obj = (Y > -radius) & (Y < radius) & (X > -radius) & (X < radius)
        # Not perfect, but approximate
        A_obj = A_obj & (X < -Y + radius) & (X < Y + radius)
    else:
        raise ValueError("Shape must be 'circle', 'square', or 'triangle'")
    
    # Object phase (random scattering)
    phi_obj = np.random.rand(N, N) * 2 * np.pi
    
    # Object field
    U_obj = A_obj * np.exp(1j * phi_obj)
    
    # Angular spectrum propagation
    k = 2 * np.pi / wavelength
    fx = np.fft.fftfreq(N, pitch)
    fy = np.fft.fftfreq(N, pitch)
    FX, FY = np.meshgrid(fx, fy)
    H = np.exp(1j * k * z_obj * np.sqrt(1 - (wavelength * FX)**2 - (wavelength * FY)**2))
    
    U_obj_fft = np.fft.fft2(U_obj)
    U_obj_h = np.fft.ifft2(U_obj_fft * H)
    
    # Reference wave
    U_ref = np.exp(1j * 2 * np.pi * ref_freq * X)
    
    # Hologram intensity
    I_hologram = np.abs(U_obj_h + U_ref)**2
    
    # Stimulation parameters
    V_max = 2.8  # Volts
    V_stim = V_max * np.sqrt(I_hologram / np.max(I_hologram))
    phase_stim = np.angle(U_obj_h + U_ref)
    
    # Frequency modulation from phase gradient
    grad_y, grad_x = np.gradient(phase_stim)
    grad_mag = np.sqrt(grad_x**2 + grad_y**2)
    f_carrier = 90.0  # Hz
    alpha = 5.0       # Hz per rad/m
    f_stim = f_carrier + alpha * grad_mag
    
    return {
        'A_obj': A_obj,
        'U_obj_h': U_obj_h,
        'I_hologram': I_hologram,
        'V_stim': V_stim,
        'phase_stim': phase_stim,
        'f_stim': f_stim,
        'X': X,
        'Y': Y
    }

def plot_hologram(data, save_path=None):
    """Plot hologram and stimulation parameters."""
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    axes[0, 0].imshow(data['A_obj'], cmap='gray')
    axes[0, 0].set_title('Object amplitude')
    axes[0, 1].imshow(np.real(data['U_obj_h']), cmap='RdBu')
    axes[0, 1].set_title('Real part of object wave')
    axes[0, 2].imshow(data['I_hologram'], cmap='gray')
    axes[0, 2].set_title('Hologram intensity')
    
    axes[1, 0].imshow(data['V_stim'], cmap='plasma')
    axes[1, 0].set_title('Stimulation amplitude (V)')
    axes[1, 1].imshow(data['phase_stim'], cmap='hsv')
    axes[1, 1].set_title('Stimulation phase (rad)')
    axes[1, 2].imshow(data['f_stim'], cmap='viridis')
    axes[1, 2].set_title('Stimulation frequency (Hz)')
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        plt.close(fig)
    else:
        plt.show()

if __name__ == "__main__":
    # Example: generate hologram for a square
    data = generate_hologram(shape='square', N=128)
    plot_hologram(data, save_path='holographic_stimulus.png')
    print("✅ Hologram saved as 'holographic_stimulus.png'")
