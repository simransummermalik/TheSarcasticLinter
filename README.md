# TheSarcasticLinter
 The Sarcastic Linter is a Python code linter with an attitude. It doesn't just find issues like too many imports, infinite loops, or sloppy indentation..it makes fun of you for them. 
# More
 The linter uses a built in ast import to parse the input file into an AST, this then allows it to analyze the structure of the code. 
 # Issues the linter can detect
 - Imports: Catches unnesscary imports to discourage overcomplicated code
 - Functions: Can identify unused variables, empty functions and functions that may be too long to encourage better and efficient code
 - "Magic Numbers": this is random hardcoded numbers with no assigned/random values
 - Loops: Catches infinite loops
 - Variable names: Catches vague variable names in order to make code less confusing
 - Print statements: Catches overly excessive print statements
 - Improper indentation: self explanatory, one of the biggest issues begginers to python face
