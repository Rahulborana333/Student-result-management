#!/usr/bin/env python3
students = [
    {"id": 1, "name": "Rahul", "age": 21, "marks": 78},
    {"id": 2, "name": "Priya", "age": 22, "marks": 85},
    {"id": 3, "name": "Amit", "age": 20, "marks": 92},
    {"id": 4, "name": "Neha", "age": 23, "marks": 67 },
    {"id": 5, "name": "Sahil", "age": 21, "marks": 81},
]

def menu():
    print("student result management")
    print("1.add student")
    print("2.all data")
    print("3.update marks")
    print("4.search student")
    print("5.delete by id")
    print("6.show topper fail/pass count")
    print("7.show rank")
    print("8.write to text file")
    print("9.exit")



def add_student(students):
    id=int(input("enter student id :"))
    name=input("enter student name for add :")
    marks=int(input(f"enter student {name} marks :"))
    age=int(input(f"enter age of student {name} :"))
    for data in students:
        if data["name"]==name and data["id"]==id:
            print(f"student {name} already present in data")
            return
    else:
        students.append({"id":id,"name":name,"age":age,"marks":marks})
        

def all_data(students):
    for data in students:
        print(f"📉{data}")

def update_mark(students):
    name=input("enter student name for mark update :")
    mark=int(input("enter mark for update"))
    for d in students:
        if d["name"].lower()==name:
            d["marks"]=mark
            print("{name} mark updated succesfully")
            return 
    else:
        print("student data not found")

def search_student(students):
    name=input("enter student name for search")
    for d in students:
        if d["name"].lower()==name:
            print(d)
            return
    else:
        print("student not found")

def delete_data(students):
    id=int(input("enter student id for remove :"))
    for d in students:
        if d["id"]==id:
            students.remove(d)
            print(f"{id} student removed successfully")
            return
    else:
        print(f"{id} student data not found")

def show_result(students):
    topper=max(students,key=lambda x:x["marks"])
    fail=sum(1 for d in students if d["marks"]<70)
    passsed=sum(1 for d in students if d["marks"]>=70)
    print("topper :",topper)
    print("no of fail student :",fail,"number of pass student :",passsed)


def rank(students):
    sorted_data=sorted(students,key=lambda x:x["marks"],reverse= True)
    for i,d in enumerate(sorted_data,start=1):
        d["rank"]=i
    print("!top ranker!")
    for i in range(3):
        print(f"rank {i+1} :{sorted_data[i]}")

def export(student):
    if not student:
        print("student list is empty")
    else:
        with open("student.txt","w")as file:
            for d in student:
                file.write(f"id: {d["id"]} | Name: {d["name"]} | Age: {d["age"]} | Marks : {d["marks"]}\n")

def main():
    while True:
        menu()
        choice=int(input("enter your choice :"))
        
        if choice==1:
            add_student(students)
        elif choice==2:
            all_data(students)
        elif choice==3:
            update_mark(students)
        elif choice==4:
            search_student(students)
        elif choice==5:
            delete_data(students)
        elif choice==6:
            show_result(students)
        elif choice==7:
            rank(students)
        elif choice==8:
            export(students)
        elif choice==9:
            print("exiting system")
            break
        else:
            print("invalid choice")
main()

