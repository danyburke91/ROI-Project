class ReturnOnInvestment():
    
    def __init__(self, income, expenses, cash_flow):
        self.income = []
        self.expenses = []
        self.cash_flow = []
        
    def setIncome(self):
        input_income = input(" Please select your source of income (enter a whole number): Rental/Laundry/Misc: ")
        
        if input_income.lower() == 'rental':
            rental = int(input("Please enter your rental income $: "))
            self.income.append(rental)
            
        elif input_income.lower() == 'laundry':
            laundry = int(input("Please enter your laundry income $: "))
            self.income.append(laundry)
                     
        elif input_income.lower() == 'misc':
            Misc = int(input("Please enter your miscellaneous income $: "))
            self.income.append(Misc)
            
        elif input_income.lower == 'quit':
            pass
         
        else:
            print("Try another input")
        
        monthly_income = int(sum(self.income))
            
        print(f"Your total monthly income is $: {monthly_income}")
            
    def setExpenses(self):
        input_expense = (input("How much does it cost to own the property? Please enter your expenses for: Tax/Insurance/Utilities/Repairs/Mortgage/Other: "))
              
        if input_expense.lower() == 'tax':
            tax = int(input("Please enter your tax expense $: "))
            self.expenses.append(tax)
              
        elif input_expense.lower() == 'insurance':
            insurance = int(input("Please enter your insurance expense $: "))
            self.expenses.append(insurance)
              
        elif input_expense.lower() == 'utilities':
            utilities = int(input("Please enter your utilities expense $: "))
            self.expenses.append(utilities)
              
        elif input_expense.lower() == 'repairs':
            repairs = int(input("Please enter your repairs expenses $: "))
            self.expenses.append(repairs)
            
        elif input_expense.lower() == 'mortgage':
            mortgage = int(input("Please enter your monthly mortgage expense $: "))
            self.expenses.append(mortgage)
            
        elif input_expense.lower() == 'other':
            other = int(input("Please enter any other expenses $: "))
            self.expenses.append(other)
            
        elif input_expense.lower == 'quit':
            pass
        
        else:
            print("Try another input")
       
        monthly_expenses = int(sum(self.expenses))
        
        print(f"Your total monthly expenses are $: {monthly_expenses}")
              
    def setCashFlow(self):
        monthly_cashFlow = sum(self.income) - sum(self.expenses)
        self.cash_flow.append(monthly_cashFlow)
        print(f"This is the extra money you have each month (your cash flow) $: {monthly_cashFlow}")
        
    
              
    def setROI(self):
        total_investment = int(input("Please enter your total investment including (Down payment, closing costs, rehab, or misc): "))
        cashFlow = sum(self.cash_flow)
        annual_cashFlow = cashFlow * 12
        ROI = (annual_cashFlow / total_investment) * 100
    
        print(f"Your cash on cash Return Of Investment is: {ROI} percent.")


Rental_Property_Value = ReturnOnInvestment([], [], [])

def value():
    while True:
        response = input("Lets analyze this rental property, please select these options: (start with Income if beginning): Income/Expenses/Cash Flow/ROI/Quit to end - ")
        
        if response.lower() == 'income':
            Rental_Property_Value.setIncome()
        elif response.lower() == 'expenses':
            Rental_Property_Value.setExpenses()
        elif response.lower() == 'cash flow':
            Rental_Property_Value.setCashFlow()
        elif response.lower() == 'roi':
            Rental_Property_Value.setROI()
        elif response.lower() == 'quit':
            break
        else:
            print("Try another input")
            
value()