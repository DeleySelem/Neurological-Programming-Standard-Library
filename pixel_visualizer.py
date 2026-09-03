#!/usr/bin/env python3
"""
Animated pixel‑wise stimulation sequence for retinal/cortical implant.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_pixel_animation(grid_size=16, hold_ms=60, duration=5.0):
    """
    Create an animation of sequential pixel stimulation.
    
    Args:
        grid_size (int): number of pixels per side (total = grid_size^2)
        hold_ms (int): milliseconds each pixel stays active
        duration (float): total animation duration in seconds
    
    Returns:
        animation.FuncAnimation
    """
    total_pixels = grid_size * grid_size
    frames = int(duration * 1000 / hold_ms)  # number of steps
    indices = np.arange(total_pixels)
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title('Pixel Stimulation Sequence')
    
    # Precompute grid positions
    cell_size = 1.0 / grid_size
    rects = []
    for i in range(total_pixels):
        row = i // grid_size
        col = i % grid_size
        x = col * cell_size
        y = (grid_size - 1 - row) * cell_size  # flip y for display
        rect = plt.Rectangle((x, y), cell_size, cell_size,
                             edgecolor='none', facecolor='darkblue')
        ax.add_patch(rect)
        rects.append(rect)
    
    def update(frame):
        # Calculate current pixel index (cycling)
        idx = frame % total_pixels
        # Reset all to dim
        for i, rect in enumerate(rects):
            if i == idx:
                rect.set_facecolor('cyan')
            else:
                rect.set_facecolor('darkblue')
        return rects
    
    ani = animation.FuncAnimation(fig, update, frames=frames,
                                  interval=hold_ms, blit=True)
    return ani

if __name__ == "__main__":
    ani = create_pixel_animation(grid_size=16, hold_ms=60, duration=3.0)
    # To save as GIF: ani.save('pixel_animation.gif', writer='pillow')
    plt.show()
