import sys
import os.path
import re

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
    
    # Convert Markdown to HTML
    html_content = markdown_to_html(markdown_content)
    
    # Write HTML content to output file
    with open(output_file, 'w') as f:
        f.write(html_content)
    
    sys.exit(0)

def markdown_to_html(markdown_content):
    """
    Converts Markdown content to HTML.

    Args:
        markdown_content (str): Content of the Markdown file.

    Returns:
        str: Content converted to HTML.
    """
    # Regex pattern for detecting Markdown headings (e.g., ## Heading)
    heading_pattern = r'^(#+)\s+(.*)$'
    
    # Function to replace Markdown headings with HTML headings
    def replace_heading(match):
        level = len(match.group(1))  # Count of '#' determines heading level
        heading_text = match.group(2)
        html_heading = f'<h{level}>{heading_text}</h{level}>'
        return html_heading
    
    # Perform the replacement using the defined function
    html_content = re.sub(heading_pattern, replace_heading, markdown_content, flags=re.MULTILINE)
    
    return html_content

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
