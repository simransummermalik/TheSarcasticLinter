import ast
import random

#comments
annoying_comments = {
    "TooManyImports": [
        "Wow, importing the entire Python standard library? Ambitious!",
        "Who needs minimalism when you can just import everything?",
        "Imports are great, but have you tried coding without them for a challenge?"
    ],
    "LongFunction": [
        "This function is so long it should have its own Netflix series.",
        "Ever heard of breaking things into smaller pieces? No? Carry on then.",
        "If your function were a book, it’d be a bestseller. Maybe shorten it a bit?"
    ],
    "UnusedVariable": [
        "Oh, a variable that's never used! A true minimalist approach.",
        "Keeping unused variables for nostalgia? Cute.",
        "This variable is feeling lonely. Consider deleting it or giving it purpose."
    ],
    "MagicNumber": [
        "Hardcoding numbers, huh? Nothing screams 'future-proof' like magic numbers.",
        "Is this a magic trick? Where did that number come from?",
        "Ah yes, the secret sauce: hardcoded values with no explanation."
    ],
    "EmptyFunction": [
        "This function is emptier than my fridge on a Sunday.",
        "Ah, a function with no purpose. A true philosophical statement.",
        "Why bother writing a function if it’s going to do nothing? Bold move!"
    ],
    "InfiniteLoop": [
        "Infinite loops are great for heating up your laptop, not for solving problems.",
        "Do you have a plan to escape this loop? Because I don’t see one.",
        "This loop is more infinite than your coding patience."
    ],
    "RedundantPrint": [
        "Wow, another print statement. Debugging or a personal diary?",
        "Console logs everywhere! Your computer is about to confess its life story.",
        "How about one more print statement for good luck?"
    ],
    "VariableNameIssue": [
        "Variable names like 'x' and 'y' are cute, but what do they mean?",
        "Vague variable names make your code look mysterious... and unreadable.",
        "Ah yes, 'a' and 'b'. Very descriptive."
    ],
    "ImproperIndentation": [
        "Indentation so inconsistent it’s giving me whiplash.",
        "Mixing tabs and spaces? Revolutionary... and wrong.",
        "Indentation issues: the hallmark of pain."
    ]
}

# how issue is detected
def detect_issues(tree, code_lines):
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
            if len(node.names) > 3:  # too many imports
                issues.append("TooManyImports")
        if isinstance(node, ast.FunctionDef):
            if len(node.body) == 0:  #function gone
                issues.append(("EmptyFunction", node.lineno))
            elif len(node.body) > 10:  # function not used 
                issues.append("LongFunction")
        if isinstance(node, ast.Assign):
            if len(node.targets) > 1 and all(isinstance(t, ast.Name) for t in node.targets):
                issues.append("UnusedVariable") #function dne
            elif isinstance(node.value, ast.Constant) and isinstance(node.value.value, (int, float)):
                issues.append(("MagicNumber", node.lineno))
        if isinstance(node, ast.While):
            if isinstance(node.test, ast.Constant) and node.test.value is True:
                issues.append(("InfiniteLoop", node.lineno))
                #checking for more line issues?
    for i, line in enumerate(code_lines, start=1):
        if "print(" in line and code_lines.count("print(") > 5:  #too many print statements 
            issues.append(("RedundantPrint", i))
        if ";" in line and not line.strip().endswith(";"):  # semicolon was misplaced
            issues.append(("ImproperIndentation", i))
        if any(line.strip().startswith(c) for c in ["a", "b", "x", "y"]):
            issues.append(("VariableNameIssue", i))
    return issues
def generate_sarcasm(issue_type, line=None):
    if issue_type in annoying_comments:
        comment = random.choice(annoying_comments[issue_type])
        return f"[Line {line}] {comment}" if line else comment
    return "Your code is too amazing for words (or for me to understand)."
def infinite_linter(file_path):
    try:
        with open(file_path, "r") as f:
            code = f.read()
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            print(f"[Line {e.lineno}] Your code syntax is... creative. Maybe too creative?")
            return
        code_lines = code.splitlines()
        issues = detect_issues(tree, code_lines)
        print(f"Linting '{file_path}'... Here's what I think:")
        if issues:
            for issue in issues:
                if isinstance(issue, tuple):  
                    issue_type, line = issue
                    print(generate_sarcasm(issue_type, line))
                else:
                    print(generate_sarcasm(issue))
        else:
            print("No issues detected... or maybe I'm just too kind today.")
        
        print("\nLinting complete! Your code is now marginally more tolerable.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Are you sure it exists?")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the linter
if __name__ == "__main__":
    file_to_lint = input("Enter the path of the Python file to 'lint': ")
    infinite_linter(file_to_lint)
