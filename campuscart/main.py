#!/usr/bin/env python3
"""
CampusCart - Command Line Platform
Connects students with campus vendors
"""

import argparse
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
VENDORS_FILE = os.path.join(DATA_DIR, "vendors.json")


def load_vendors():
    """Load vendors from JSON file"""
    if not os.path.exists(VENDORS_FILE):
        return []
    with open(VENDORS_FILE, "r") as f:
        return json.load(f)


def list_vendors():
    """Show all vendors"""
    vendors = load_vendors()
    if not vendors:
        print("No vendors found.")
        return

    print("\n=== Campus Vendors ===")
    for vendor in vendors:
        print(f"{vendor['id']}. {vendor['name']} - {vendor['category']}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="CampusCart - Order from campus vendors"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # vendors command
    vendors_parser = subparsers.add_parser("vendors", help="List all vendors")

    # products command (placeholder)
    products_parser = subparsers.add_parser("products", help="Browse products")

    # cart commands
    cart_parser = subparsers.add_parser("cart", help="Manage your cart")
    cart_sub = cart_parser.add_subparsers(dest="cart_action")
    cart_sub.add_parser("show", help="Show current cart")
    cart_add = cart_sub.add_parser("add", help="Add product to cart")
    cart_add.add_argument("product_id", type=int)

    args = parser.parse_args()

    if args.command == "vendors":
        list_vendors()
    elif args.command == "products":
        print("Products command - coming soon")
    elif args.command == "cart":
        if args.cart_action == "show":
            print("Your cart is empty (for now)")
        elif args.cart_action == "add":
            print(f"Added product {args.product_id} to cart (placeholder)")
        else:
            cart_parser.print_help()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
