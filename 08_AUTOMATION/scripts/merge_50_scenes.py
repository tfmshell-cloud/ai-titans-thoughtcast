#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os
sys.path.append("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/08_AUTOMATION/scripts")

from build_50_scenes_data_part1 import SCENES_PART1
from build_50_scenes_data_part2 import SCENES_PART2

ALL_SCENES = SCENES_PART1 + SCENES_PART2
print(f"Total merged scenes: {len(ALL_SCENES)}")

# Overwrite generate_50_scenes_hassabis.py
output_py = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/08_AUTOMATION/scripts/generate_50_scenes_hassabis.py"

with open(output_py, "w", encoding="utf-8") as f:
    f.write("#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n")
    f.write('"""\n50 Biographical Scenes / 3-Prompt Triads for Demis Hassabis (EP03)\n100% Policy-Safe (Zero Moderation Triggers)\n"""\n\n')
    f.write("import sys\n\n")
    f.write("from build_50_scenes_data_part1 import SCENES_PART1\n")
    f.write("from build_50_scenes_data_part2 import SCENES_PART2\n\n")
    f.write("SCENES = SCENES_PART1 + SCENES_PART2\n")

print(f"Successfully updated {output_py}")
