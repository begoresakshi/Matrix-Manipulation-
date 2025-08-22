import numpy as np
import matplotlib.pyplot as plt


def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements for {name} row by row, separated by spaces:")
    data = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            raise ValueError("Number of elements does not match columns.")
        data.append(row)
    return np.array(data)


def visualize_matrix_interactive(matrix, title="Matrix"):
    fig, ax = plt.subplots()
    ax.set_axis_off()
    rows, cols = matrix.shape
    texts = []

    for i in range(rows):
        for j in range(cols):
            text = f"[{matrix[i, j]:.2f}]"
            t = ax.text(j, rows - i - 1, text, ha='center', va='center', fontsize=14,
                        bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=0.3'))
            texts.append((t, i, j))

    ax.set_xlim(-0.5, cols - 0.5)
    ax.set_ylim(-0.5, rows - 0.5)
    ax.set_title(title)
    plt.gca().invert_yaxis()

    plt.show()


def main():
    print("Matrix Operations (Interactive Output)\n")
    while True:
        print("\nSupported operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")

        choice = input("Choose an operation (1-6): ").strip()

        if choice == '6':
            print("Exiting program.")
            break

        if choice not in {'1', '2', '3', '4', '5'}:
            print("Invalid choice. Please enter a number between 1 and 6.\n")
            continue

        try:
            if choice in {'1', '2', '3'}:
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")

                if choice == '1':  # Add
                    if A.shape != B.shape:
                        print("Error: Matrices must have the same shape for addition.\n")
                        continue
                    result = A + B
                    print("Result (A + B):")

                elif choice == '2':  # Subtract
                    if A.shape != B.shape:
                        print("Error: Matrices must have the same shape for subtraction.\n")
                        continue
                    result = A - B
                    print("Result (A - B):")

                elif choice == '3':  # Multiply
                    if A.shape[1] != B.shape[0]:
                        print("Error: Number of columns of A must equal number of rows of B for multiplication.\n")
                        continue
                    result = np.matmul(A, B)
                    print("Result (A x B):")

                print(result)
                visualize_matrix_interactive(result, "Result Matrix")

            elif choice == '4':  # Transpose
                A = input_matrix("Matrix A")
                result = A.T
                print("Result (Transpose of A):")
                print(result)
                visualize_matrix_interactive(result, "Transpose Matrix")

            elif choice == '5':  # Determinant
                A = input_matrix("Matrix A")
                if A.shape[0] != A.shape[1]:
                    print("Error: Matrix must be square for determinant.\n")
                    continue
                det = np.linalg.det(A)
                print(f"Determinant of Matrix A: {det:.4f}\n")

        except ValueError as ve:
            print(f"Input error: {ve}\n")
        except Exception as e:
            print(f"Unexpected error: {e}\n")


if __name__ == "__main__":
    main()
