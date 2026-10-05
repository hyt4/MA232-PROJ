"""Single source of truth for the MA 232 Project 1 data.

Transcribed from the assignment PDF (Project 1.pdf, pp. 2-3).
Do not edit without re-checking the PDF.
"""
import numpy as np

SECTORS = ["AGR", "MIN", "UTL", "CON", "MAN", "TRA", "INF", "FIN", "PRO", "GOV"]

SECTOR_NAMES = {
    "AGR": "Agriculture & Forestry",
    "MIN": "Mining & Extraction",
    "UTL": "Utilities (Electric, Gas, Water)",
    "CON": "Construction",
    "MAN": "Manufacturing",
    "TRA": "Transportation & Warehousing",
    "INF": "Information & Telecommunications",
    "FIN": "Finance, Insurance, & Real Estate",
    "PRO": "Professional & Business Services",
    "GOV": "Government & Public Infrastructure",
}

# c[i][j] = value of sector i's output used by sector j per unit of sector j's output.
# Column j = inputs required by sector j.
C = np.array([
    [0.12, 0.01, 0.00, 0.05, 0.18, 0.02, 0.00, 0.01, 0.02, 0.05],
    [0.02, 0.08, 0.15, 0.08, 0.22, 0.05, 0.01, 0.00, 0.01, 0.02],
    [0.06, 0.09, 0.10, 0.02, 0.11, 0.08, 0.04, 0.03, 0.02, 0.08],
    [0.01, 0.04, 0.02, 0.02, 0.05, 0.03, 0.02, 0.08, 0.14, 0.15],
    [0.20, 0.15, 0.05, 0.25, 0.15, 0.12, 0.08, 0.02, 0.05, 0.10],
    [0.08, 0.10, 0.06, 0.06, 0.08, 0.07, 0.03, 0.01, 0.04, 0.05],
    [0.01, 0.02, 0.02, 0.01, 0.04, 0.04, 0.12, 0.10, 0.15, 0.06],
    [0.04, 0.05, 0.03, 0.08, 0.06, 0.05, 0.10, 0.15, 0.12, 0.04],
    [0.05, 0.06, 0.04, 0.10, 0.08, 0.06, 0.18, 0.12, 0.10, 0.12],
    [0.05, 0.04, 0.08, 0.05, 0.04, 0.04, 0.03, 0.04, 0.05, 0.02],
])

# Final demand, billions of dollars
d = np.array([45, 20, 60, 110, 280, 75, 90, 150, 130, 180], dtype=float)
