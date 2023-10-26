
class StudentInfo2:
    # class variable
    standard = "12th"

    @classmethod
    def changeStandard(cls, newStandard):
        StudentInfo2.standard = newStandard

    # instance variable
    def __init__(self, mat, eng, eco, acc, bs):
        self.mathsMarks = mat
        self.engMarks = eng
        self.ecoMarks = eco
        self.accMarks = acc
        self.businessmarks = bs

    # instance method
    def totalMarks(self):
        print(sum([self.mathsMarks, self.engMarks,
              self.ecoMarks, self.accMarks, self.businessmarks, self.computerMarks]))

    def createMarks(self, comp):
        self.computerMarks = comp

    def retriveMarks(self):
        return self.engMarks

    def updateMarks(self, acc, mat, eco, bs, eng):

        self.mathsMarks = mat
        self.engMarks = eng
        self.ecoMarks = eco
        self.accMarks = acc
        self.businessmarks = bs
        


kartik = StudentInfo2(99, 98, 99, 90, 91)

print(kartik.engMarks)  # 98
print(kartik.businessmarks)  # 91
print(kartik.accMarks)  # 90
print(kartik.ecoMarks)  # 99
print(kartik.mathsMarks)   # 99

kartik.createMarks(100)
print(kartik.computerMarks)

kartik.totalMarks()  # 577

kartik.updateMarks(80, 81, 82, 83, 84)
print(kartik.engMarks)  # 84
print(kartik.businessmarks)  # 83
print(kartik.accMarks)  # 80
print(kartik.ecoMarks)  # 82
print(kartik.mathsMarks)  # 81

kartik.totalMarks()  # 510
