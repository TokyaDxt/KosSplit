"""Indonesian display labels shared by the screens and the exported reports."""

from __future__ import annotations

MONTH_NAMES = (
    "Januari",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember",
)

METHOD_LABELS = {
    "equal": "Bagi rata",
    "custom_amount": "Nominal kustom",
    "percentage": "Persentase",
    "itemized": "Per item",
}

KIND_LABELS = {"expense": "Pengeluaran", "income": "Pemasukan"}


def period_label(period: str) -> str:
    """'2026-11' -> 'November 2026'."""
    return f"{MONTH_NAMES[int(period[5:7]) - 1]} {period[:4]}"


def date_label(value: str) -> str:
    """'2026-11-02' -> '2 Nov 2026'."""
    return f"{int(value[8:10])} {MONTH_NAMES[int(value[5:7]) - 1][:3]} {value[:4]}"
