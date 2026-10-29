# # # 1. Совет по погоде — if / elif / else

# # # temperature = 10

# # # if temperature < 0:
# # #     print("Надень куртку по-братски")
# # # elif temperature <= 15:
# # #     print("Возьми куртку")
# # # else:
# # #     print("Можно в футболке")

# # # 2. Сумма чётных чисел — for

# # n = 10
# # total = 0

# # for i in range(1, n + 1):
# #     if i % 2 == 0:
# #         total += i

# # print(total)

# # 3. Список результатов — append / pop


# # scores = [10, 20, 30]

# # scores[0] = 15
# # scores.append(25)
# # removed = scores.pop()

# # print(removed)
# # print(scores)
# # print(len(scores))








# # # # # Накопить на покупку 4


# # # # balance = 100
# # # # deposit = 200
# # # # target = 1000

# # # # weeks = 0
# # # # while balance < target:
# # # #     balance += deposit
# # # #     weeks += 1

# # # # print(weeks)
# # # # print(balance)


# # # # Задача 5: стоимость доставки

# # # def delivery_cost(weight):
# # #     if weight <= 1:
# # #         return 100
# # #     elif weight <= 5:
# # #         return 250
# # #     else:
# # #         return 500


# # # print(delivery_cost(1))
# # # print(delivery_cost(5))
# # # print(delivery_cost(6))


# # 6. Итоги контрольной — Python

# def count_passed(scores, limit=50):
#     count = 0
#     for score in scores:
#         if score >= limit:
#             count += 1
#     return count


# scores = [40, 55, 70, 80]

# total = 0
# for score in scores:
#     total += score

# average = total / len(scores)

# print(total)
# print(average)
# print(count_passed(scores))

# if average >= 50:
#     print("Зачёт")
# else:
#     print("Повторить")
