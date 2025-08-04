#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .blue import Blueprint


def main():
    opening = "2025-08-11"

    payload = {
        "IME0411": "24",
    }

    for code in payload.keys():
        Blueprint(opening, code, payload[code]).save
        print(Blueprint(opening, code, payload[code]).bean)


if __name__ == "__main__":
    main()
