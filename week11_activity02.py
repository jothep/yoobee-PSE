'''
Expense tracing program
'''
import unittest

class Expense:
    '''
    Expense for once
    '''
    def __init__(self, description: str, amount: float):
        self.description = description
        self.amount = amount

class ExpenseFactory:
    '''
    The factory for creating expense object
    '''
    @staticmethod
    def create(description: str, amount: float) -> Expense:
        if amount <= 0:
            raise ValueError("Amount should not be negative number")
        return Expense(description, amount)
    
class PersonalExpenseTracker:
    '''
    Manage personal expense
    '''
    def __init__(self):
        self._expenses = []
        self._factory = ExpenseFactory()

    def add_expense(self, description: str, amount: float):
        '''
        Add a new track of expense
        '''
        expense = self._factory.create(description, amount)
        self._expenses.append(expense)
        print(f"Added the expense: {description}, {amount:.2f}")

    def calculate_total(self) -> float:
        total = sum(expense.amount for expense in self._expenses)
        return total

class TestPersonalExpenseTracker(unittest.TestCase):
    '''
    Unit test
    '''

    def setUp(self):
        '''
        New instance for test'''
        self.tracker = PersonalExpenseTracker()

    def test_add_multiple_expenses(self):
        '''
        test add multiple expenses
        '''
        self.tracker.add_expense("Lunch", 15.00)
        self.tracker.add_expense("Tickets", 12.50)
        self.assertAlmostEqual(self.tracker.calculate_total(), 27.50)

if __name__ == '__main__':
    print("--- Personal Expense Tracker ---")
    myTracker = PersonalExpenseTracker()
    myTracker.add_expense("Books", 72.50)
    myTracker.add_expense("Bus Ticket", 20.00)
    total = myTracker.calculate_total()
    print(f"\nTotal Amount: ${total:.2f}\n")

    unittest.main()