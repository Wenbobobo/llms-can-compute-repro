"""Export finite-precision stress checks for 2D latest-write addressing."""

from __future__ import annotations

import json
from pathlib import Path

from model import (
    check_precision_range,
    check_precision_scheme_range,
    sweep_precision_ranges,
    sweep_precision_scheme_ranges,
)

FORMATS = ("float64", "float32", "bfloat16", "float16")
EXHAUSTIVE_RANGES = (16, 32, 64)
LOCAL_RANGES = (16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192)
SCHEMES = (
    ("single_head", 64),
    ("radix2", 64),
    ("block_recentered", 64),
)


def encode_result(result):
    return {
        "fmt": result.fmt,
        "kind": result.kind,
        "mode": result.mode,
        "address_limit": result.address_limit,
        "max_steps": result.max_steps,
        "passed": result.passed,
        "first_failure": None
        if result.first_failure is None
        else {
            "query_address": result.first_failure.query_address,
            "expected_address": result.first_failure.expected_address,
            "expected_step": result.first_failure.expected_step,
            "competing_address": result.first_failure.competing_address,
            "competing_step": result.first_failure.competing_step,
            "expected_score": result.first_failure.expected_score,
            "competing_score": result.first_failure.competing_score,
        },
    }


def main() -> None:
    output = {
        "experiment": "m4_precision_stress",
        "notes": [
            "Scores are simulated by quantizing query/key components and intermediate arithmetic into the target format.",
            "Local checks compare the exact winner against the nearest wrong-address neighbors plus the older same-address write.",
            "Scheme-aware sweeps add two decomposition families: radix-2 address splitting and block-recentered local addressing.",
        ],
        "exhaustive_checks": {
            fmt: {
                kind: [
                    encode_result(
                        check_precision_range(address_limit, fmt=fmt, kind=kind, mode="exhaustive")
                    )
                    for address_limit in EXHAUSTIVE_RANGES
                ]
                for kind in ("identity", "latest_write")
            }
            for fmt in FORMATS
        },
        "local_sweeps": {
            fmt: {
                kind: [
                    {
                        "address_limit": row.address_limit,
                        "passed": row.passed,
                        "first_failure_query": row.first_failure_query,
                    }
                    for row in sweep_precision_ranges(LOCAL_RANGES, fmt=fmt, kind=kind, mode="local")
                ]
                for kind in ("identity", "latest_write")
            }
            for fmt in FORMATS
        },
        "scheme_local_sweeps": {
            fmt: {
                kind: {
                    scheme: [
                        {
                            "address_limit": row.address_limit,
                            "passed": row.passed,
                            "first_failure_query": row.first_failure_query,
                        }
                        for row in sweep_precision_scheme_ranges(
                            LOCAL_RANGES,
                            fmt=fmt,
                            kind=kind,
                            mode="local",
                            scheme=scheme,
                            base=base,
                        )
                    ]
                    for scheme, base in SCHEMES
                }
                for kind in ("identity", "latest_write")
            }
            for fmt in FORMATS
        },
        "scheme_exhaustive_checks": {
            fmt: {
                kind: {
                    scheme: [
                        {
                            "fmt": result.fmt,
                            "scheme": result.scheme,
                            "kind": result.kind,
                            "mode": result.mode,
                            "address_limit": result.address_limit,
                            "max_steps": result.max_steps,
                            "passed": result.passed,
                            "first_failure": None
                            if result.first_failure is None
                            else {
                                "query_address": result.first_failure.query_address,
                                "expected_address": result.first_failure.expected_address,
                                "expected_step": result.first_failure.expected_step,
                                "competing_address": result.first_failure.competing_address,
                                "competing_step": result.first_failure.competing_step,
                                "expected_scores": list(result.first_failure.expected_scores),
                                "competing_scores": list(result.first_failure.competing_scores),
                            },
                        }
                        for result in [
                            check_precision_scheme_range(
                                address_limit,
                                fmt=fmt,
                                kind=kind,
                                mode="exhaustive",
                                scheme=scheme,
                                base=base,
                            )
                            for address_limit in EXHAUSTIVE_RANGES
                        ]
                    ]
                    for scheme, base in SCHEMES
                }
                for kind in ("identity", "latest_write")
            }
            for fmt in FORMATS
        },
    }

    out_path = Path("results/M4_precision_scaling/summary.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(out_path.as_posix())


if __name__ == "__main__":
    main()
