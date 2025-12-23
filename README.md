# cta-trend-execution-system# 

## Overview
This project implements a simple CTA trend-following strategy for futures markets.
It focuses on realistic execution assumptions including slippage, transaction cost,
and risk control.

## Strategy Logic
- Trend signal based on moving average breakout
- Volatility-adjusted position sizing
- Risk control with maximum drawdown and stop-loss

## Execution Assumptions
- Market order execution
- Fixed slippage model
- Commission included

## Backtest Scope
- Futures contracts: multiple commodities
- Backtest period: 3+ years

## Limitations
- Not suitable for high-frequency trading
- Performance sensitive to trend regime

cta-trend-execution-system/
├── data/
├── strategy.py
├── backtest.py
├── execution.py
└── README.md
