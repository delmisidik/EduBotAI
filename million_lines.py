with open("million_lines.py", "w") as f:
    for i in range(1_000_000):
        f.write(f"print('This is line {i+1}')\n")
