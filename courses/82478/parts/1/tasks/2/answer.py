def tree_hieght(arr, x, height = 0):
    if x == -1:
        return height
    return tree_hieght(arr, arr[x], height + 1)
    

def work(text):
    arr = list(map(int, text.split(' ')))

    height = 0
    for x in arr:
        height = max(height, tree_hieght(arr, x))

    return height + 1

# IO side effects
def main():
    count = int(input())
    text = input()
    print(work(text))

main()

# Для проверки, в решение не входит

tasks = [
    {
        "input": "4 -1 4 1 1",
        "output": 3,
    },
    {
        "input": "-1 0 4 0 3",
        "output": 4,
    },
    {
        "input": "9 7 5 5 2 9 9 9 2 -1",
        "output": 4,
    },
]

for task in tasks:
    task_input = task['input']
    task_output = task['output']
    result = work(task['input'])
    if task_output != result:
        print("Входное значение:", task_input)
        print("Выходное значение:", task_output)
        print("Полученное значение:", result)
        assert task_output == result
