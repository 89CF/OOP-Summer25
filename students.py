students = [{
 'first_name' = 'Mehmet',
'last_name' = 'Konmaz',
'index_number' = 'TR30011',
'nationality' = 'Turkey',
'starting_date' = '2024-11-01',
'courses' = ['Computer security', 'Match','Ethics']
},
{
 'first_name' = 'Berk',
'last_name' = 'Oldu',
'index_number' = 'TR2202',
'nationality' = 'Turkey',
'starting_date' = '2024-09-01',
'courses' = ['Computer Science', 'Match','Ethics']
},
{
 'first_name' = 'Ata',
'last_name' = 'Ucmaz',
'index_number' = 'TR32551',
'nationality' = 'Turkey',
'starting_date' = '2024-01-01',
'courses' = ['English', 'Match','Ethics']
}
]

for student in students:
print(f"Student Name:
{student['first_name']}
{student['last_name']}
{student['index_number']}
)
