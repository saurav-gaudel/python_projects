# income calculator

def finance_calculation(monthly_income:float, tax_rate:float, expenses:float, currency:str) ->None:
    yearly_income:float= monthly_income*12
    monthly_tax:float= monthly_income*(tax_rate/100)
    yearly_tax:float= monthly_tax*12
    net_monthly_income:float= monthly_income-monthly_tax
    net_yearly_income:float = net_monthly_income*12
    monthly_left_over:float= net_monthly_income-expenses


    print("----------------------------")
    print(f"Monthly Income = {currency}.{monthly_income:,.2f}")
    print(f"Monthly Tax = {currency}.{tax_rate}%")
    print(f"Yearly Income = {currency}.{yearly_income:.2f}")
    print(f"Yearly Tax = {currency}.{yearly_tax:,.2f}")
    print(f"Net Monthly Income = {currency}.{net_monthly_income:,.2f}")
    print(f"Net Yearly Income = {currency}.{net_yearly_income:,.2f}")
    print(f"Monthly_leftover:{currency}.{monthly_left_over:,.2f}")
    print("-----------------------------")


def get_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    monthly_income= get_float_input("Enter monthly income: ")
    tax_rate= get_float_input("Enter tax rate: ")
    rent= get_float_input("Enter cost for rent: ")
    food= get_float_input("Enter cost for food : ")
    expenses:float = rent + food
    
   
    finance_calculation(monthly_income, tax_rate ,expenses,currency="NRS.")

if __name__ == "__main__":
    main()



