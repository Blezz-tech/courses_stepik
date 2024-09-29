    if not stack_max:
        stack_max.append(x)
    else:
        stack_max.append(max(stack_max[-1], x))

def work(count, numbers, window):
    stack_start = []
    stack_end = []
    result = []

    for i in numbers:





# IO side effects
def main():
    count = int(input())
    numbers = [int(x) for x in input().split()]
    window = int(input())
    
    result = work(count, numbers, window)
    print(result)

# main()

# Для проверки, в решение не входит

tasks = [
    {
        "input": {
            "count": 3,
            "numbers": [2, 1, 5],
            "window": 1,
        },
        "output": 2 1 5
    },
    {
        "input": {
            "count": 8,
            "numbers": [2, 7, 3, 1, 5, 2, 6, 2],
            "window": 4,
        },
        "output": 7 7 5 6 6
    },
]

for task in tasks:
    task_input = task['input']
    task_output = task['output']
    result = work(task['input'])
    if task_output != result:
        print("Входное значение: ", task_input)
        print("Выходное значение: ", task_output)
        print("Полученное значение: ", result)
        assert task_output == result
