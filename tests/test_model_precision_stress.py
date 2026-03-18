from __future__ import annotations

from model.precision_stress import (
    check_precision_range,
    check_precision_scheme_range,
    PrecisionStressRunner,
)


def test_float64_and_float32_pass_small_exhaustive_ranges() -> None:
    for fmt in ("float64", "float32"):
        assert check_precision_range(64, fmt=fmt, kind="identity", mode="exhaustive").passed is True
        assert check_precision_range(64, fmt=fmt, kind="latest_write", mode="exhaustive").passed is True


def test_bfloat16_breaks_identity_retrieval_early() -> None:
    result = check_precision_range(32, fmt="bfloat16", kind="identity", mode="exhaustive")

    assert result.passed is False
    assert result.first_failure is not None
    assert result.first_failure.query_address == 16


def test_float16_breaks_latest_write_tie_break_early() -> None:
    result = check_precision_range(16, fmt="float16", kind="latest_write", mode="exhaustive")

    assert result.passed is False
    assert result.first_failure is not None
    assert result.first_failure.query_address == 8


def test_single_head_scheme_matches_legacy_check_for_small_ranges() -> None:
    legacy = check_precision_range(64, fmt="float32", kind="latest_write", mode="local")
    scheme = check_precision_scheme_range(
        64,
        fmt="float32",
        kind="latest_write",
        mode="local",
        scheme="single_head",
    )

    assert scheme.passed == legacy.passed
    assert (None if scheme.first_failure is None else scheme.first_failure.query_address) == (
        None if legacy.first_failure is None else legacy.first_failure.query_address
    )


def test_radix2_scheme_extends_float32_latest_write_range() -> None:
    single_head = check_precision_scheme_range(
        2048,
        fmt="float32",
        kind="latest_write",
        mode="local",
        scheme="single_head",
    )
    radix2 = check_precision_scheme_range(
        2048,
        fmt="float32",
        kind="latest_write",
        mode="local",
        scheme="radix2",
        base=64,
    )

    assert single_head.passed is False
    assert radix2.passed is True


def test_precision_runner_sweep_records_rows() -> None:
    runner = PrecisionStressRunner(fmt="float32", scheme="block_recentered", base=64)
    report = runner.sweep((64, 128), kind="identity", mode="local")

    assert report.scheme == "block_recentered"
    assert len(report.rows) == 2
