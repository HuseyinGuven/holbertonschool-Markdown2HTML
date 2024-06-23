import sys
import os
import markdown

if len(sys.argv) != 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

if not os.path.exists(input_filename):
    sys.stderr.write(f"Missing {input_filename}\n")
    sys.exit(1)

with open(input_filename, 'r') as markdown_file:
    markdown_content = markdown_file.read()

html_content = markdown.markdown(markdown_content)

with open(output_filename, 'w') as html_file:
    html_file.write(html_content)

sys.exit(0)
