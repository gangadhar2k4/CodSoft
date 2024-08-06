
from ToDoListBlocks import PrintInOrder,ValidateInput,returnFormatedTime,CurrentDateTime,returnFormatedDate,ValidateTaskId,ValideteDate,ValideteTime
class Task:
    def __init__(self,TaskId,CurrentTime,CurrentDate,TaskTime,TaskDate,TaskContent):
        self.TaskId = TaskId
        self.CurrentTime = CurrentTime
        self.CurrentDate = CurrentDate
        self.TaskTime = TaskTime
        self.TaskDate = TaskDate
        self.TaskContent = TaskContent
class ToDoList:
    def __init__(self):
        pass
    TaskId = 0
    Tasks = []
    def AddTask(self):

        self.TaskId = self.TaskId + 1
        cdate,ctime = CurrentDateTime()
        CurrentDate = returnFormatedDate(cdate)
        CurrentTime = returnFormatedTime(ctime)
        TaskContent = input('What is your Task? Clearly describe what needs to be done.\n')
        while True:
            tdate = input('Enter date that will remind you (DD/MM/YYYY) ?')
            if ValideteDate(tdate,cdate):
                break
            else:
                print('Invalid Date !!')
        while True:
            ttime = input('Enter time that will remind you (HH:MM)[ 24 Hours ] ?')
            if ValideteTime(ttime):
                break
            else:
                print('Invalid Time !!')
        TaskTime = returnFormatedTime(ttime)
        TaskDate = returnFormatedDate(tdate)
        task = Task(self.TaskId,CurrentTime,CurrentDate,TaskTime,TaskDate,TaskContent)
        self.Tasks.append(task)

        print('Task is Successfully Added!')
    def DeleteTask(self):
        if not self.Tasks:
            print('No Tasks are Added !!')
        else:
            while True:
                taskId = input('Enter Task Id do you want to Drop ?')
                if ValidateTaskId(taskId, self.TaskId):
                    taskId = int(taskId)
                    break
            for task in self.Tasks:
                if task.TaskId == taskId:
                    index = self.Tasks.index(task)
                    break
            self.Tasks.pop(index)
            print('Task is Successfully Deleted !!')
    def UpdateTask(self):
        if not self.Tasks:
            print('No Tasks are Added !!')
        else:
            while True:
                taskId = input('Enter Task Id do you want to modify ?')
                if ValidateTaskId(taskId, self.TaskId):
                    taskId = int(taskId)
                    break
            for task in self.Tasks:
                if task.TaskId == taskId:
                    while True:
                        tContent = input('Enter Your Task?')
                        if not tContent or tContent.isdigit():
                            print('integer not Allowed !!')
                        else:
                            task.TaskContent = tContent
                            break
            print(f'Task-{taskId} Successfully Updated !!')
    def DisplayAllTasks(self):
        if not self.Tasks:
            print('No Tasks are Added !!')
        for task in self.Tasks:
            TaskContent = PrintInOrder(task.TaskContent)

            print('┌───────────────────────────────────────────────┐\n'
                  f'│ Task - {task.TaskId}                                      │\n'
                  '│   ┌───────────────────────────────────────┐   │')
            print(TaskContent)
            print(f'│   │                         {task.TaskDate}   │   │\n'
                  f'│   │                            {task.TaskTime}   │   │\n'
                  '│   └───────────────────────────────────────┘   │\n'
                  f'│   Created on:                   {task.CurrentDate}   │\n'
                  f'│                                    {task.CurrentTime}   │\n'
                  '└───────────────────────────────────────────────┘')
class Main(ToDoList):
    def __init__(self):
        print('############## ToDoList Remainder ################')
    # It will return Current date && time in form of list and type(string)
    def CallFuniton(self,operation):
        match operation:
            case 1:
                self.AddTask()
            case 2:
                self.UpdateTask()
            case 3:
                self.DeleteTask()
            case 4:
                self.DisplayAllTasks()
            case 5:
                quit()
    # General function to call ToDolist functionalities
    def RunFunctions(self):
        while True:
            print('1.AddTask\n2.UpdateTask\n3.DeleteTask\n4.DisplayAllTasks\n5.Quit')
            while True:
                Operation = input('What do you want perform ?')
                if ValidateInput(Operation):
                    Operation = int(Operation)
                    break

            self.CallFuniton(Operation)

if __name__ == '__main__':
    main = Main()
    main.RunFunctions()

