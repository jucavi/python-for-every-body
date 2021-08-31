def arithmetic_arranger(problems, solutions=False):
    arranged_problems = []
    sep = '-'
    
    if len(problems) > 5:
        return "Error: Too many problems."

    for operation in problems:
        num1, op, num2 = operation.split()
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if not op in "+-":
            return "Error: Operator must be '+' or '-'."

        max_len = max(len(num1), len(num2))
        
        arranged_problems.append([
            f'{num1:>{max_len + 2}}',
            f"{op} {num2:>{max_len}}",
            f"{sep * (max_len + 2)}"
        ])
        
        if solutions:
            arranged_problems[-1].append(f"{eval(operation):>{max_len + 2}}")
            
    lines = ("    ".join(line) for line in zip(*arranged_problems))
    
    return "\n".join(lines)