my_dict = {
  "students": [
    {"id": 20, "name": "Giorgi", "age": 25},
    {"id": 25, "name": "Giorgi", "age": 23},
    {"id": 100, "name": "Nika", "age": 22},
    {"id": 56, "name": "Nika", "age": 25},
    {"id": 1232, "name": "Dato", "age": 22},
    {"id": 846723, "name": "Archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
  ]
}


students_id =  []
for student in my_dict.get('students'):
    students_id.append(student['id'])

print("students_id: ", end="")
print(*students_id, sep=", ")

id = input("Choose Id: ")
if id == "" or not id.isdigit() or int(id) not in students_id:
    print(f"\nStudents with ID '{id}' not found. Try again...\n")
else:
    id = int(id)
    print("\nStudent info:")
    for student in my_dict.get('students'):
        if id == student['id']:
            print(f"ID: {student['id']}, Name: {student['name']}, age: {student['age']}")

        for grade in my_dict.get('subjects'):
            print(f"Subject: {grade['name']}, Grade: {grade['grades'][str(id)]}")
        
        break

