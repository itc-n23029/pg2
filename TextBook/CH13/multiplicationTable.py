import sys
import pandas as pd

def create_multiplication_table(n):
    table = [[(i+1)*(j+1) for j in range(n)] for i in range(n)]
    
    df = pd.DataFrame(table)
    
    filename = f"multiplication_table_{n}x{n}.xlsx"
    df.to_excel(filename, index=False, header=False)
    print(f"Multiplication table saved to {filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python multiplicationTable.py <N>")
        return
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for N")
        return
    
    create_multiplication_table(n)

if __name__ == "__main__":
    main()

