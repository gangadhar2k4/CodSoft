import math
class SimpleCalculator():
    def __init__(self):
        pass

    def Addition(self , num1, num2):
        return num1 + num2

    def Substraction(self , num1, num2):
        return num1 - num2

    def Multiplication(self , num1, num2):
        return num1 * num2

    def Division(self, num1, num2):
        try:
            return round(num1 / num2, 3)
        except ZeroDivisionError:
            print("You cann't divide a number with Zero.")
        return 'Infinity'

    def Modulus(self, num1, num2):
        return num1 % num2

    def Expression(self, expression):

        try:
            return round(eval(expression),3)
        except Exception:
            print('Please check the expression and rewrite it!')
    def SquareRoot(self,num):
        try:
            return math.sqrt(num)
        except ValueError:
            print('Negative numbers are not allowed')

class Main(SimpleCalculator):

    def __init__(self):
        print('################ Simple Calculator ################')

    def ValidateFuntionId(self,operation):
        if operation.isdigit():
            operation = int(operation)
            if 1 <= operation <= 7:
                return operation
            else:
                print('Invalid ID.')
        else:
            print('Characters are not allowed.')

    def TakeInputAndValidate(self,cnum):
        nums = [0, 0]
        for i in range(cnum):
            while True:
                num = input(f'Enter number-{i + 1} ?\n')
                if num.isdigit():
                    num = int(num)
                    nums[i] = num
                    break
                else:
                    print('Charcters or Symbols are not allowed.')
        return nums

    def CallingRightFuntion(self,operation):
        match operation:
            case 1:
                num1, num2 = self.TakeInputAndValidate(2)
                return self.Addition(num1, num2)
            case 2:
                num1, num2 = self.TakeInputAndValidate(2)
                return self.Substraction(num1, num2)
            case 3:
                num1, num2 = self.TakeInputAndValidate(2)
                return self.Multiplication(num1, num2)
            case 4:
                num1, num2 = self.TakeInputAndValidate(2)
                return self.Division(num1, num2)
            case 5:
                num1, num2 = self.TakeInputAndValidate(2)
                return self.Modulus(num1, num2)
            case 6:
                expression = input('Enter Mathematical Expression ?\n')
                return self.Expression(expression)
            case 7:
                num = self.TakeInputAndValidate(1)[0]
                return self.SquareRoot(num)
            case 8:
                exit(0)
    def main(self):
        while True:
            print('All the operations are provided in the below:')
            print('1.Addition - [+]')
            print('2.Substraction - [-]')
            print('3.Multiplication - [x]')
            print('4.Division - [/]')
            print('5.Modulus - [%]')
            print('6.Expression - [+,-,*,/,%,^]')
            print('7.SquareRoot - sqrt()')
            print('8.Exit')

            while True:
                operation = input('Enter operation id ?')

                operation = self.ValidateFuntionId(operation)
                if operation:
                    break

            Answer = self.CallingRightFuntion(operation)
            print(f'<< {Answer} >>')

            runAgain = input('Do you want to calculate again?(Y/N)')

            if runAgain.lower() == 'n':
                break

if __name__ == '__main__':

    cal = Main()
    cal.main()

