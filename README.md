# AlphaVantage API + GraphQL /w 🍓

## Special Thanks to the [`alpha-vantage` Python library](https://pypi.org/project/alpha-vantage/)

## Setup

1. Install Requirements /w `pipenv` or `requirements.txt`
2. Start the `uvicorn` server with `uvicorn app:app --reload`
3. Navigate to [`http://localhost:8000/graphql`](http://localhost:8000/graphql)

## Available APIs (currently)

### Series

- `TimeSeries`
- `TimeSeriesAdjusted`

### Fundemental Information

- `BalanceSheet`
- - Annual & Quarterly
- `CashFlow`
- - Annual & Quarterly
- `IncomeStatement`
- - Annual & Quarterly

**_with more coming soon!_**
