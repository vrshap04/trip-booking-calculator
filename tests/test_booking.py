import pytest

from booking import (
    calculate_total_price,
    apply_seasonal_discount,
    calculate_tax,
    get_price_category,
    format_booking_summary,
)


def test_calculate_total_price_returns_correct_value():
    result = calculate_total_price(base_price=100.0, nights=3, guests=2)
    assert result == 600.0


def test_apply_seasonal_discount_returns_correct_value():
    result = apply_seasonal_discount(price=1000.0, month=1)
    assert result == 850.0


def test_calculate_tax_returns_correct_value():
    result = calculate_tax(price=1000.0, country="france")
    assert result == 200.0


def test_get_price_category_returns_mid_range_for_1000():
    result = get_price_category(1000.0)
    assert result == "mid-range"


def test_format_booking_summary_returns_correct_string():
    result = format_booking_summary(
        trip_name="Bali Adventure",
        destination="Indonesia",
        total_price=1200.0,
        guests=4,
    )
    expected = (
        "Booking Summary\n"
        "  Trip:            Bali Adventure\n"
        "  Destination:     Indonesia\n"
        "  Total price:     $1200.00\n"
        "  Guests:          4\n"
        "  Price per person: $300.00"
    )
    assert result == expected
