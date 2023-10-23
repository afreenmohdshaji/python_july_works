class Bank:
    acc_no:int
    ac_type:str
    balance:int
    bank_name="SBI"

    def __init__(self,acc_no,ac_type,balance):
        self.acc_no=acc_no
        self.ac_type=ac_type
        self.balance=balance
    def withrawal(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(f"your {self.acc_no} has debited amount of {amount} from your {Bank.bank_name}")
        else:
            print("insuficient fund ")

    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.acc_no} has credited {amount} in your account")

    

    def balance_enq(self):
        print(f"your current balance in your {self.ac_type} account is {self.balance}")
    
    

bk1=Bank(1234,"savings",50000)
# bk1.set_account(1234,"savings",50000,"afreen")
bk1.withrawal(1000)
bk1.deposit(2000)
bk1.balance_enq()
bk2=Bank(2653,"current",100000)
bk2.withrawal(20000)
bk2.deposit(50000)
bk2.balance_enq()


