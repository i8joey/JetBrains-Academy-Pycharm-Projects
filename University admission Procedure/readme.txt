Retrieves students test scores, and their choices of departments in order from first to third.
The list of students are ranked by their choice of department and test scores
eg. Natha Keefe 71 (Physics test) 67 (Chemistry Test) 53 (Math Test) 60 (Computer Science Test) 31 (Admission Exam Score) Engineering (First choice) Biotech Chemistry
Department picking order - Biotech, chemistry, engineering, mathematics, and physics 

Tests used to rank students - physics and math for the Physics department, chemistry for the Chemistry department, 
math for the Mathematics department, computer science and math for the Engineering Department, chemistry and physics for the Biotech department

If a department requires more than 1 test, the tests are averaged.
Then the students are sorted by their average score or their admission exam score, whichever is higher

The program takes an input int() to decide the size of each department
Then sorts the students into their respective departments, if department is full then it will sort them into the department of their second/third choice 
depending on the capacity
