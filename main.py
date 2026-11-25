import os

# Verified count: 134 characters (134 UTF-8 bytes), no trailing newline.
LINE = (
    "Lights out. The house went dark, the Wi-Fi died, "
    "and for the first time in years I heard what silence "
    "actually sounds like. It snores."
)

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8', newline='') as f:
    f.write(LINE)

print(len(LINE.encode('utf-8')))
