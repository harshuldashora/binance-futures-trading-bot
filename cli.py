import argparse

from bot.client import get_client
from bot.orders import OrderManager

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.logging_config import (
    setup_logger
)


def print_order_summary(
    symbol,
    side,
    order_type,
    quantity,
    price=None
):

    print("\n===== ORDER REQUEST =====")

    print(f"Symbol      : {symbol}")
    print(f"Side        : {side}")
    print(f"Order Type  : {order_type}")
    print(f"Quantity    : {quantity}")

    if price:
        print(f"Price       : {price}")


def print_response(response):

    print("\n===== ORDER RESPONSE =====")

    print(
        f"Order ID    : "
        f"{response.get('orderId')}"
    )

    print(
        f"Status      : "
        f"{response.get('status')}"
    )

    print(
        f"ExecutedQty : "
        f"{response.get('executedQty', 'N/A')}"
    )

    avg_price = response.get(
        "avgPrice",
        response.get(
            "price",
            "N/A"
        )
    )

    print(
        f"Avg Price   : "
        f"{avg_price}"
    )


def main():

    parser = argparse.ArgumentParser(
        description=
        "Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        help="Required for LIMIT order"
    )

    args = parser.parse_args()

    logger = setup_logger()

    try:

        symbol = validate_symbol(
            args.symbol
        )

        side = validate_side(
            args.side
        )

        order_type = validate_order_type(
            args.type
        )

        quantity = validate_quantity(
            args.quantity
        )

        client = get_client()

        manager = OrderManager(
            client,
            logger
        )

        if order_type == "MARKET":

            print_order_summary(
                symbol,
                side,
                order_type,
                quantity
            )

            response = (
                manager.place_market_order(
                    symbol,
                    side,
                    quantity
                )
            )

        else:

            if args.price is None:
                raise ValueError(
                    "Price is required "
                    "for LIMIT orders"
                )

            price = validate_price(
                args.price
            )

            print_order_summary(
                symbol,
                side,
                order_type,
                quantity,
                price
            )

            response = (
                manager.place_limit_order(
                    symbol,
                    side,
                    quantity,
                    price
                )
            )

        print_response(response)

        print(
            "\nSUCCESS: "
            "Order submitted successfully."
        )

    except Exception as e:

        logger.error(
            f"APPLICATION ERROR | {str(e)}"
        )

        print(
            f"\nFAILED: {str(e)}"
        )


if __name__ == "__main__":
    main()