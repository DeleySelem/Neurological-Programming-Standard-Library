#!/usr/bin/env python3
"""
Common utilities for the neurological programming framework.
"""

import numpy as np
import matplotlib.pyplot as plt

def fft_shift_2d(arr):
    """Return centered 2D FFT shift."""
    return np.fft.fftshift(np.fft.fft2(arr))

def ifft_shift_2d(arr):
    """Inverse of fft_shift_2d."""
    return np.fft.ifft2(np.fft.ifftshift(arr))

def compute_spectrum(signal, fs):
    """
    Compute power spectrum of a 1D signal.
    Returns frequencies and magnitudes.
    """
    n = len(signal)
    f = np.fft.fftfreq(n, 1/fs)
    mag = np.abs(np.fft.fft(signal)) / n
    return f[:n//2], mag[:n//2]

def plot_wave(ax, t, signal, color, label, ylabel='Amplitude'):
    """Plot a waveform with clean styling."""
    ax.plot(t, signal, color=color, linewidth=1.5, label=label)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel(ylabel)
    ax.grid(True, linestyle=':', alpha=0.3)
    if label:
        ax.legend()

def plot_spectrum(ax, freq, mag, color, label):
    """Plot power spectrum."""
    ax.plot(freq, mag, color=color, linewidth=1.5, label=label)
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Magnitude')
    ax.grid(True, linestyle=':', alpha=0.3)
    ax.legend()

def create_fig_with_text(text, title=None, save_path=None, figsize=(10, 8)):
    """
    Create a figure with only text (for equations/explanations).
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.axis('off')
    if title:
        ax.set_title(title, fontsize=16, color='black')
    ax.text(0.05, 0.95, text, transform=ax.transAxes,
            verticalalignment='top', fontsize=13, color='black',
            linespacing=1.8)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=200, bbox_inches='tight')
        plt.close(fig)
    else:
        plt.show()
