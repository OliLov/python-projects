"""Curreny converter."""

import argparse
from typing import Optional

import requests


def fetch_usd_exchange_rate(
    api_url: str, target_currency: str
) -> Optional[float]:
    """Fetch the USD exchange rate for a target currency.

    :param api_url: API URL including the API key.
    :param target_currency: The target currency to fetch the exchange rate for.
    :return: The exchange rate for the target currency in USD or `None`.
    """
    try:
        response = requests.get(api_url, timeout=120)
        response.raise_for_status()
        rates = response.json().get("rates", {})
        return rates.get(target_currency, None)
    except requests.RequestException as exception:
        print(f"Failed to fetch exchange rates: {exception}")
        return None


def convert_currency(
    api_url: str, amount: float, target_currency: str
) -> Optional[float]:
    """Convert the amount using the provided exchange rate in USD.

    :param api_url: API URL including the API key.
    :param amount: The amount to convert.
    :param target_currency: The target currency to fetch the exchange rate for.
    :return: The amount in the target curreny.
    """
    rate = fetch_usd_exchange_rate(api_url, target_currency)
    if rate is not None:
        return amount * rate
    return None


def main(api_url: str) -> None:
    """Main function for the currency converter.

    :param api_url: API URL including the API key.
    """
    while True:
        target_currency = input(
            "Convert USD to currency (Type 'exit' to quit): "
        )
        if target_currency.lower() == "exit":
            break

        try:
            amount = float(input("Amount in USD: "))
            target_amount = convert_currency(api_url, amount, target_currency)
            if target_amount is not None:
                print(f"{amount} USD is {target_amount} {target_currency}.")
            else:
                print("Failed to convert currency. Please check your inputs.")
        except ValueError:
            print("Please enter a valid amount.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Currency Converter")

    API_URL_HELP = "URL to the currency conversion API including the API key"
    parser.add_argument("api_url", type=str, help=API_URL_HELP)

    args = parser.parse_args()
    main(args.api_url)
