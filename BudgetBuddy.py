"""
Spending planner App 
Using python, I want to create an app that will monitor a persons spending habit; an app that will make sure it holds them accountable for every money they earn to allow them have savings. Then this app can suggest what they can invest their savings into and advice them on the percentage of their money that should seat in a savings account which will yield some percentage as it seats in the savings account. Now if this person is spending so much, I need this app to be able to advice them on how to cut their spending or find another job (if they feel miserable) working at the current job: 

Questions for the user to answer: 
	1.	What state and zip code do you live in?
	2.	Are you married, single?
	3.	Do you have kids? If yes, how many? 
	4.	Do you have parents and siblings? If yes, how many siblings do you have and what are their ages? What are the ages of your parents? 
	5.	Are you being paid in wages per hour or are you a salary earner? 
	6.	How many hours do you work a week and how much are you being paid per hour?
	7.	How much salary do you earn per month? 
	8.	Do you get bonuses? 
	9.	Do you have any debt on your name? What type of debt? For example, student loan, credit card debt? 
	10.	What are the utilities you spend your money on every month and cost? For example: charges for electricity, water, sewer, gas, trash, and potentially internet and cable Allow the person to input their utility bills and amount 
	11.	How much is your monthly rent? 
	12.	Do you spend weekly or monthly on food? How much do you spend weekly on food or else how much do you spend monthly on food? 
	13.	Do you have a car? If yes, is it paid for  or you pay for it monthly? If yes, how much do you pay for your car per month? 
	14.	How many miles do you travel to work? 
	15.	Do you have any insurance you pay for? If yes, list them for example; car, renters, health insurance 
	16.	Do you find fulfillment in the job you do?
	17.	Is there room to grow at your current job? 
After the user answers all the questions, go ahead and tell them if they are spending too much per month. For example, let them know they shouldn’t spend no more than 25% percent on rent per month. Split their monthly expenses to 60 percent (rent 20%, food 7%, insurance 10%, utilities 10%, gas 8%, 5% spending)  for In all, make sure they are able to save at least 40% percent of their money every month and let this app direct them on how to invest 20% of their savings on stocks and the remainder 20% percent should be saved in a bank account that yields good return on profits. But if this person answers they don’t feel fulfilled at their current job, direct them on how to have a target of 1 year to work and save up with the above percentage and quit. 20% of their savings should be invested in self growth 
Direct me on how to upload this on my GitHub account 



Answer: 

Creating a spending planner app involves several steps, including defining a structure for user interaction, calculating expenses, and advising on financial goals. Below is an outline of how you can create this app using Python. Here's a simplified version of the code and guidance on uploading it to GitHub.
Step 1: Define the Structure
First, set up a basic structure for collecting user information and calculating expenses.
Step 2: Create the Python Script
class SpendingPlanner:
    def _init_(self):
        self.user_data = {}
"""

"""
class SpendingPlanner:
    def __init__(self):
        self.user_data = {}

    def collect_user_data(self):
        self.user_data['state'] = input(
            "What state and zip code do you live in? ")
        self.user_data['marital_status'] = input("Are you married or single? ")
        self.user_data['kids'] = int(
            input("Do you have kids? If yes, how many? "))
        self.user_data['parents_siblings'] = input(
            "Do you have parents and siblings? Please list them. ")
        self.user_data['payment_type'] = input(
            "Are you paid hourly or on salary? ")

        if self.user_data['payment_type'] == "hourly":
            self.user_data['hours_per_week'] = int(
                input("How many hours do you work a week? "))
            self.user_data['hourly_rate'] = float(
                input("How much are you paid per hour? "))
            self.user_data['monthly_income'] = 4 * \
                self.user_data['hours_per_week'] * \
                self.user_data['hourly_rate']
        else:
            self.user_data['monthly_income'] = float(
                input("What is your monthly salary? "))

        self.user_data['bonuses'] = float(
            input("Do you get bonuses? Enter the amount. "))
        self.user_data['debts'] = input(
            "Do you have any debts? Please list the type and amounts. ")
        self.user_data['utilities'] = float(
            input("Enter your total monthly utilities cost: "))
        self.user_data['rent'] = float(input("Enter your monthly rent: "))
        self.user_data['food'] = float(
            input("Enter your monthly food expense: "))
        self.user_data['car_payment'] = float(
            input("Enter your monthly car payment: "))
        self.user_data['miles_to_work'] = float(
            input("How many miles do you travel to work? "))
        self.user_data['insurance'] = float(
            input("Enter your total monthly insurance costs: "))
        self.user_data['job_fulfillment'] = input(
            "Do you find fulfillment in your job? (yes/no) ")
        self.user_data['room_to_grow'] = input(
            "Is there room to grow at your current job? (yes/no) ")

    def calculate_expenses(self):
        expenses = {
            'rent': self.user_data['rent'],
            'utilities': self.user_data['utilities'],
            'food': self.user_data['food'],
            'car_payment': self.user_data['car_payment'],
            'insurance': self.user_data['insurance']
        }

        total_expenses = sum(expenses.values())
        savings = self.user_data['monthly_income'] - total_expenses

        return total_expenses, savings

    def provide_advice(self):
        total_expenses, savings = self.calculate_expenses()
        income = self.user_data['monthly_income'] + self.user_data['bonuses']

        if total_expenses > 0.6 * income:
            print("You are spending too much. Try to cut down your expenses.")
        else:
            print("Good job! You are within your budget.")

        # Saving strategies
        if savings < 0.4 * income:
            print("Try to save at least 40% of your income.")
        else:
            print("You are saving appropriately.")

        # Investment advice
        invest_amount = 0.2 * savings
        print(f"Consider investing {invest_amount} in stocks for growth.")
        print(
            f"Save the remaining {0.2 * savings} in a high-yield savings account.")

        if self.user_data['job_fulfillment'] == "no":
            print("Consider saving up for a year and invest in personal growth.")


def main():
    planner = SpendingPlanner()
    planner.collect_user_data()
    planner.provide_advice()


if __name__ == "__main__":
    main()




Step 3: Upload to GitHub
	•			Create a GitHub Account: If you don't have one, sign up at github.com.
	•			Initialize a Local Repository:
	•			Create a directory for your project.
	•			Move your Python script into this directory.
	•			Open a terminal (or command prompt) and navigate to your project directory.
	•			Initialize Git:git init
	•			Add Your Script:git add your_script.py
	•			Commit Your Changes:git commit -m "Initial commit of Spending Planner app"
	•			Create a GitHub Repository:
	•			Go to GitHub and create a new repository.
	•			Follow on-screen instructions to push your local repository to GitHub. Typically, the commands will look like:
	•			git remote add origin https://github.com/yourusername/your-repo-name.git
	•			git branch -M main
	•			git push -u origin main
	•			Verify on GitHub: Go to your repository link to ensure your code is uploaded.
This basic structure should help you start building the app. You can expand it with more features and improve it based on user feedback.


Here's a brief explanation of each function and keyword:
	•			_init_: A special method in Python used to initialize objects of a class. Called automatically when a new instance is created.
	•			def: A keyword used to define a new function or method in Python.
	•			float: Converts a number or a string to a floating-point number, which is a decimal value.
	•			input: Reads a line of text from user input and returns it as a string.
	•			int: Converts a number or a string to an integer.
	•			print: Outputs the specified message to the screen.
	•			sum: Calculates and returns the total of a sequence of numbers.
	•			if: A control flow statement that executes a block of code if its condition evaluates to True.
	•			else: Used alongside if to execute a block of code when the if condition is False.
	•			return: Exits a function and optionally passes back an expression to the caller.
	•			main: A common name for the main function in a script, usually where the script's execution begins.
	•			self: Represents the instance of the class. Used to access variables and methods within the class.

In programming, "initialize" means to assign an initial value to a variable, object, or data structure before it is used, ensuring it has a defined starting state
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


#Key Changes from the previous code above:
#Streamlined Input: Removed non-essential information like detailed family data for clarity.
#Refined Financial Calculation: Integrated bonuses directly into income for a clearer view.
#Clearer Output Messages: Provides straightforward financial and career advice.
#Simplified Expense Data Structure: Stores expenses in a dictionary, making it easier to manage.