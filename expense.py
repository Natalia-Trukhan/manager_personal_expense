import json
from pathlib import Path


class Expense:
    def __init__(self, title: str, amount: float, category: list[str], id: int) -> None:
        self.title = title
        self.amount = amount
        self.category = category
        self.id = id

    def __str__(self) -> str:

        return f"{self.id}. Title={self.title}, amount={self.amount}, category={list(self.category)}."

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        if not title:
            raise ValueError("Title cannot be empty!")
        self.__title = title

    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, amount: float) -> None:
        if not amount:
            raise ValueError("Amount cannot be empty!")
        elif amount <= 0:
            raise ValueError("Amount must be greater than Zero!")
        self.__amount = amount

    @property
    def category(self) -> list[str]:
        return self.__category

    @category.setter
    def category(self, category: list[str]) -> None:
        if not category:
            raise ValueError("Category cannot be empty!")
        self.__category = category


class OperationsUnderExpense:
    def __init__(self, path_json: str = "file.json") -> None:
        self.path_file_json: Path = Path(path_json)
        self.list_objects: list[Expense] = self.load_from_json()

    def add_expense(self, expense: Expense):
        self.list_objects.append(expense)
        self.add_to_json()

    def add_to_json(self) -> None:
        obj: list[dict] = [
            {"id": item.id,
             "title": item.title,
             "amount": item.amount,
             "category": list(item.category)
             }
            for item in self.list_objects
        ]

        with open(self.path_file_json, "w", encoding="utf-8") as file:
            json.dump(obj, file, ensure_ascii=False, indent=4)

    def load_from_json(self) -> list[Expense]:
        if not self.path_file_json.exists():
            return []

        list_obj: list[Expense] = []
        with open(self.path_file_json, "r", encoding="utf-8") as file:
            load_file = json.load(file)
        for item in load_file:
            obj = Expense(title=item["title"], amount=item["amount"],
                          category=item["category"], id=item["id"])
            list_obj.append(obj)
        return list_obj

    def __str__(self) -> str:
        if not self.list_objects:
            return f"No expense jet!"
        return "\n".join(str(i) for i in self.list_objects)

    def search_certain_category(self, category: str) -> list[Expense]:
        list_obj: list[Expense] = []
        for expense in self.list_objects:
            for cat in expense.category:
                if cat.lower() == category.lower():
                    list_obj.append(expense)
        return list_obj

    def show_total_amount(self) -> float:
        total_amount: float = 0.0
        if not self.list_objects:
            raise ValueError("Expense list is empty!")
        for exp in self.list_objects:
            total_amount += exp.amount
        return total_amount

    def id_number(self) -> int:
        counter: int = len(self.list_objects)
        return counter + 1
