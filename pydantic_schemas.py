from pydantic import BaseModel, Field


class IncomeStatementSchema(BaseModel):
    """
    Income Statement for AlphaVantage API\n\n
    """

    fiscal_date_ending: str = Field(
        title="Fiscal Date Ending", validation_alias="fiscalDateEnding"
    )
    reported_currency: str = Field(
        title="Reported Currency", validation_alias="reportedCurrency"
    )
    gross_profit: str = Field(title="Gross Profit", validation_alias="grossProfit")
    total_revenue: str = Field(title="Total Revenue", validation_alias="totalRevenue")
    cost_of_revenue: str = Field(
        title="Cost of Revenue", validation_alias="costOfRevenue"
    )
    cost_of_goods_services_sold: str = Field(
        title="Cost of Goods Sold", validation_alias="costofGoodsAndServicesSold"
    )
    operating_income: str = Field(
        title="Operating Income", validation_alias="operatingIncome"
    )
    selling_general_and_administrative: str = Field(
        title="Selling, General and Administrative",
        validation_alias="sellingGeneralAndAdministrative",
    )
    research_and_development: str = Field(
        title="Research and Development", validation_alias="researchAndDevelopment"
    )
    operating_expenses: str = Field(
        title="Operating Expenses", validation_alias="operatingExpenses"
    )
    investment_income_net: str = Field(
        title="Investment Income Net", validation_alias="investmentIncomeNet"
    )
    net_interest_income: str = Field(
        title="Net Interest Income", validation_alias="netInterestIncome"
    )
    interest_income: str = Field(
        title="Interest Income", validation_alias="interestIncome"
    )
    interest_expense: str = Field(
        title="Interest Expenses", validation_alias="interestExpense"
    )
    non_interest_income: str = Field(
        title="Non Interest Income", validation_alias="nonInterestIncome"
    )
    other_non_operating_income: str = Field(
        title="Other Non Operating Income", validation_alias="otherNonOperatingIncome"
    )
    depreciation: str = Field(title="Depreciation", validation_alias="depreciation")
    depreciation_and_amortization: str = Field(
        title="Depreciation and Amortization",
        validation_alias="depreciationAndAmortization",
    )
    income_before_tax: str = Field(
        title="Income Before Tax", validation_alias="incomeBeforeTax"
    )
    income_tax_expense: str = Field(
        title="Income Tax Expense", validation_alias="incomeTaxExpense"
    )
    interest_and_debt_expense: str = Field(
        title="Interest and Debt Expense", validation_alias="interestAndDebtExpense"
    )
    net_income_from_continuing_operations: str = Field(
        title="Net Income from Continuing Operations",
        validation_alias="netIncomeFromContinuingOperations",
    )
    comprehensive_income_net_of_tax: str = Field(
        title="Comprehensive Income Net of Tax",
        validation_alias="comprehensiveIncomeNetOfTax",
    )
    ebit: str = Field(title="EBIT", validation_alias="ebit")
    ebitda: str = Field(title="EBITDA", validation_alias="ebitda")
    net_income: str = Field(title="Net Income", validation_alias="netIncome")


class GlobalQuoteSchema(BaseModel):
    symbol: str = Field(title="Symbol", validation_alias="01. symbol")
    open: str = Field(title="Open", validation_alias="02. open")
    high: str = Field(title="High", validation_alias="03. high")
    low: str = Field(title="Low", validation_alias="04. low")
    price: str = Field(title="Price", validation_alias="05. price")
    volume: str = Field(title="Volume", validation_alias="06. volume")
    latest_trading_day: str = Field(
        title="Latest Trading Day", validation_alias="07. latest trading day"
    )
    previous_close: str = Field(
        title="Previous Close", validation_alias="08. previous close"
    )
    change: str = Field(title="Change", validation_alias="09. change")
    change_percent: str = Field(
        title="Change Percent", validation_alias="10. change percent"
    )


class CashFlowSchema(BaseModel):
    """The above code is defining a class with multiple fields representing financial data. Each field
    has a title and a validation alias. The fields can store values of type float or None. The class
    is used to store and manipulate financial data for different fiscal dates."""

    fiscal_date_ending: str = Field(
        title="Fiscal Date Ending", validation_alias="fiscalDateEnding"
    )
    reported_currency: str = Field(
        title="Reported Currency", validation_alias="reportedCurrency"
    )
    operating_cash_flow: str = Field(
        title="Operating Cash Flow", validation_alias="operatingCashflow"
    )
    payments_for_operating_activities: str = Field(
        title="Payments for Operating Activities",
        validation_alias="paymentsForOperatingActivities",
    )
    proceeds_from_operating_activities: str = Field(
        title="Proceeds from Operating Activities",
        validation_alias="proceedsFromOperatingActivities",
    )
    change_in_operating_liabilities: str = Field(
        title="Change in Operating Liabilities",
        validation_alias="changeInOperatingLiabilities",
    )
    change_in_operating_assets: str = Field(
        title="Change in Operating Assets", validation_alias="changeInOperatingAssets"
    )
    depreciation_depletion_and_amortization: str = Field(
        title="Depreciation, Depletion and Amortization",
        validation_alias="depreciationDepletionAndAmortization",
    )
    capital_expenditures: str = Field(
        title="Capital Expenditures", validation_alias="capitalExpenditures"
    )
    change_in_receivables: str = Field(
        title="Change in Receivables", validation_alias="changeInReceivables"
    )
    change_in_inventory: str = Field(
        title="Change in Inventory", validation_alias="changeInInventory"
    )
    profit_loss: str = Field(title="Profit/Loss", validation_alias="profitLoss")
    cashflow_from_investment: str = Field(
        title="Cashflow from Investment", validation_alias="cashflowFromInvestment"
    )
    cashflow_from_financing: str = Field(
        title="Cashflow from Financing", validation_alias="cashflowFromFinancing"
    )
    proceeds_from_repayments_of_short_term_debt: str = Field(
        title="Proceeds from Repayments of Short Term Debt",
        validation_alias="proceedsFromRepaymentsOfShortTermDebt",
    )
    payments_for_repurchase_of_common_stock: str = Field(
        title="Payments for Repurchase of Common Stock",
        validation_alias="paymentsForRepurchaseOfCommonStock",
    )
    payments_for_repurchase_of_equity: str = Field(
        title="Payments for Repurchase of Equity",
        validation_alias="paymentsForRepurchaseOfEquity",
    )
    payments_for_repurchase_of_preferred_stock: str = Field(
        title="Payments for Repurchase of Preferred Stock",
        validation_alias="paymentsForRepurchaseOfPreferredStock",
    )
    dividend_payout: str = Field(
        title="Dividend Payout", validation_alias="dividendPayout"
    )
    dividend_payout_common_stock: str = Field(
        title="Dividend Payout Common Stock",
        validation_alias="dividendPayoutCommonStock",
    )
    dividend_payout_preferred_stock: str = Field(
        title="Dividend Payout Preferred Stock",
        validation_alias="dividendPayoutPreferredStock",
    )
    proceeds_from_issuance_of_common_stock: str = Field(
        title="Proceeds from Issuance of Common Stock",
        validation_alias="proceedsFromIssuanceOfCommonStock",
    )
    proceeds_from_issuance_of_long_term_debt_and_capital_securities_net: str = Field(
        title="Proceeds from Issuance of Long Term Debt and Capital Securities, Net",
        validation_alias="proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet",
    )
    proceeds_from_issuance_of_preferred_stock: str = Field(
        title="Proceeds from Issuance of Preferred Stock",
        validation_alias="proceedsFromIssuanceOfPreferredStock",
    )
    proceeds_from_repurchase_of_equity: str = Field(
        title="Proceeds from Repayments of Long Term Debt",
        validation_alias="proceedsFromRepurchaseOfEquity",
    )
    proceeds_from_sale_of_treasury_stock: str = Field(
        title="Proceeds from Sale of Treasury Stock",
        validation_alias="proceedsFromSaleOfTreasuryStock",
    )
    change_in_cash_and_cash_equivalents: str = Field(
        title="Change in Cash and Cash Equivalents",
        validation_alias="changeInCashAndCashEquivalents",
    )
    change_in_exchange_rate: str = Field(
        title="Change in Exchange Rate", validation_alias="changeInExchangeRate"
    )
    net_income: str = Field(title="Net Income", validation_alias="netIncome")


class BalanceSheetSchema(BaseModel):
    """
    Balance Sheet for AlphaVantage API\n\n
    """

    fiscal_date_ending: str = Field(
        title="Fiscal Date Ending", validation_alias="fiscalDateEnding"
    )
    reported_currency: str = Field(
        title="Reported Currency", validation_alias="reportedCurrency"
    )
    total_assets: str = Field(title="Total Assets", validation_alias="totalAssets")
    total_current_assets: str = Field(
        title="Total Current Assets", validation_alias="totalCurrentAssets"
    )
    cash_and_cash_equivalents_at_carrying_value: str = Field(
        title="Cash and Cash Equivalents at Carrying Value",
        validation_alias="cashAndCashEquivalentsAtCarryingValue",
    )
    cash_and_short_term_investments: str = Field(
        title="Cash and Short Term Investments",
        validation_alias="cashAndShortTermInvestments",
    )
    inventory: str = Field(title="Inventory", validation_alias="inventory")
    current_net_receivables: str = Field(
        title="Current Net Receivables", validation_alias="currentNetReceivables"
    )
    total_non_current_assets: str = Field(
        title="Total Non Current Assets", validation_alias="totalNonCurrentAssets"
    )
    property_plant_equipment: str = Field(
        title="Property Plant Equipment", validation_alias="propertyPlantEquipment"
    )
    accumulated_depreciation_amortization_ppe: str = Field(
        title="Accumulated Depreciation Amortization PPE",
        validation_alias="accumulatedDepreciationAmortizationPPE",
    )
    intangible_assets: str = Field(
        title="Intangible Assets", validation_alias="intangibleAssets"
    )
    intangible_assets_excluding_goodwill: str = Field(
        title="Intangible Assets Excluding Goodwill",
        validation_alias="intangibleAssetsExcludingGoodwill",
    )
    goodwill: str = Field(title="Goodwill", validation_alias="goodwill")
    investments: str = Field(title="Investments", validation_alias="investments")
    long_term_investments: str = Field(
        title="Long Term Investments", validation_alias="longTermInvestments"
    )
    short_term_investments: str = Field(
        title="Short Term Investments", validation_alias="shortTermInvestments"
    )
    other_current_assets: str = Field(
        title="Other Current Assets", validation_alias="otherCurrentAssets"
    )
    other_non_current_assets: str = Field(
        title="Other Non Current Assets", validation_alias="otherNonCurrentAssets"
    )
    total_liabilities: str = Field(
        title="Total Liabilities", validation_alias="totalLiabilities"
    )
    total_current_liabilities: str = Field(
        title="Total Current Liabilities", validation_alias="totalCurrentLiabilities"
    )
    current_accounts_payable: str = Field(
        title="Current Accounts Payable", validation_alias="currentAccountsPayable"
    )
    deferred_revenue: str = Field(
        title="Deferred Revenue", validation_alias="deferredRevenue"
    )
    current_debt: str = Field(title="Current Debt", validation_alias="currentDebt")
    short_term_debt: str = Field(
        title="Short Term Debt", validation_alias="shortTermDebt"
    )
    total_non_current_liabilities: str = Field(
        title="Total Non Current Liabilities",
        validation_alias="totalNonCurrentLiabilities",
    )
    capital_lease_obligations: str = Field(
        title="Capital Lease Obligations", validation_alias="capitalLeaseObligations"
    )
    long_term_debt: str = Field(title="Long Term Debt", validation_alias="longTermDebt")
    current_long_term_debt: str = Field(
        title="Current Long Term Debt", validation_alias="currentLongTermDebt"
    )
    long_term_debt_noncurrent: str = Field(
        title="Long Term Debt Noncurrent", validation_alias="longTermDebtNoncurrent"
    )
    short_long_term_debt_total: str = Field(
        title="Short Long Term Debt Total", validation_alias="shortLongTermDebtTotal"
    )
    other_current_liabilities: str = Field(
        title="Other Current Liabilities", validation_alias="otherCurrentLiabilities"
    )
    other_non_current_liabilities: str = Field(
        title="Other Non Current Liabilities",
        validation_alias="otherNonCurrentLiabilities",
    )
    total_shareholder_equity: str = Field(
        title="Total Shareholder Equity", validation_alias="totalShareholderEquity"
    )
    treasury_stock: str = Field(
        title="Treasury Stock", validation_alias="treasuryStock"
    )
    retained_earnings: str = Field(
        title="Retained Earnings", validation_alias="retainedEarnings"
    )
    common_stock: str = Field(title="Common Stock", validation_alias="commonStock")
    common_stock_shares_outstanding: str = Field(
        title="Common Stock Shares Outstanding",
        validation_alias="commonStockSharesOutstanding",
    )


class OverviewSchema(BaseModel):
    """
    Overview for AlphaVantage API\n\n
    """

    symbol: str = Field(title="Symbol", validation_alias="Symbol")
    asset_type: str = Field(title="Asset Type", validation_alias="AssetType")
    name: str = Field(title="Name", validation_alias="Name")
    description: str = Field(title="Description", validation_alias="Description")
    cik: str = Field(title="CIK", validation_alias="CIK")
    exchange: str = Field(title="Exchange", validation_alias="Exchange")
    currency: str = Field(title="Currency", validation_alias="Currency")
    country: str = Field(title="Country", validation_alias="Country")
    sector: str = Field(title="Sector", validation_alias="Sector")
    industry: str = Field(title="Industry", validation_alias="Industry")
    address: str = Field(title="Address", validation_alias="Address")
    fiscal_year_end: str = Field(
        title="Fiscal Year End", validation_alias="FiscalYearEnd"
    )
    latest_quarter: str = Field(
        title="Latest Quarter", validation_alias="LatestQuarter"
    )
    market_capitalization: str = Field(
        title="Market Capitalization", validation_alias="MarketCapitalization"
    )
    ebitda: str = Field(title="EBITDA", validation_alias="EBITDA")
    pe_ratio: str = Field(title="PE Ratio", validation_alias="PERatio")
    peg_ratio: str = Field(title="PEG Ratio", validation_alias="PEGRatio")
    book_value: str = Field(title="Book Value", validation_alias="BookValue")
    dividend_per_share: str = Field(
        title="Dividend Per Share", validation_alias="DividendPerShare"
    )
    dividend_yield: str = Field(
        title="Dividend Yield", validation_alias="DividendYield"
    )
    eps: str = Field(title="EPS", validation_alias="EPS")
    revenue_per_share_ttm: str = Field(
        title="Revenue Per Share TTM", validation_alias="RevenuePerShareTTM"
    )
    profit_margin: str = Field(title="Profit Margin", validation_alias="ProfitMargin")
    operating_margin_ttm: str = Field(
        title="Operating Margin TTM", validation_alias="OperatingMarginTTM"
    )
    return_on_assets_ttm: str = Field(
        title="Return on Assets TTM", validation_alias="ReturnOnAssetsTTM"
    )
    return_on_equity_ttm: str = Field(
        title="Return on equity TTM", validation_alias="ReturnOnEquityTTM"
    )
    revenue_ttm: str = Field(title="Revenue TTM", validation_alias="RevenueTTM")
    gross_profit_ttm: str = Field(
        title="Gross Profit TTM", validation_alias="GrossProfitTTM"
    )
    diluted_eps_ttm: str = Field(
        title="Diluted EPS TTM", validation_alias="DilutedEPSTTM"
    )
    quarterly_earnings_growth_yoy: str = Field(
        title="Quarterly Earnings Growth YOY",
        validation_alias="QuarterlyEarningsGrowthYOY",
    )
    quarterly_revenue_growth_yoy: str = Field(
        title="Quarterly Revenue Growth YOY",
        validation_alias="QuarterlyRevenueGrowthYOY",
    )
    analyst_target_price: str = Field(
        title="Analyst Target Price", validation_alias="AnalystTargetPrice"
    )
    trailing_pe: str = Field(title="Trailing PE", validation_alias="TrailingPE")
    forward_pe: str = Field(title="Forward PE", validation_alias="ForwardPE")
    price_to_sales_ratio_ttm: str = Field(
        title="Price to Sales Ratio TTM", validation_alias="PriceToSalesRatioTTM"
    )
    price_to_book_ratio: str = Field(
        title="Price to Book Ratio", validation_alias="PriceToBookRatio"
    )
    ev_to_revenue: str = Field(title="EV to Revenue", validation_alias="EVToRevenue")
    ev_to_ebitda: str = Field(title="EV to EBITDA", validation_alias="EVToEBITDA")
    beta: str = Field(title="Beta", validation_alias="Beta")
    week_high_52: str = Field(title="52 Week High", validation_alias="52WeekHigh")
    week_low_52: str = Field(title="52 Week Low", validation_alias="52WeekLow")
    day_moving_average_50: str = Field(
        title="50 Day Moving Average", validation_alias="50DayMovingAverage"
    )
    day_moving_average_200: str = Field(
        title="200 Day Moving Average", validation_alias="200DayMovingAverage"
    )
    shares_outstanding: str = Field(
        title="Shares Outstanding", validation_alias="SharesOutstanding"
    )
    dividend_date: str = Field(title="Dividend Date", validation_alias="DividendDate")
    ex_dividend_date: str = Field(
        title="Ex Dividend Date", validation_alias="ExDividendDate"
    )


class CryptoMetadataSchema(BaseModel):
    """The CryptoMetadataSchema class defines the schema of the response returned by the `metadata` method."""

    information: str = Field(
        ...,
        title="The information of the cryptocurrency.",
        validation_alias="1. Information",
    )
    digital_currency_code: str = Field(
        ...,
        title="The code of the cryptocurrency.",
        validation_alias="2. Digital Currency Code",
    )
    digital_currency_name: str = Field(
        ...,
        title="The name of the cryptocurrency.",
        validation_alias="3. Digital Currency Name",
    )
    market_code: str = Field(
        ...,
        title="The code of the market.",
        validation_alias="4. Market Code",
    )
    market_name: str = Field(
        ...,
        title="The name of the market.",
        validation_alias="5. Market Name",
    )
    last_refreshed: str = Field(
        ...,
        title="The date and time the metadata was last refreshed.",
        validation_alias="6. Last Refreshed",
    )
    interval: str = Field(
        ...,
        title="The interval of the metadata.",
        validation_alias="7. Interval",
    )
    output_size: str = Field(
        ..., title="The output size of the metadata.", validation_alias="8. Output Size"
    )
    time_zone: str = Field(
        ..., title="The timezone of the metadata.", validation_alias="9. Time Zone"
    )


class CurrencyExchangeRateSchema(BaseModel):
    """The CurrencyExchangeRateSchema class defines the schema of the response returned by the
    `exchange_rate` method."""

    from_currency_code: str = Field(
        ...,
        title="The code of the currency to convert from.",
        validation_alias="1. From_Currency Code",
    )
    from_currency_name: str = Field(
        ...,
        title="The name of the currency to convert from.",
        validation_alias="2. From_Currency Name",
    )
    to_currency_code: str = Field(
        ...,
        title="The code of the currency to convert to.",
        validation_alias="3. To_Currency Code",
    )
    to_currency_name: str = Field(
        ...,
        title="The name of the currency to convert to.",
        validation_alias="4. To_Currency Name",
    )
    exchange_rate: str = Field(
        ...,
        title="The exchange rate between the two currencies.",
        validation_alias="5. Exchange Rate",
    )
    last_refreshed: str = Field(
        ...,
        title="The date and time the exchange rate was last refreshed.",
        validation_alias="6. Last Refreshed",
    )
    timezone: str = Field(
        ..., title="The timezone of the exchange rate.", validation_alias="7. Time Zone"
    )
    bid_price: str = Field(
        ...,
        title="The bid price of the exchange rate.",
        validation_alias="8. Bid Price",
    )
    ask_price: str = Field(
        ...,
        title="The ask price of the exchange rate.",
        validation_alias="9. Ask Price",
    )


class TechIndicatorMetadataSchema(BaseModel):
    """The TechIndicatorMetadataSchema class defines the schema of the response returned by the
    `get_metadata` method."""

    symbol: str = Field(
        ...,
        title="The symbol of the stock.",
        validation_alias="1: Symbol",
    )
    indicator: str = Field(
        ...,
        title="The indicator of the stock.",
        validation_alias="2: Indicator",
    )
    last_refreshed: str = Field(
        ...,
        title="The date and time the data was last refreshed.",
        validation_alias="3: Last Refreshed",
    )
    interval: str = Field(
        ...,
        title="The interval of the data.",
        validation_alias="4: Interval",
    )
    time_period: int = Field(
        ...,
        title="The time period of the data.",
        validation_alias="5: Time Period",
    )
    series_type: str = Field(
        ...,
        title="The series type of the data.",
        validation_alias="6: Series Type",
    )
    time_zone: str = Field(
        ...,
        title="The time zone of the data.",
        validation_alias="7: Time Zone",
    )

    def __str__(self) -> str:
        """Returns the string representation of the class.

        Returns:
            str: `SYMBOL:INDICATOR`
        """
        return f"{self.symbol}:{self.indicator}"
