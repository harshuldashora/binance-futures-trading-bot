from time import sleep

from binance.exceptions import (
    BinanceAPIException,
    BinanceRequestException
)


class OrderManager:

    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):

        try:

            self.logger.info(
                f"MARKET REQUEST | "
                f"symbol={symbol} "
                f"side={side} "
                f"quantity={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            self.logger.info(
                f"MARKET RESPONSE | {response}"
            )

            # Wait briefly for Binance to update status
            sleep(1)

            order_details = self.client.futures_get_order(
                symbol=symbol,
                orderId=response["orderId"]
            )

            self.logger.info(
                f"MARKET ORDER DETAILS | {order_details}"
            )

            return order_details

        except (
            BinanceAPIException,
            BinanceRequestException
        ) as e:

            self.logger.error(
                f"MARKET ERROR | {str(e)}"
            )

            raise

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        try:

            self.logger.info(
                f"LIMIT REQUEST | "
                f"symbol={symbol} "
                f"side={side} "
                f"quantity={quantity} "
                f"price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            self.logger.info(
                f"LIMIT RESPONSE | {response}"
            )

            sleep(1)

            order_details = self.client.futures_get_order(
                symbol=symbol,
                orderId=response["orderId"]
            )

            self.logger.info(
                f"LIMIT ORDER DETAILS | {order_details}"
            )

            return order_details

        except (
            BinanceAPIException,
            BinanceRequestException
        ) as e:

            self.logger.error(
                f"LIMIT ERROR | {str(e)}"
            )

            raise