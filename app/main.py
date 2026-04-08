from decimal import Decimal
import json


def calculate_profit() -> dict:
    with open("app/trades.json", "r") as f:
        trades = json.load(f)

    money = Decimal("0")
    coins = Decimal("0")
    for trade in trades:
        if trade["sold"] is None:
            coins += Decimal(trade["bought"])
            money -= (Decimal(trade["matecoin_price"])
                      * Decimal(trade["bought"]))

        elif trade["bought"] is None:
            coins -= Decimal(trade["sold"])
            money += Decimal(trade["matecoin_price"]) * Decimal(trade["sold"])

    result = {
        "earned_money": str(money),
        "matecoin_account": str(coins)
    }

    with open("app/profit.json", "w") as f:
        json.dump(result, f)
    return result
