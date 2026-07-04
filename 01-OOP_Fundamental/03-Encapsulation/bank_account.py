"""
对于balance和account_holder这两个变量只暴露了查询方法, 无法直接修改他们的值

这就是Encapsulation的作用: 保护关键变量不被篡改
"""



class BankAccount:
    def __init__(self, account_holder: str):
        self._account_holder = account_holder
        self._balance = 0.0
    
    def deposit(self, amount: float) -> None:
        # 存钱
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        # 取钱
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount

    @property
    def balance(self)->float:
        # 伪装成属性的方法, 可以 banckAccount.balance直接执行这个方法获得值
        return self._balance
    
    @property
    def account_holder(self) -> str:
        return self._account_holder