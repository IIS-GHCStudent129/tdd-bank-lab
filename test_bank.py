import pytest

from bank import transfer_funds


@pytest.fixture
def source_account():
    return {"id": 1001, "balance": 250.00, "owner": "Alicia Nguyen"}


@pytest.fixture
def destination_account():
    return {"id": 1002, "balance": 75.50, "owner": "Marcus Chen"}


def test_transfer_funds_returns_transaction_details_for_valid_transfer(
    source_account, destination_account
):
    transaction = transfer_funds(source_account, destination_account, 75.50)

    assert transaction == {
        "from_id": 1001,
        "to_id": 1002,
        "amount": 75.50,
        "from_balance_after": 174.50,
        "to_balance_after": 151.00,
    }


def test_transfer_funds_decreases_source_balance_by_transfer_amount(
    source_account, destination_account
):
    transfer_funds(source_account, destination_account, 50.00)

    assert source_account["balance"] == 200.00


def test_transfer_funds_increases_destination_balance_by_transfer_amount(
    source_account, destination_account
):
    transfer_funds(source_account, destination_account, 50.00)

    assert destination_account["balance"] == 125.50


@pytest.mark.parametrize("amount", [0, -10.00])
def test_transfer_funds_rejects_non_positive_transfer_amount(
    source_account, destination_account, amount
):
    with pytest.raises(ValueError, match="greater than zero"):
        transfer_funds(source_account, destination_account, amount)


def test_transfer_funds_rejects_transfer_when_source_has_insufficient_funds(
    source_account, destination_account
):
    with pytest.raises(ValueError, match="sufficient funds"):
        transfer_funds(source_account, destination_account, 500.00)


def test_transfer_funds_requires_source_and_destination_accounts_to_be_different(
    source_account,
):
    with pytest.raises(ValueError, match="different"):
        transfer_funds(source_account, source_account, 10.00)
