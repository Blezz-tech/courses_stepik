def work(text, n):
    arr = list(map(int, text.split(' ')))
    heights = [-1] * n

    def compute_height(x):
        if x == -1:
            return 0
        if heights[x] != -1:
            return heights[x]
        
        heights[x] = 1 + compute_height(arr[x])
        return heights[x]

    max_height = 0
    for x in range(n):
        max_height = max(max_height, compute_height(x))

    return max_height

# IO side effects
def main():
    n = int(input())
    text = input()
    print(work(text, n))

main()

# Для проверки, в решение не входит

tasks = [
    {
        "input": [
            "4 -1 4 1 1",
            5
        ],
        "output": 3,
    },
    {
        "input": [
            "-1 0 4 0 3",
            5
        ],
        "output": 4,
    },
    {
        "input": [
            "9 7 5 5 2 9 9 9 2 -1",
            10
        ],
        "output": 4,
    },
]

for task in tasks:
    task_input = task['input']
    task_output = task['output']
    result = work(task_input[0], task_input[1])
    if task_output != result:
        print("Входное значение:", task_input)
        print("Выходное значение:", task_output)
        print("Полученное значение:", result)
        assert task_output == result
