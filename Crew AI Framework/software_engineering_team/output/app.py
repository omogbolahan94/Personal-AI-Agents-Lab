
import gradio as gr
# from gradio import Interface, inputs, outputs
from accounts import Account, get_share_price

account = Account(user_id='user123', initial_deposit=10000)

def deposit(amount):
    try:
        account.deposit_funds(float(amount))
        return f"Deposited: {amount}. Current balance: {account.balance}"
    except ValueError as e:
        return str(e)

def withdraw(amount):
    try:
        account.withdraw_funds(float(amount))
        return f"Withdrew: {amount}. Current balance: {account.balance}"
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        account.buy_shares(symbol, int(quantity))
        return f"Bought {quantity} shares of {symbol}. Current balance: {account.balance}"
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        account.sell_shares(symbol, int(quantity))
        return f"Sold {quantity} shares of {symbol}. Current balance: {account.balance}"
    except ValueError as e:
        return str(e)

def portfolio_value():
    return f"Portfolio Value: {account.get_portfolio_value()}"

def profit_or_loss():
    return f"Profit/Loss: {account.get_profit_or_loss()}"

def holdings():
    return f"Holdings: {account.get_holdings()}"

def transactions():
    return f"Transactions: {account.get_transactions()}"

# iface = gr.Interface(
#     fn=[
#         deposit,
#         withdraw,
#         buy_shares,
#         sell_shares,
#         portfolio_value,
#         profit_or_loss,
#         holdings,
#         transactions
#     ],
#     inputs=[
#         gr.Textbox(label="Deposit Amount"),
#         gr.Textbox(label="Withdraw Amount"),
#         gr.Textbox(label="Buy Symbol"),
#         gr.Textbox(label="Buy Quantity"),
#         gr.Textbox(label="Sell Symbol"),
#         gr.Textbox(label="Sell Quantity"),
#         gr.Button(value="Get Portfolio Value"),
#         gr.Button(value="Get Profit/Loss"),
#         gr.Button(value="Get Holdings"),
#         gr.Button(value="Get Transactions"),
#     ],
#     outputs=gr.Textbox(),
#     title="Account Management System",
#     description="Simple trading account manager"
# )

# Create individual Interfaces
deposit_ui = gr.Interface(fn=deposit, inputs=gr.Textbox(label="Deposit Amount"), outputs="text")
withdraw_ui = gr.Interface(fn=withdraw, inputs=gr.Textbox(label="Withdraw Amount"), outputs="text")
buy_ui = gr.Interface(fn=buy_shares, inputs=[gr.Textbox(label="Buy Symbol"), gr.Textbox(label="Buy Quantity")], outputs="text")
sell_ui = gr.Interface(fn=sell_shares, inputs=[gr.Textbox(label="Sell Symbol"), gr.Textbox(label="Sell Quantity")], outputs="text")
portfolio_ui = gr.Interface(fn=portfolio_value, inputs=None, outputs="text")
profit_ui = gr.Interface(fn=profit_or_loss, inputs=None, outputs="text")
holdings_ui = gr.Interface(fn=holdings, inputs=None, outputs="text")
transactions_ui = gr.Interface(fn=transactions, inputs=None, outputs="text")

# Combine into tabs
app = gr.TabbedInterface(
    [deposit_ui, withdraw_ui, buy_ui, sell_ui, portfolio_ui, profit_ui, holdings_ui, transactions_ui],
    ["Deposit", "Withdraw", "Buy Shares", "Sell Shares", "Portfolio Value", "Profit/Loss", "Holdings", "Transactions"]
)

app.launch()