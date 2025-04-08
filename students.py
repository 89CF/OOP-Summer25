students = [
{
 'first_name' : 'Mehmet',
'last_name' : 'Konmaz',
'index_number' : 'TR30011',
'nationality' : 'Turkey',
'starting_date' : '2024-11-01',
'courses' : ['Computer security', 'Match','Ethics']
},
{
 'first_name' : 'Berk',
'last_name' : 'Oldu',
'index_number' : 'TR2202',
'nationality' : 'Turkey',
'starting_date' : '2024-09-01',
'courses' : ['Computer Science', 'Match','Ethics']
},
{
 'first_name' : 'Ata',
'last_name' : 'Ucmaz',
'index_number' : 'TR32551',
'nationality' : 'Turkey',
'starting_date' : '2024-01-01',
'courses' : ['English', 'Match','Ethics']
}
]

def add_student():
    """Adds a new student"""
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    index_number = input("Enter student's index number: ")
    nationality = input("Enter student's nationality: ")
    starting_date = input("Enter starting date (YYYY-MM-DD): ")
    courses = input("Enter courses (comma-separated): ").split(',')
    courses = [course.strip() for course in courses]

    students.append({
        'first_name': first_name,
        'last_name': last_name,
        'index_number': index_number,
        'nationality': nationality,
        'starting_date': starting_date,
        'courses': courses
    })
    print(f"Student {first_name} {last_name} added successfully.")

def display_students():
    """Displays all students in the list."""
    print("\nCurrent Students:")
    for student in students:
        print(f"Name: {student['first_name']} {student['last_name']}, Index: {student['index_number']}")
