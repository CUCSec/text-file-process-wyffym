student_number = '201811113002'
count = 0
with open('log_files/201811113002.log', encoding='utf-8') as file:
    for line in file:
        count += line.count(student_number)
print("我的学号在文件中出现的次数是：{0}次".format(count))
file.close()