"""Export the current Python/Torch runtime environment for reproducibility."""

from __future__ import annotations

import json
from pathlib import Path

from utils import detect_runtime_environment, project_virtual_env


def main() -> None:
    environment = detect_runtime_environment()
    output = {
        "experiment": "runtime_environment",
        "project_virtual_env": project_virtual_env().as_posix(),
        "environment": environment.as_dict(),
    }

    out_path = Path("results/runtime_environment.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(out_path.as_posix())


if __name__ == "__main__":
    main()
