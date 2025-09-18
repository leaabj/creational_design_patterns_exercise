
class GlobalBudget:
    """
    One shared marketing budget across the system.
    """
    _instance = None

    def __new__(cls, initial_amount: float = 0.0):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._balance  = max(0.0, initial_amount)
        return cls._instance

    def allocate(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient budget")
        if amount <= 0:
            raise ValueError("Allocation amount must be positive")

        self._balance -= amount

    def remaining(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"<GlobalBudget remaining={self._balance}>"
