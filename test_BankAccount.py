import pytest
from BankDetails import BankAccount

@pytest.fixture
def account():
    return BankAccount(100)

@pytest.mark.parametrize("deposit_amount, expected_balance", [
    (50, 150),
    (200, 300),
    (0, 100),
    (-50, 100)
])
def test_deposit(account, deposit_amount, expected_balance):
    if deposit_amount <= 0:
        with pytest.raises(ValueError):
            account.deposit(deposit_amount)
    else:
        account.deposit(deposit_amount)
        assert account.get_balance() == expected_balance

@pytest.mark.parametrize("withdraw_amount, expected_balance", [
    (50, 50),
    (100, 0),
    (200, 100)
])
def test_withdraw(account, withdraw_amount, expected_balance):
    if withdraw_amount > account.get_balance():
        with pytest.raises(ValueError):
            account.withdraw(withdraw_amount)
    else:
        account.withdraw(withdraw_amount)
        assert account.get_balance() == expected_balance
