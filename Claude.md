# CLAUDE.md — Trip Booking Calculator

## Project Overview
A Python library for calculating trip booking prices.
It handles base pricing, seasonal discounts, tax calculations,
and booking summaries for a travel booking platform.

## Coding Standards
- Use Python 3.10+
- Follow PEP 8 style guidelines
- Add a docstring to every function
- Use type hints for all function parameters and return values
- Use f-strings for all string formatting
- Raise ValueError with a clear message for invalid inputs
  (never silently return 0 or None for bad data)

## Testing Standards
- Use pytest (not unittest) for all tests
- Test file: tests/test_booking.py
- Run tests with: pytest tests/ -v
- Run with coverage: pytest tests/ -v --tb=short
- Every function needs:
    - At least one happy path test (normal valid input)
    - At least one edge case test (boundary values)
    - At least one error case test (invalid input raises ValueError)
- Use descriptive test names: test_calculate_total_price_returns_correct_value
- Use pytest.raises() to test exceptions
- Never use real network calls or file I/O in tests

## Project Structure
```
trip_booking/
├── CLAUDE.md              ← You are here
├── booking.py             ← Main booking logic (working code)
└── tests/
    └── test_booking.py    ← Test suite (to be created in this demo)
```

## Off-Limits
- Do NOT modify CLAUDE.md
- Do NOT modify booking.py until a failing test reveals a bug
