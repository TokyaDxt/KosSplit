from __future__ import annotations

from decimal import Decimal, ROUND_FLOOR


def rupiah(value: int) -> str:
    """Indonesian Rupiah with dot separators; negatives read '-Rp100.000'."""
    number = int(value)
    sign = "-" if number < 0 else ""
    return f"{sign}Rp{abs(number):,}".replace(",", ".")


def allocate_weighted(total: int, weights: dict[int, Decimal]) -> dict[int, int]:
    """Allocate every rupiah deterministically with largest remainders."""
    if total < 0:
        raise ValueError("Total tidak boleh negatif")
    if not weights or any(weight < 0 for weight in weights.values()):
        raise ValueError("Bobot pembagian tidak valid")
    weight_total = sum(weights.values(), Decimal(0))
    if weight_total <= 0:
        raise ValueError("Total bobot harus lebih dari nol")

    exact = {
        key: Decimal(total) * weight / weight_total for key, weight in weights.items()
    }
    result = {
        key: int(value.to_integral_value(rounding=ROUND_FLOOR))
        for key, value in exact.items()
    }
    remainder = total - sum(result.values())
    order = sorted(
        exact,
        key=lambda key: (exact[key] - Decimal(result[key]), -key),
        reverse=True,
    )
    for key in order[:remainder]:
        result[key] += 1
    return result
