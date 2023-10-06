# class Banking:
# 	bankName="SbI"
# 	def __init__(self,accName,accNo,bal) -> None:
# 		self.accountName=accName
# 		self.accountNumber=accNo
# 		self.balance=bal
# 		self.transactions=[]
		

# 	def deposits (self,amountDeposit):
# 		self.balance=self.balance+amountDeposit
# 		self.transactions.append(amountDeposit)
# 		return self.balance

# 	def withdrawls(self,amountWithdrawls):
# 		if self.balance > amountWithdrawls:
# 			self.balance=self.balance - amountWithdrawls
# 			self.transactions.append(-amountWithdrawls)

# 		else:
# 			print("overdraft",self.balance-amountWithdrawls)

# 		return self.balance
		
# 	# def countTransactions(self,transactionsNumber):
# 	# 	(self.transactionsNumber)=transactionsNumber
# 	# 	return len(self.transactions)
	
	
# rahul = Banking("rahulSharma","10001",8000)

# print(rahul.bankName)             # SBI
# print(rahul.accountName)          #rahulSharma
# print(rahul.accountNumber)        #10001
# print(rahul.balance)              #8000

# rahul.withdrawls(100)
# rahul.withdrawls(10000)
# rahul.withdrawls(500)
# rahul.deposits(200)
# rahul.deposits(1000)

# print(rahul.balance)          #-1400
# print(rahul.transactions)     #[-100, -500, 200, 1000, -10000] 

			
# print (len(rahul.transactions))



# class BanK:
#     def __init__(self,accName,accNo,bal):
#         self.accName = accName
#         self.accNo = accNo
#         self.bal = bal
#         self.transactions = []

#     def withDrawl(self,amount):
#         if self.bal > amount:
#             self.bal = self.bal - amount
#             self.transactions.append(-amount)
#         else:
#             print("insufficient balance")
#         return self.bal

#     def depsosit(self,amount):
#         self.bal = self.bal + amount
#         self.transactions.append(amount)
#         return self.bal

#     def lastFiveTransactions(self):
#         return self.transactions[-5:]

# chinmay  =  BanK("chinmay","123",100)


# chinmay.depsosit(10)
# chinmay.withDrawl(100)
# chinmay.depsosit(100)
# chinmay.depsosit(200)
# chinmay.withDrawl(100)

# print(chinmay.lastFiveTransactions())


class Banking :
	def __init__(self,accName,accNum,bal) -> None:
		self.accountNumber=accNum
		self.accountName=accName
		self.balance=bal
		self.transactions=[]
	def deposits(self,amount):
		self.amountDeposit=amount
		self.balance=self.balance+amount
		self.transactions.append(amount)
		return self.balance
	def withdrawl(self,amount):
		if self.balance > amount:
			self.balance=self.balance-amount
			self.transactions.append(-amount)
		else:
			print("insufficiant balance",self.balance)
		return self.balance
	def numberOfTransactions(self):
		return len(self.transactions)
	def lastTransaction(self):
		return self.transactions[-1:-2]	
			
hdfc = Banking("ankurDeswal",21170,1000)
print(hdfc.accountName)     # ankur deswal
print(hdfc.accountNumber)   # 21170
print(hdfc.balance)         # 1000

hdfc.deposits(500)
hdfc.deposits(500)

print(hdfc.balance)        # 2000

hdfc.withdrawl(200)
hdfc.withdrawl(200)

print(hdfc.balance)        #1600

hdfc.withdrawl(1700)
print(hdfc.balance)       #insufficiant balance

hdfc.deposits(100)
hdfc.withdrawl(200)

print(hdfc.balance)

hdfc.deposits(1000)
hdfc.withdrawl(2000)
print(hdfc.balance)