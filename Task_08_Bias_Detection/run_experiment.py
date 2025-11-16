import glob
import json
from datetime import datetime

results = []

prompt_files = sorted(glob.glob("prompts/*.txt"))

for pf in prompt_files:
    with open(pf, "r") as f:
        text = f.read()

    for sample in range(3):  # 3 runs per prompt
        print(f"Running {pf} sample {sample+1}")

        output = call_model(text)

        results.append({
            "prompt_file": pf,
            "sample_id": sample+1,
            "prompt": text,
            "response": output,
            "timestamp": datetime.utcnow().isoformat()
        })

with open("results/raw_responses.json", "w") as f:
    json.dump(results, f, indent=2)

print("Experiment done!")
