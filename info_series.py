from os import getenv
from alpha_vantage.fundamentaldata import FundamentalData
from typing import Literal, List, Union, Annotated
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import strawberry
from pandas import DataFrame

load_dotenv()
key = getenv("AV_KEY")
av = FundamentalData(key=key)

type FloatOrNone = Annotated[
    Union[float, Literal["None"]], strawberry.union("FloatOrNone")
]


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


@strawberry.experimental.pydantic.type(IncomeStatementSchema, all_fields=True)
class IncomeStatementType:
    """The class "IncomeStatementType" is defined."""

    pass


def manipulate_is(data: DataFrame) -> List[IncomeStatementType]:
    """
    The function `manipulate_is` converts a DataFrame into a list of IncomeStatementType objects by
    validating the data and converting it into the appropriate format.

    :param data: The `data` parameter is a DataFrame object
    :type data: DataFrame
    :return: The function `manipulate_is` returns a list of `IncomeStatementType` objects.
    """
    as_json = data.to_dict(orient="index")
    items = as_json.values()
    l: List[IncomeStatementType] = []
    for i in items:
        pymodel = IncomeStatementSchema.model_validate(i)
        gqltype: IncomeStatementType = IncomeStatementType.from_pydantic(pymodel)
        l.append(gqltype)
    return l


@strawberry.type
class INCOME_STATEMENT:
    """The `INCOME_STATEMENT` class provides methods to retrieve and manipulate annual and quarterly income
    statement data for a given stock symbol."""

    @strawberry.field
    def get_income_statement_annual(self, symbol: str) -> List[IncomeStatementType]:
        """
        The function `get_income_statement_annual` retrieves annual income statement data for a given
        stock symbol and returns a manipulated version of the data.

        :param symbol: The symbol parameter is a string that represents the stock symbol of a company.
        It is used to retrieve the income statement data for that specific company
        :type symbol: str
        :return: a list of IncomeStatementType objects.
        """
        data, _ = av.get_income_statement_annual(symbol)
        data: DataFrame
        return manipulate_is(data)

    @strawberry.field
    def get_income_statement_quarterly(self, symbol: str) -> List[IncomeStatementType]:
        """
        The function `get_income_statement_quarterly` retrieves quarterly income statement data for a
        given stock symbol and returns a manipulated version of the data.

        :param symbol: The "symbol" parameter is a string that represents the stock symbol of a company
        :type symbol: str
        :return: a list of IncomeStatementType objects.
        """
        data, _ = av.get_income_statement_quarterly(symbol)
        data: DataFrame
        return manipulate_is(data)


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


@strawberry.experimental.pydantic.type(CashFlowSchema, all_fields=True)
class CashFlowType:
    pass


def manipulate_cf(data: DataFrame) -> List[CashFlowType]:
    """
    The function `manipulate_cf` takes a DataFrame as input, converts it to a dictionary, validates the
    data using a CashFlowSchema model, and then converts the validated data to a list of CashFlowType
    objects.

    :param data: The `data` parameter is a DataFrame object
    :type data: DataFrame
    :return: The function `manipulate_cf` returns a list of `CashFlowType` objects.
    """

    as_json = data.to_dict(orient="index")
    items = as_json.values()
    l: List[CashFlowType] = []
    for i in items:
        pymodel = CashFlowSchema.model_validate(i)
        gqltype: CashFlowType = CashFlowType.from_pydantic(pymodel)
        l.append(gqltype)
    return l


@strawberry.type
class CASH_FLOW:
    """The `CASH_FLOW` class provides methods to retrieve and manipulate annual and quarterly cash flow
    data for a given stock symbol."""

    @strawberry.field
    def get_cash_flow_annual(self, symbol: str) -> List[CashFlowType]:
        """
        The function `get_cash_flow_annual` retrieves annual cash flow data for a given stock symbol and
        returns a manipulated version of the data.

        :param symbol: The symbol parameter is a string that represents the stock symbol of a company.
        It is used to retrieve the cash flow data for that specific company
        :type symbol: str
        :return: a list of CashFlowType objects.
        """
        data, _ = av.get_cash_flow_annual(symbol)
        data: DataFrame
        return manipulate_cf(data)

    @strawberry.field
    def get_cash_flow_quarterly(self, symbol: str) -> List[CashFlowType]:
        """
        The function `get_cash_flow_quarterly` retrieves quarterly cash flow data for a given stock symbol
        and returns a manipulated version of the data.

        :param symbol: The "symbol" parameter is a string that represents the stock symbol of a company
        :type symbol: str
        :return: a list of CashFlowType objects.
        """
        data, _ = av.get_cash_flow_quarterly(symbol)
        data: DataFrame
        return manipulate_cf(data)


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


@strawberry.experimental.pydantic.type(BalanceSheetSchema, all_fields=True)
class BalanceSheetType:
    """The class BalanceSheetType is defined."""

    pass


def manipulate_bs(data: DataFrame) -> List[BalanceSheetType]:
    """
    The function `manipulate_bs` takes a DataFrame as input, converts it to a dictionary, validates the
    data using a BalanceSheetSchema model, and then converts the validated data to a list of BalanceSheetType
    objects.

    :param data: The `data` parameter is a DataFrame object
    :type data: DataFrame
    :return: The function `manipulate_bs` returns a list of `BalanceSheetType` objects.
    """

    as_json = data.to_dict(orient="index")
    items = as_json.values()
    l: List[BalanceSheetType] = []
    for i in items:
        pymodel = BalanceSheetSchema.model_validate(i)
        gqltype: BalanceSheetType = BalanceSheetType.from_pydantic(pymodel)
        l.append(gqltype)
    return l


@strawberry.type
class BALANCE_SHEET:
    """The `BALANCE_SHEET` class provides methods to retrieve and manipulate annual and quarterly balance sheet
    data for a given stock symbol."""

    @strawberry.field
    def get_balance_sheet_annual(self, symbol: str) -> List[BalanceSheetType]:
        """
        The function `get_balance_sheet_annual` retrieves annual balance sheet data for a given stock symbol and
        returns a manipulated version of the data.

        :param symbol: The symbol parameter is a string that represents the stock symbol of a company.
        It is used to retrieve the balance sheet data for that specific company
        :type symbol: str
        :return: a list of BalanceSheetType objects.
        """
        data, _ = av.get_balance_sheet_annual(symbol)
        data: DataFrame
        return manipulate_bs(data)

    @strawberry.field
    def get_balance_sheet_quarterly(self, symbol: str) -> List[BalanceSheetType]:
        """
        The function `get_balance_sheet_quarterly` retrieves quarterly balance sheet data for a given stock symbol
        and returns a manipulated version of the data.

        :param symbol: The "symbol" parameter is a string that represents the stock symbol of a company
        :type symbol: str
        :return: a list of BalanceSheetType objects.
        """
        data, _ = av.get_balance_sheet_quarterly(symbol)
        data: DataFrame
        return manipulate_bs(data)
