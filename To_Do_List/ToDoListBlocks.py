from datetime import datetime
def PrintInOrder(str):
    lst = []
    k = 0
    isFirstLine = True
    while True:
        row = ''
        i = 0
        if isFirstLine:
            row += '  ● '
            while i < 35 and k < len(str):
                row += str[k]
                k += 1
                i += 1
            while i < 35:
                row += ' '
                i += 1
            if i <= 35: lst.append(row)
            if k == len(str): break
            isFirstLine = False
        else:
            i = 0
            if str[k] == ' ':
                k += 1
            while i <= 38 and k < len(str):
                row += str[k]
                k += 1
                i += 1
            while i <= 38:
                row += ' '
                i += 1
            if i <= 39:lst.append(row)
            if k == len(str): break
    for i in range(len(lst)):
        if i != len(lst) - 1:
            lst[i] = '│   │' + lst[i]
            lst[i] = lst[i] + '│   │\n'
        else:
            lst[i] = '│   │' + lst[i]
            lst[i] = lst[i] + '│   │'
    TaskContent = ''.join(lst)
    return TaskContent
def ValidateInput(operation):
    if operation.isdigit():
        operation = int(operation)
        if 1<= operation <= 5:
            return True
        else:
            print('Please Enter a Valid Input')
    else:
        print('Charecters are not allowed.')

    return False
def returnFormatedTime(ttime):

    time = datetime.strptime(ttime,'%H:%M')
    meridian = time.strftime('%p')
    return time.strftime('%H')+':'+time.strftime('%M') + ' ' + meridian
# print(returnFormatedTime('1:5'))
def returnFormatedDate(tdate):
    date = datetime.strptime(tdate,'%d/%m/%Y')
    # %a for day_Name like 'Wed' and %A for full day name 'Wednesday'
    day_name = date.strftime('%a')
    # %b for month_Name like 'Jul' and %B for full Month name 'July'
    month_name = date.strftime('%b')
    # return Sat, Jul 27
    return day_name+', '+month_name+' '+date.strftime('%d')
def CurrentDateTime():
    now = datetime.now()
    return str(now.day)+'/'+str(now.month)+'/'+str(now.year),str(now.hour)+':'+str(now.minute)
def ValidateTaskId(taskId,totalTasks):

    if taskId.isdigit():
        taskId = int(taskId)
        if taskId <= totalTasks:
            return True
        else:
            print('Invalid Task Id !!')
    else:
        print('Characters are not allowed !!')
    return False
def ValideteDate(tdate_str,cdate_str,format_str = "%d/%m/%Y"):
    try:
        # it validate the given date if weather is it correct format then exception not Occurred
        tdate = datetime.strptime(tdate_str,format_str)
        cdate = datetime.strptime(cdate_str, format_str)
        if (tdate < cdate):
            print('You con not go past ',end='')
            return False
        return True
    except ValueError:
        # date not in correct format return false
        return False
def ValideteTime(time_str,format_str = '%H:%M'):
    try:
        # it validate the given time if weather is it correct format then exception not Occurred
        datetime.strptime(time_str,format_str)
        return True
    except ValueError:
        # time not in correct format return false
        return False
