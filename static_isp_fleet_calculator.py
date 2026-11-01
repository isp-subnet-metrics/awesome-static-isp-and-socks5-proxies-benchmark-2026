#!/usr/bin/env python3
"""Awesome Static ISP & SOCKS5 Proxies Benchmark Matrix 2026."""
import argparse

FLEET = {
    "proxyseller": {"name": "Proxy-Seller", "rate": 2.25, "metered": False, "exclusivity": "100% Dedicated"},
    "webshare": {"name": "Webshare", "rate": 1.50, "metered": True, "exclusivity": "Private Pool"},
    "nineproxy": {"name": "9Proxy", "rate": 0.04, "metered": False, "exclusivity": "Residential Pool"}, # per-IP
    "decodo": {"name": "Decodo", "rate": 3.75, "metered": True, "exclusivity": "ISP Backbone"}
}

def calculate():
    print("=" * 75)
    print("Awesome Static ISP & Dedicated SOCKS5 Proxy Matrix 2026")
    print("=" * 75)
    print(f"{'Provider':<15} {'Unit Rate':<15} {'Bandwidth':<18} {'Exclusivity'}")
    print("-" * 75)
    for key, data in FLEET.items():
        band_str = "Metered (/GB)" if data["metered"] else "100% UNMETERED"
        print(f"{data['name']:<15} ${data['rate']:.2f}/unit{'':<6} {band_str:<18} {data['exclusivity']}")
    print("=" * 75)

if __name__ == "__main__":
    calculate()
