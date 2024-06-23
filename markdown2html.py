import sys
import os.path

def convert_markdown_to_html(markdown_file, output_file):
    """
    Converts a Markdown file to HTML.

    Args:
        markdown_file (str): Path to the Markdown file.
        output_file (str): Path to the output HTML file.

    Raises:
        FileNotFoundError: If the Markdown file does not exist.
    """
    # Check if markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
    
    # Read Markdown content
    with open(markdown_file, 'r') as f:
        markdown_content = f.read()
    
    # In a real scenario, implement Markdown to HTML conversion logic here
    # For demonstration, just writing Markdown content to output file
    with open(output_file, 'w') as f:
        f.write(markdown_content)
    
    sys.exit(0)

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)
    
    # Extract arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Convert Markdown to HTML
    convert_markdown_to_html(input_file, output_file)
