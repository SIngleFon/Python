from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []

def check_int(msg):
    while True:
        try:
            return int(input(msg))
        except (TypeError,ValueError):
            print("Error, you did not enter a number")

def show_all():
    if all_data:
        print("------------",*all_data,"------------", sep="\n")
    else:
        print("Empty data")

def check_record(string):
    global all_data
    baby = string.split(" ")
    test = []
    for i in range(4):
        copy = all_data[i][1:].split()
        count = 0
        for j in range(4):
            
            if baby[j].lower() in copy[j].lower():
                count += 1
        test.append(count)
    if max(test) == 4 or set(baby) == " ":
        return False
    else: return True

def add_new_contact():
    global last_id
    array = ["surname", "name", "patronymic", "phone_number"]
    string = ""
    for i in array:
        string += input(f"Enter {i} ") + " "
    last_id += 1  
    if string == "    ":
        print("Вы ничего не ввели")
    else:
        if check_record(string) == True:
            with open(file_base, "a", encoding="utf-8") as f:
                f.write(f"{last_id} {string}\n")
            print(f"==============\n"
                  "Контакт успешно добавлен!")
        else:
            print(f"==============\n"
                    "Такой контакт уже есть, Либо вы ничего не ввели")

            

def search_record():
    search = input("Search: ").lower()
    list = []
    for i in range(last_id):
        try:
            for j in all_data[i]:
                if search in all_data[i].lower():
                    list.append(all_data[i])
                break
        except IndexError:
            pass
    print("------------",*list,"------------", sep="\n")


def change_record():
    delete_record(id)
    add_new_contact()

def delete_record(id):
    global last_id, all_data
    search_record()
    while True:
        # id = int(input("Select and write id to change/remove: "))
        id = check_int("Select and write id to change/remove: ")
        if id > len(all_data):
            print("Error, enter the correct ID")
        else:
            break
    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
    with open(file_base,"w", encoding="utf-8") as f:
        for line in all_data:
            if line.strip("\n") != all_data[id - 1]:
                f.write(f"{line}\n")
    last_id -= 1


def change_id_records():
    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
    with open(file_base,"w", encoding="utf-8") as f:
        i = 1
        for line in all_data:
            line = line[:0] + str(i) + line[1:]
            i += 1
            f.write(f"{line}\n")
            

def export_import():
    global all_data, last_id
    UserKey = int(input("Import(0)\n" 
                        "Export(1)\n"
                        "You're choice: "))
    match UserKey:
        case 1:
            export_record()
        case 0:
            import_record()
        case _:
            print("Try again!\n")    

def export_record():
    new_file_name = input("Write name new file: ") + ".txt"
    if not path.exists(new_file_name):
        with open(new_file_name, "a+", encoding="utf-8") as f:
            for line in all_data:
                f.write(f"{line}\n")
    else: 
        with open(new_file_name, "w", encoding="utf-8") as f:
            for line in all_data:
                f.write(f"{line}\n")

def import_record():
    file_name_import = input("Write name importing file: ") + ".txt"
    if not path.exists(file_name_import):
        print("File not matched\n"
            "Try Again!")
    copy_data = []
    with open(file_name_import, encoding="utf-8") as f:
        copy_data = [i.strip() for i in f]
    all_data = all_data + copy_data
    print(all_data)
    with open(file_base, "a", encoding="utf-8") as f:
        for line in copy_data:
            f.write(f"{line}\n")

def main_menu():
    play = True
    while play:
        change_id_records()
        read_records()
        answer = input("==============\n"
                        "Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n"
                       "==============\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_record()
            case "4":
                change_record()
            case "5":
                delete_record(id = None)
            case "6":
                export_import()
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()
