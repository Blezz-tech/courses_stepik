def execute_commands(commands):
    log = []
    stack_max = []
    for command in commands:
        match command[0]:
            case "push":
                x = int(command[1])
                if not stack_max:
                    stack_max.append(x)
                else:
                    stack_max.append(max(stack_max[-1], x))
            case "pop":
                stack_max.pop()
            case "max":
                log.append(stack_max[-1])
    return log


def list_splitting(lst):
    return [ x.split() for x in lst ]

def work(commands):
    return execute_commands(list_splitting(commands))


# IO side effects
def get_commands(count_commands):
    commands = []
    for i in range(count_commands):
        commands.append(input())
    return commands 

# IO side effects
def main():
    commands = get_commands(int(input()))  
    result = work(commands)
    if result != []:
        print("\n".join(list(map(str, result))))

main()

# Для проверки, в решение не входит

tasks = [
    {
        "input": [
            "push 2",
            "push 1",
            "max",
            "pop",
            "max",
        ],
        "output": [
            2,
            2,
        ]
    },
    {
        "input": [
            "push 1",
            "push 2",
            "max",
            "pop",
            "max",
        ],
        "output": [
            2,
            1,
        ]
    },
    {
        "input": [
            "push 2",
            "push 3",
            "push 9",
            "push 7",
            "push 2",
            "max",
            "max",
            "max",
            "pop",
            "max",
        ],
        "output": [
            9,
            9,
            9,
            9,
        ]
    },
    {
        "input": [
            "push 1",
            "push 2",
            "push 3",
            "push 4",
            "push 5",
            "push 6",
            "push 7",
            "push 8",
            "push 9",
            "push 10",
            "push 11",
            "max",
            "pop",
            "max",
            "pop",
            "max",
            "pop",
            "max",
            "pop",
            "max",
            "pop",
            "max",
            "pop",
            "max",
            "pop",
            "max",
            "pop",
            "max",
            "pop",
            "max",
            "pop",
            "max",
        ],
        "output": [
            11,
            10,
            9,
            8,
            7,
            6,
            5,
            4,
            3,
            2,
            1,
        ]
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
