# Напишите программу, которая считывает целое число и выводит текст,
# аналогичный приведенному в примере (важно в точности соблюдать
# вывод программы: обратите внимание на пробелы и на точки).
# Нельзя пользоваться конкатенацией строк,
# используйте print с несколькими параметрами.

n = int(input())

print("The next number for the number ", n, " is ", n + 1, ".", sep="")
print("The previous number for the number ", n, " is ", n - 1, ".", sep="")
