tasks = []

def menu():
    print('\n --- to do list ---')
    print('1. add a task ')
    print('2. view a task ')
    print('3. mark a task completed')
    print('4. delete a task')
    print('5. exit')

def add():
    task = input('enter a task: ')
    tasks.append({'task': task, 'completed': False})
    print(f'Task {task} added succesfully !')

def view():
    if not tasks:
        print('no tasks to view')

    else:
        for index, task in enumerate(tasks):
            if task['completed']:
                status = '✓'
            else:
                status = '✗'
            print(f"{index}. {task['task']} [{status}]")
def mark():
    view()
    task_num = int(input('enter the task number to mark as done: '))

    if task_num < len(tasks) and task_num >= 0:
        tasks[task_num]['completed'] = True
        print(f"task '{tasks[task_num]['task']} marked completed !")
    else:
        print('invalid task number')

def delete():
    view()
    task_num = int(input('enter the task number to delete: '))
    
    if task_num < len(tasks) and task_num >= 0:
        deleted = tasks.pop(task_num)
        print(f"task '{deleted['task']}' deleted successfully ! ")
    else:
        print('invalid task number')

def main():
    while True:
        menu()
        choice = input('Enter your choice: ')

        if choice == '1':
            add()

        elif choice == '2':
            view()

        elif choice == '3':
            mark()

        elif choice == '4':
            delete()

        elif choice == '5':
            break

        else:
            print('invalid choice please enter between 1-5 only !')

main()
