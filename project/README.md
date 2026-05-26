# Stock Portfolio Tracker

A full-stack stock portfolio tracking application built with Django and PostgreSQL. Track investments, log trades, monitor real-time P&L, and visualize portfolio performance over time.

## Features

- **Real-Time P&L**: Live price data from Yahoo Finance API calculates profit/loss per transaction
- **Portfolio Chart**: Historical portfolio value over time aggregated across all holdings using pandas
- **Transaction Logging**: Log buy/sell transactions with date, quantity, and price per share
- **Watchlist**: Track stocks of interest with live price updates
- **Stock Browser**: Search and filter stocks by ticker, company name, or sector
- **User Authentication**: Register, login, and manage your own portfolio

## Data Model

User (Django Auth) → Profile (OneToOne) → Transaction (ForeignKey) → Stock

Profile → Watchlist (ForeignKey) → Stock

## Tech Stack

- **Backend**: Python, Django, PostgreSQL
- **Data**: Yahoo Finance API (yfinance), pandas
- **Frontend**: Django templates, Chart.js
- **Auth**: Django built-in authentication

## Key Views

| URL | Description |
|-----|-------------|
| `/project/` | Landing page with market overview |
| `/project/stocks/` | Searchable stock list with sector filter |
| `/project/stocks/<id>/` | Stock detail with 6-month price chart |
| `/project/profile/<id>/` | Portfolio summary, transactions, watchlist |
| `/project/transactions/add/` | Log a new transaction |

## Author

**Shrey Jain** - Boston University CS '26 - [GitHub](https://github.com/shreyj03)
