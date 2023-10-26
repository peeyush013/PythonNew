class ExpansesQ1:
	def setJanExp(self,jan):
		self.januaryExpanses=jan
	def setFebExp(self,feb):
		self.februaryExpanses=feb
	def setMarExp(self,mar):
		self.marchExpanses=mar
	def getTotalExp(self):
		return self.januaryExpanses+self.februaryExpanses+self.marchExpanses	


class IncomeQ1:
	def setJanInc(self,jan):
		self.januaryIncome=jan
	def setFebInc(self,feb):
		self.februaryIncome=feb
	def setMarInc(self,mar):
		self.marchIncome=mar
	def getTotalIncome(self):
		return self.januaryIncome+self.februaryIncome+self.marchIncome	


class NetProfitQ1(ExpansesQ1,IncomeQ1):
	def getJanProfit(self):
		self.januaryProfit=self.januaryIncome-self.januaryExpanses
		return self.januaryProfit
	def getFebProfit(self):
		self.februaryProfit=self.februaryIncome-self.februaryExpanses
		return self.februaryProfit
	def getMarProfit(self):
		self.marchProfit=self.marchIncome-self.marchExpanses
		return self.marchProfit
	def getTotalProfit(self):
		return self.getTotalExp()-self.getTotalIncome()

Alphabet=ExpansesQ1()
Alphabet.setJanExp(20)
Alphabet.setFebExp(30)
Alphabet.setMarExp(35)

te=Alphabet.getTotalExp()
print(te)   #85

Alphabet=IncomeQ1()
Alphabet.setFebInc(50)
Alphabet.setMarInc(50)
Alphabet.setJanInc(50)

ti=Alphabet.getTotalIncome()
print(ti)   #150

Alphabet=NetProfitQ1()
tp=Alphabet.getTotalProfit()
print(tp)
