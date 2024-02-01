# AlphaVantage API + GraphQL /w 🍓

## Special Thanks to the [`alpha-vantage` Python library](https://pypi.org/project/alpha-vantage/)

## Setup

## Now with `Dockerfile`!

> For a quick and simple setup, just spin up the Docket image! Your instance will be available at http://localhost/graphql - Make sure to provide your API Key as `AV_KEY` environment variable

1. Install Requirements /w `pipenv` or `requirements.txt`
2. Create / Edit `.env` file and add your AlphaVantage API Key as an environment variable with the key `AV_KEY`
3. Start the `uvicorn` server with `uvicorn app:app --reload`
4. Navigate to [`http://localhost:8000/graphql`](http://localhost:8000/graphql)

## Available APIs (currently)

- `getFundementalData`
- - `getBalanceSheetAnnual(symbol: String!)`
- - `getBalanceSheetQuarterly(symbol: String!)`
- - `getCompanyOverview(symbol: String!)`
- - `getCashFlowAnnual(symbol: String!)`
- - `getCashFlowQuarterly(symbol: String!)`
- - `getIncomeStatementAnnual(symbol: String!)`
- - `getIncomeStatementQuarterly(symbol: String!)`
- `getCrypto`
- - `exchangeRate(fromCurrency: String!, toCurrency: String!)`
- - `intraday(symbol: String!, market: String! = "USD", interval: String! = "5min")`
- `getTechnicalAverages`
- - Parameters for each
- - - symbol: `String`
- - - interval: `String` = "weekly"
- - - timePeriod: `Int` = 60
- - - seriesType: `String` = "open"
- - `sma(...)`
- - `ema(...)`
- - `wma(...)`
- - `dema(...)`
- - `tema(...)`
- `getTimeSeries` & `getTimeSeriesAdjusted`
- - `intraday(symbol: String!, interval: String! = "15min", outputsize: String! = "compact")`
- - `daily(symbol: String!, outputsize: String! = "compact")`
- - `monthly(symbol: String!)`
- - `weekly(symbol: String!)`

## Example

```sql
query {
  getTechnicalAverages {
    sma(symbol:"AAPL", interval:"weekly") {
      Analysis {
        date
        average
      }
    }
    ema(symbol:"AAPL", interval:"weekly") {
      Analysis {
        date
        average
      }
    }

  }
}
```

```sql
query {
  getTimeSeries {
    monthly(symbol:"AAPL") {
      open
      close
    }
  }
}
```
