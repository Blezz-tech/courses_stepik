def execute_commands(commands):
    log = []
    stack = []
    stack_max = []
    for command in commands:
        match command[0]:
            case "push":
                stack.append(command[1])
                if (len(stack) == 1):
                    stack_max.append(stack[-1])
                else:
                    stack_max.append(max(stack_max[-1], stack[-1]))
            case "pop":
                stack.pop()
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
        print("\n".join(result))

# main()

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
            "2",
            "2",
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
            "2",
            "1",
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
            "9",
            "9",
            "9",
            "9",
        ]
    }
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
