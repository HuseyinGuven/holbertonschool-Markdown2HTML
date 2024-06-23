import sys
import os.path

def convert_markdown_to_html(markdown_file, output_file):
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
    
    with open(markdown_file, 'r') as f:
        markdown_content = f.read()
    
    with open(output_file, 'w') as f:
        f.write(markdown_content)
    
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    convert_markdown_to_html(input_file, output_file)
