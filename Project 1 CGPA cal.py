# # def calculate_gpa(marks):
# #
# #     if 80 <= marks <= 100:
# #         return "A+", 4
# #     elif 75 <= marks <= 79:
# #         return "A", 3.75
# #     elif 70 <= marks <= 74:
# #         return "A-", 3.5
# #     elif 65 <= marks <= 69:
# #         return "B+", 3.25
# #     elif 60 <= marks <= 64:
# #         return "B", 3.00
# #     elif 55 <= marks <= 59:
# #         return "B-", 2.75
# #     elif 50 <= marks <= 54:
# #         return "C+", 2.50
# #     elif 45 <= marks <= 49:
# #         return "C", 2.25
# #     elif 40 <= marks <= 44:
# #         return "D", 2.00
# #     else:
# #         return "F", 0  # Assuming F for marks below 40
# #
# # def main():
# #     try:
# #         # Input marks from the user
# #         marks = int(input("Enter your marks (0-100): "))
# #
# #         # Validate marks range
# #         if 0 <= marks <= 100:
# #             grade, grade_point = calculate_gpa(marks)
# #             print(f"Your Grade: {grade}")
# #             print(f"Your Grade Point: {grade_point}")
# #         else:
# #             print("Invalid marks. Please enter a value between 0 and 100.")
# #     except ValueError:
# #         print("Invalid input. Please enter a numeric value.")
# #
# # if __name__ == "__main__":
# #     main()
#
#
#
# subjects = ['bangla','english','math',23]
#
# copy_1= subjects[:]
# copy_1.append(12)
#
# # copy_2= subjects
# # copy_2.append(56)
#
#
# print("subjects",subjects)
# print("copy_1",copy_1)
#
# # a= 5
# # b=a
# #
# # b=b+5
# #
# # print(a)
# # print(b)
#
#


# fruits = ['A','B','C']
# for fruit in fruits:
#     print(fruit)
#
# number=[1,2,3,4,5,6]
# for num in number:
#     print(num)
#
# name = ["zubair","ahmed","bijoy"]
# for nam in name:
#     print(nam)




# for x in range(1,100,2):
#     print(x) #odd number 1-100

#1. List
# numbers= [1,2,3]
# for num in numbers:
#     print(num)
#String
# name="Python"
# for char in name:
#     print(char)
#3.Dictionary
# person = {"Enter Your Name": "John", "age": 25}
# for key, value in person.items():
#     print(key, ":",value)
#
# #4.rang
# for i in range(1,6):
#     print(i)

# sum = 0
#
# for x in range(5):
#     sum=sum+x
#     print(sum)
#
# print(sum)

#list

nums = [1,2,3,4,5,6,7]
for num in nums:
  if num % 2 == 0:
      print(num)