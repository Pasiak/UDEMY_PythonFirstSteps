import datetime
import  time
import functools

def CreateFunctionWithWraper_LoGToFile(logFilePath):
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            file = open(logFilePath,"a")
            file.write("-"*30 + "\n")
            file.write("Function started at {}\n".format(datetime.datetime.now().isoformat()))
            file.write("Following arguments were used:\n")
            file.write(" ".join("{}".format(x) for x in args))
            file.write("\n")
            file.write(" ".join("{}={}".format(k,v) for (k,v) in kwargs.items()))
            file.write("\n")
            result = func(*args, **kwargs)
            file.write("Function returned {}\n".format(result))
            file.close()
            return result

        return func_with_wrapper

    return CreateFunctionWithWrapper

@CreateFunctionWithWraper_LoGToFile(r"C:\Users\El Patrico\Desktop\tempTXT\change_slary_log.txt")
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS={}'.format(emp_name, new_salary, is_bonus))
    return new_salary
@CreateFunctionWithWraper_LoGToFile(r"C:\Users\El Patrico\Desktop\tempTXT\change_possition_log.txt")
def ChangePossition(empName, empPossition):
    print("Changing possition for {} TO {}".format(empName,empPossition))
    return empPossition

ChangeSalary('Johnson', 20000, True)
print(ChangeSalary('Johnson', 20000, True))
ChangePossition("John","Manager")

