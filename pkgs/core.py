#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pkgs.blue import Blueprint


def main():
    opening = "2025-03-07"

    payload = {
        "IME0010": "46",
        "IME0379": "46",
        "IME0416": "35",
    }

    for code in payload.keys():
        Blueprint(opening, code, payload[code]).save


if __name__ == "__main__":
    main()
