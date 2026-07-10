with open('sections/recently-viewed-paired.liquid', 'r') as f:
    text = f.read()
import re
tags = re.findall(r'{%\s*(.*?)\s*%}', text)

stack = []
for tag in tags:
    parts = tag.split()
    if not parts: continue
    name = parts[0]
    if name in ['if', 'for', 'unless', 'capture', 'case', 'paginate', 'form', 'style']:
        stack.append(name)
    elif name.startswith('end'):
        expected = name[3:]
        if not stack:
            print(f"Error: unexpected {name}")
        elif stack[-1] != expected:
            print(f"Error: expected end{stack[-1]}, got {name}")
        else:
            stack.pop()

if stack:
    print("Error: unclosed tags:", stack)
else:
    print("All tags matched.")
