# Python Online Judge(POJ)

## Usage

### Solve a random picked problem
- ./poj new
- vim answer.py
- ./poj submit

### Solve a specific problem
- ./poj new -n <problem_name>
- vim answer.py
- ./poj submit

### Check submit log
- ls log/
- cat log/stats.yaml

### Clean submit log
- ./poj clean

### Add a quesiont
- cd questions
- mkdir <question_name>
- follow sample question test, script.py for UT, answer.py as a sample answer
- question_name starts with #, means it won't be chosen with "./poj new"

### Check the sample answer under question dir
- ./poj sanity
- ./poj sanity -n <question_name>