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
    def category(self, category: list[str]):
        if not category:
            raise ValueError("Category cannot be empty!")
        self.__category = category