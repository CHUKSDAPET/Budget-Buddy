"""
A Python-based Spending Planner to manage personal finances. Users input income and expenses 
to receive tailored budgeting advice, savings analysis, and investment tips.
The tool also offers insights into job satisfaction. Easy-to-use interface for those seeking to optimize financial health.
"""

class SpendingPlanner:
    def __init__(self):
        self.user_data = {}

    def collect_user_data(self):
        # Collect only essential data
        state = input("Enter your state and zip code: ")
        marital_status = input("Marital status (married/single): ")
        kids = int(input("Number of kids: "))
        payment_type = input("Payment type (hourly/salary): ")

        if payment_type == "hourly":
            hours_per_week = int(input("Hours worked per week: "))
            hourly_rate = float(input("Hourly rate: "))
            monthly_income = 4 * hours_per_week * hourly_rate
        else:
            monthly_income = float(input("Monthly salary: "))

        bonuses = float(input("Monthly bonuses: $"))
        total_income = monthly_income + bonuses

        # Collect expense data
        rent = float(input("Monthly rent: $"))
        utilities = float(input("Monthly utilities: $"))
        food = float(input("Monthly food expense: $"))
        car_payment = float(input("Monthly car payment: $"))
        insurance = float(input("Monthly insurance costs: $"))

        self.user_data = {
            'monthly_income': total_income,
            'expenses': {
                'rent': rent,
                'utilities': utilities,
                'food': food,
                'car_payment': car_payment,
                'insurance': insurance
            },
            'job_fulfillment': input("Are you fulfilled in your job? (yes/no): "),
        }

    def calculate_expenses(self):
        expenses = self.user_data['expenses']
        total_expenses = sum(expenses.values())
        savings = self.user_data['monthly_income'] - total_expenses
        return total_expenses, savings

    def provide_advice(self):
        total_expenses, savings = self.calculate_expenses()
        income = self.user_data['monthly_income']
        
        # Budget assessment
        if total_expenses > 0.6 * income:
            print("You are spending over 60% of your income. Reduce expenses.")
        else:
            print("You are spending within your budget. Good job!")

        # Saving advice
        if savings < 0.4 * income:
            print("Aim to save at least 40% of your income.")
        else:
            print("You are saving well.")

        # Investment tips
        invest_amount = 0.2 * savings
        print(f"Invest ${invest_amount:.2f} for growth.")
        print(f"Save ${0.2 * savings:.2f} in a savings account.")
        
        # Job satisfaction advice
        if self.user_data['job_fulfillment'] == "no":
            print("Consider career changes to improve job satisfaction.")

def main():
    planner = SpendingPlanner()
    planner.collect_user_data()
    planner.provide_advice()

if __name__ == "__main__":
    main()


