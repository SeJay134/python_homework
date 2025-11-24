import traceback

try:
    with open('diary.txt', 'a') as file:
        # Сначала задаём первый вопрос вне цикла
        answer_user = input("What happened today? ")
        file.write(answer_user + '\n')

        # Цикл для всех последующих вопросов
        while True:
            answer_user = input("What else? ")
            file.write(answer_user + '\n')
            
            if answer_user == "done for now":
                break

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")