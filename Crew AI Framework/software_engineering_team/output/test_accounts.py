import unittest

class Account:
    def __init__(self, user_id: str, initial_deposit: float) -> None:
        self.user_id = user_id
        if initial_deposit < 0:
            raise ValueError('Initial deposit must be non-negative.')
        self.balance = initial_deposit
        self.portfolio = {}
        self.transactions = []
        self.initial_deposit = initial_deposit

    def deposit_funds(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')
        self.balance += amount
        self.transactions.append(f'Deposited: {amount}')

    def withdraw_funds(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError('Insufficient balance for withdrawal.')
        self.balance -= amount
        self.transactions.append(f'Withdrew: {amount}')

    def buy_shares(self, symbol: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError('Quantity must be positive.')
        price_per_share = get_share_price(symbol)
        total_cost = price_per_share * quantity
        if total_cost > self.balance:
            raise ValueError('Insufficient funds to buy shares.')
        self.balance -= total_cost
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        self.transactions.append(f'Bought {quantity} shares of {symbol}')

    def sell_shares(self, symbol: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError('Quantity must be positive.')
        if symbol not in self.portfolio or self.portfolio[symbol] < quantity:
            raise ValueError('Not enough shares to sell.')
        price_per_share = get_share_price(symbol)
        total_sale = price_per_share * quantity
        self.balance += total_sale
        self.portfolio[symbol] -= quantity
        if self.portfolio[symbol] == 0:
            del self.portfolio[symbol]
        self.transactions.append(f'Sold {quantity} shares of {symbol}')

    def get_portfolio_value(self) -> float:
        total_value = 0.0
        for symbol, quantity in self.portfolio.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def get_profit_or_loss(self) -> float:
        return (self.balance + self.get_portfolio_value()) - self.initial_deposit

    def get_holdings(self) -> dict:
        return self.portfolio

    def get_transactions(self) -> list:
        return self.transactions


def get_share_price(symbol):
    prices = {'AAPL': 150, 'TSLA': 700, 'GOOGL': 2800}
    return prices.get(symbol, 0)

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(user_id='user123', initial_deposit=10000)

    def test_initial_deposit(self):
        self.assertEqual(self.account.balance, 10000)

    def test_deposit_funds(self):
        self.account.deposit_funds(5000)
        self.assertEqual(self.account.balance, 15000)
        with self.assertRaises(ValueError):
            self.account.deposit_funds(-100)

    def test_withdraw_funds(self):
        self.account.withdraw_funds(2000)
        self.assertEqual(self.account.balance, 8000)
        with self.assertRaises(ValueError):
            self.account.withdraw_funds(10000)

    def test_buy_shares(self):
        self.account.buy_shares('AAPL', 10)
        self.assertEqual(self.account.portfolio['AAPL'], 10)
        self.assertEqual(self.account.balance, 8500)
        with self.assertRaises(ValueError):
            self.account.buy_shares('TSLA', 15)

    def test_sell_shares(self):
        self.account.buy_shares('AAPL', 10)
        self.account.sell_shares('AAPL', 5)
        self.assertEqual(self.account.portfolio['AAPL'], 5)
        self.assertEqual(self.account.balance, 9250)
        with self.assertRaises(ValueError):
            self.account.sell_shares('AAPL', 10)

    def test_get_portfolio_value(self):
        self.account.buy_shares('AAPL', 10)
        self.assertEqual(self.account.get_portfolio_value(), 1500)

    def test_get_profit_or_loss(self):
        self.assertEqual(self.account.get_profit_or_loss(), 0)
        self.account.withdraw_funds(2000)
        self.assertEqual(self.account.get_profit_or_loss(), -2000)

    def test_get_holdings(self):
        self.account.buy_shares('AAPL', 10)
        self.assertEqual(self.account.get_holdings(), {'AAPL': 10})

    def test_get_transactions(self):
        self.account.deposit_funds(5000)
        self.account.withdraw_funds(2000)
        self.assertEqual(self.account.get_transactions(), [
            'Deposited: 5000',
            'Withdrew: 2000'
        ])

if __name__ == '__main__':
    unittest.main()