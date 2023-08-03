import os

# Define the base path of the project
base_path = "/Users/tachikoma000/Documents/GitHub/pgGPT_discord/bot_system_main"

def analyze_imports(file_content):
    """Analyze the file content and identify imports"""
    lines = file_content.split("\n")
    imports = [line for line in lines if line.startswith("from") or line.startswith("import")]
    return imports

# Walk through the directory and subdirectories
for root, dirs, files in os.walk(base_path):
    for file in files:
        # We're only interested in Python files
        if file.endswith(".py"):
            # Get the full file path
            file_path = os.path.join(root, file)
            # Read the file content
            with open(file_path, 'r') as f:
                content = f.read()
            # Analyze the imports in the file
            imports = analyze_imports(content)
            # Print the imports
            print(f"In file {file_path}, found imports:")
            for imp in imports:
                print(f"    {imp}")
