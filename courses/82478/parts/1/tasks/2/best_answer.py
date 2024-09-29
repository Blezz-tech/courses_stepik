def work(s, n):
    d={}
    def up(v):
        next=s[v]
        if next==-1:
            return 1
        if v not in d:
            d[v]=up(next)+1
        return d[v]

    mx = 0
    for i in range(n):
        mx = max(mx, up(i))
    return mx

def main():
    n = int(input())
    s = list(map(int, input().split()))
    n = len(s)

    print(work(s, n))

# main()

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
    s = list(map(int, task_input[0].split()))
    n = task_input[1]

    task_output = task['output']
    result = work(s, n)
    if task_output != result:
        print("Входное значение:", task_input)
        print("Выходное значение:", task_output)
        print("Полученное значение:", result)
        assert task_output == result
