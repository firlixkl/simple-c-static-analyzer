# Simple C Static Analyzer

## Purpose
The Simple C Static Analyzer is a tool designed to analyze C source code for potential errors, coding style violations, and other static analysis purposes. This tool aims to assist developers in improving code quality and adhering to coding standards.

## Project Structure

```
Simple-C-Static-Analyzer/
|-- StaticCAnalyzer/
|   |-- README.md       # Comprehensive description of the project structure and purpose
|   |-- Analyzer.c      # Contains the main analysis logic
|   |-- Checker.h       # Header file for the analysis functions
|   |-- utils.c         # Various utility functions used in the analysis
|   |-- utils.h         # Header file for utility functions
|-- tests/
|   |-- test_analyzer.c # Unit tests for the analyzer
|-- .gitignore           # Specifies files/folders to ignore in Git
|-- Makefile             # Build instructions for the project
|-- LICENSE              # Licensing information for using this project
|-- README.md            # Main project overview and instructions
```

## How to Use
1. Clone the repository: `git clone https://github.com/firlixkl/simple-c-static-analyzer.git`
2. Navigate to the `StaticCAnalyzer` directory.
3. Build the project using the provided Makefile: `make`
4. Run the analyzer on your C source files.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.
