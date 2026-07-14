def transfer_funds(from_account, to_account, amount):
    """
    Transfer amount from from_account to to_account.

    Each account is a dict: {"id": int, "balance": float, "owner": str}

    Returns a transaction dict on success.
    Raises ValueError for invalid inputs.
    """
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        raise ValueError("Transfer amount must be a numeric value")

    if amount <= 0:
        raise ValueError("Transfer amount must be greater than zero")

    if from_account is to_account:
        raise ValueError("Source and destination accounts must be different")

    if from_account.get("balance", 0) < amount:
        raise ValueError("Source account must have sufficient funds")

    from_account["balance"] -= amount
    to_account["balance"] += amount

    return {
        "from_id": from_account["id"],
        "to_id": to_account["id"],
        "amount": amount,
        "from_balance_after": from_account["balance"],
        "to_balance_after": to_account["balance"],
    }