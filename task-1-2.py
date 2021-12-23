seconds_input = int(input("Введите время в секундах >>> "))
hour = seconds_input // 3600
minutes = (seconds_input % 3600) // 60
seconds = (seconds_input % 3600) % 60
print(f"{str(hour).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
