from langchain.tools import tool

from app.agent.tools.product_search import product_search_tool
#from app.config import Config


def get_product_price(doc) -> float:
    content = doc.page_content
    page_content_dict = {
    k.strip(): v.strip() for k, v in (
        line.split(":", 1) for line in content.splitlines() if ":" in line)}
    price = float(page_content_dict.get("price", 0))
    return price


@tool
def financing_tool(model: str, brand: str, years: int = 3) -> str:
    """Calculate the financing details for a car purchase."""
    if not 3 <= years <= 6:
        return "The term must be between 3 and 6 years."
    # Define constants
    interest_rate = 0.10
    down_payment_percent = 0.20
    item = product_search_tool(model + brand)
    if not item:
        return f"Model '{model}' with the specified brand was not found '{brand}'."
    price = get_product_price(item[0])
    months = years * 12
    down_payment = price * down_payment_percent
    financed_amount = price - down_payment
    monthly_interest_rate = interest_rate / 12
    monthly_payment = (financed_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)

    total_payment = monthly_payment * months
    # total_customer_payment = total_payment + down_payment 

    return (f"For product '{model, brand}' with a price of ${price:,.2f} USD:\n"
            f"- Down payment of {down_payment_percent * 100:.0f}%: ${down_payment:,.2f} USD\n"
            f"- Amount to finance: ${financed_amount:,.2f} USD\n"
            f"- Term: {years} years\n"
            f"- Estimated monthly payment: ${monthly_payment:,.2f} USD\n"
            f"- Annual interest rate: {interest_rate*100:.0f}%")
