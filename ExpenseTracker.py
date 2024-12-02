class ExpenseTracker:

    def __init__(self):
        self.expenses = []  # Tuščias sąrašas, kuriame bus žodynai

    def add_expense(self, expense: str, sum: float, category: str):
        # Sukuriame žodyną su išlaidų duomenimis
        self.expenses.append({"expense": expense, "sum": sum, "category": category})
        print(f"Kam išleista: {expense}, Suma: ${sum:.2f}, Kategorija: {category}")

    def remove_expense(self, expense: str):
        for i, item in enumerate(self.expenses):
            if item["expense"] == expense:
                del self.expenses[i]
                print(f"Išlaida '{expense}' pašalinta.")
                return
        print(f"Išlaida '{expense}' nerasta.")

    def display_expenses(self):
        if not self.expenses:  # Jei sąrašas tuščias
            print("Nėra išlaidų!")
        else:
            for expense in self.expenses:
                print(f"Išlaida: {expense['expense']}, Suma: ${expense['sum']:.2f}, Kategorija: {expense['category']}")

    def total_expenses(self):
        return sum(expense['sum'] for expense in self.expenses)

    def filter_by_category(self, category: str):
        return [f"{expense['expense']}: ${expense['sum']:.2f}" for expense in self.expenses if expense['category'] == category]


# Naudojimas
tracker = ExpenseTracker()
tracker.add_expense("Kava", 5.00, "Maistas")
tracker.add_expense("Taksi", 15.00, "Transportas")
tracker.add_expense("Knyga", 20.00, "Švietimas")
tracker.add_expense("Pica", 12.00, "Maistas")
tracker.remove_expense("Kava")
tracker.add_expense("Arbata", 4.00, "Maistas")
tracker.display_expenses()

print(f"Bendros išlaidos: ${tracker.total_expenses():.2f}")
print("Maisto išlaidos:", tracker.filter_by_category("Maistas"))
