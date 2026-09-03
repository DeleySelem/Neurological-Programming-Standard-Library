#!/usr/bin/env python3
"""
Simulate extracellular recordings from the thalamic reticular nucleus (TRN)
in different states (wake, slow-wave sleep, REM).
"""

import numpy as np
import matplotlib.pyplot as plt
from utils import plot_wave

def generate_trn_spike_train(duration=1.0, dt=0.001, state='sws', seed=42):
    """
    Generate simulated TRN spike train and local field potential (LFP).
    
    Args:
        duration (float): duration in seconds
        dt (float): time step
        state (str): 'wake', 'sws', 'rem', 'transition'
        seed (int): random seed for reproducibility
    
    Returns:
        t (ndarray): time vector
        spikes (ndarray): binary spike events (0/1)
        lfp (ndarray): local field potential
        rate (float): mean firing rate
    """
    np.random.seed(seed)
    t = np.arange(0, duration, dt)
    spikes = np.zeros_like(t)
    lfp = np.zeros_like(t)
    
    # State parameters from published data
    if state == 'wake':
        tonic_rate = 22.0      # Hz
        burst_prob = 0.05
        spindle_amp = 0.0
        spindle_freq = 0.0
    elif state == 'sws':
        tonic_rate = 5.0
        burst_prob = 0.85
        spindle_amp = 0.6
        spindle_freq = 10.0
    elif state == 'rem':
        tonic_rate = 3.0
        burst_prob = 0.90
        spindle_amp = 0.3
        spindle_freq = 10.0
    else:  # transition
        tonic_rate = 28.0
        burst_prob = 0.20
        spindle_amp = 0.1
        spindle_freq = 8.0
    
    # Slow oscillation modulating burst probability
    slow_osc = 0.5 + 0.5 * np.sin(2 * np.pi * 0.25 * t + 0.3)
    burst_mod = burst_prob * slow_osc
    
    # Generate spikes
    for i in range(1, len(t)):
        # Tonic spikes (single, irregular)
        if np.random.rand() < tonic_rate * dt * 0.3:
            spikes[i] = 1
        
        # Burst spikes (with accelerando-decelerando pattern)
        if burst_mod[i] > 0.3:
            # Intra-burst frequency ~10 Hz with modulation
            burst_phase = (t[i] * 10.0) % 1.0
            freq_mod = 0.7 + 0.6 * np.sin(burst_phase * 2 * np.pi)
            instant_freq = 10.0 * freq_mod
            # Spike if within the burst window
            if (t[i] % (1.0 / instant_freq)) < dt * 2:
                spikes[i] = 1
    
    # Spindle LFP (field potential)
    spindle_env = 0.5 + 0.5 * np.sin(2 * np.pi * 0.08 * t)
    lfp = spindle_amp * spindle_env * np.sin(2 * np.pi * spindle_freq * t + 0.7)
    lfp += 0.05 * np.random.randn(len(t))  # background noise
    
    # Mean firing rate
    rate = np.sum(spikes) / duration
    
    return t, spikes, lfp, rate

def plot_trn(t, spikes, lfp, state, save_path=None):
    """Plot spike raster and LFP."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
    
    # Spike raster (eventplot)
    spike_times = t[spikes > 0]
    ax1.eventplot(spike_times, color='black', linewidths=0.8)
    ax1.set_ylabel('Spikes')
    ax1.set_title(f'TRN Spike Train – {state.upper()} state')
    ax1.set_xlim(0, t[-1])
    
    # LFP
    ax2.plot(t, lfp, color='navy', linewidth=1.5)
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('LFP (µV)')
    ax2.set_title('TRN Local Field Potential')
    ax2.grid(True, linestyle=':', alpha=0.3)
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=200, bbox_inches='tight')
        plt.close(fig)
    else:
        plt.show()

if __name__ == "__main__":
    # Simulate SWS state
    t, spikes, lfp, rate = generate_trn_spike_train(state='sws', duration=2.0)
    print(f"Mean firing rate: {rate:.2f} Hz")
    plot_trn(t, spikes, lfp, state='sws', save_path='trn_wave_data.png')
    print("✅ TRN simulation saved as 'trn_wave_data.png'")
