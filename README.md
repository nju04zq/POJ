# Python Online Judge(POJ)

## Usage

### Solve a random picked question
- ./poj new
- vim answer.py
- ./poj submit

### Solve a specific question
- ./poj new -n <question\_name>
- vim answer.py
- ./poj submit

### Check submit log
- ls log/
- cat log/stats.yaml

### Clean submit log
- ./poj clean -n <question\_name>

### Add a question
- cd questions
- mkdir <question\_name>
- follow sample question test, script.py for UT, answer.py as a sample answer
- question\_name starts with #, means it won't be chosen with "./poj new"

### Verify the sample answer under question dir
- ./poj sanity
- ./poj sanity -n <question\_name>
