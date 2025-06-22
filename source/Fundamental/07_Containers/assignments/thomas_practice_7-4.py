def main():
    rows, cols = 4, 3
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter matrix value [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)

    # sum and display each element
    total = 0
    for i in range(rows):
        for j in range(cols):
            total += matrix[i][j]

    print(matrix)
    print(f"Total: {total}")

if __name__ == "__main__":
    main()