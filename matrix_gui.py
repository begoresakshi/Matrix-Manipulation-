import numpy as np
import matplotlib.pyplot as plt

def show_matrix(matrix, title="Result Matrix"):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_axis_off()
    
    rows, cols = matrix.shape

    # Add title centered at the top
    plt.text(cols/2 - 0.5, rows + 0.3, title, ha='center', va='bottom', fontsize=16, fontweight='bold')
    
    # Plot each matrix element as text inside a box
    for i in range(rows):
        for j in range(cols):
            val_str = f"[{matrix[i,j]:.2f}]"
            ax.text(j, rows - i - 1, val_str, ha='center', va='center',
                    fontsize=14, fontfamily='monospace',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='black'))
    
    ax.set_xlim(-0.5, cols - 0.5)
    ax.set_ylim(-0.5, rows - 0.5)
    plt.gca().invert_yaxis()
    
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    matrix = np.array([[10, 14], [6, 8]])
    show_matrix(matrix)
