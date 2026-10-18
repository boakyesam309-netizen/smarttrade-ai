# SmartTrade AI — Android Website / PWA Starter

This package is a mobile-friendly website that can be added to an Android home screen after it is hosted over HTTPS.

## Current status
- Mobile dashboard, PWA manifest, icons, and service worker are included.
- The dashboard does not connect to Exness, stream live BTC/USD data, or place trades.
- The toggle is simulated and trading is deliberately disabled.
- A compatible always-on MT5 trading engine and secure server still need to be implemented and tested.

## Hosting and installing on Android
This Flask website must run on a server; opening the ZIP directly will not run it. Once hosted on an HTTPS-enabled service, open the website in Chrome and choose the menu → Add to Home screen or Install app. Browser options vary.

## MT5 integration needed next
A separate trading service must run in a compatible Windows environment with the official MetaTrader 5 Python integration and a logged-in MT5 terminal. It must use demo credentials first, verify the exact Exness BTCUSD symbol and contract specifications, and implement backtested entry/exit rules, server-side position sizing and loss limits, duplicate-order protection, audit logs, authentication, HTTPS, and encrypted secret handling.

Do not share MT5 passwords in chat or hard-code them in source files. No trading strategy can guarantee profits.
