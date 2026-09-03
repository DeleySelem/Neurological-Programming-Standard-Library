#!/usr/bin/env python3
"""
Main entry point for the Neurological Programming Framework.
Run individual modules or all together.
"""

import sys
import argparse
from hologram_generator import generate_hologram, plot_hologram
from trn_simulator import generate_trn_spike_train, plot_trn
from pixel_visualizer import create_pixel_animation
from equation_renderer import render_equations

def main():
    parser = argparse.ArgumentParser(description='Neurological Programming Framework')
    parser.add_argument('--hologram', action='store_true', help='Generate hologram')
    parser.add_argument('--trn', action='store_true', help='Simulate TRN')
    parser.add_argument('--pixel', action='store_true', help='Run pixel animation')
    parser.add_argument('--equations', action='store_true', help='Render equation PNGs')
    parser.add_argument('--all', action='store_true', help='Run all modules')
    args = parser.parse_args()
    
    if args.all or args.hologram:
        data = generate_hologram(shape='square', N=128)
        plot_hologram(data, save_path='holographic_stimulus.png')
        print("✅ Hologram saved.")
    
    if args.all or args.trn:
        t, spikes, lfp, rate = generate_trn_spike_train(state='sws', duration=2.0)
        plot_trn(t, spikes, lfp, state='sws', save_path='trn_wave_data.png')
        print(f"✅ TRN simulation saved. Mean rate: {rate:.2f} Hz")
    
    if args.all or args.pixel:
        ani = create_pixel_animation(grid_size=16, hold_ms=60, duration=3.0)
        # To save: ani.save('pixel_animation.gif', writer='pillow')
        plt.show()
    
    if args.all or args.equations:
        render_equations()
        print("✅ Equation PNGs saved.")
    
    if not any(vars(args).values()):
        print("No action specified. Use --all or individual flags (--hologram, --trn, --pixel, --equations)")

if __name__ == "__main__":
    main()
