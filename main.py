import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('OBE.xlsx')

print('\nCourse Record:\n')
print(df.set_index(keys='ID').to_string())

grades = ['A','B+','B','C+','C','D+','D','F']
grade_counts = [0 for _ in range (0,len(grades))]

for i,row in df.iterrows():
        if row['Grade'] == 'A':
                grade_counts[0] =  grade_counts[0] + 1
        elif row['Grade'] == 'B+':
                grade_counts[1] =  grade_counts[1] + 1
        elif row['Grade'] == 'B':
                grade_counts[2] =  grade_counts[2] + 1
        elif row['Grade'] == 'C+':
                grade_counts[3] =  grade_counts[3] + 1
        elif row['Grade'] == 'C':
                grade_counts[4] =  grade_counts[4] + 1
        elif row['Grade'] == 'D+':
                grade_counts[5] =  grade_counts[5] + 1
        elif row['Grade'] == 'D':
                grade_counts[6] =  grade_counts[6] + 1
        else:
                grade_counts[7] =  grade_counts[7] + 1

#Grade Distribution
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.title('Grade Distribution')
plt.bar( x=grades, height=grade_counts  , width=1.0, color='yellow' , edgecolor='red' )
plt.savefig('grade_dist.png',dpi=400)
plt.close()

#Score Distribution
students = df['Name'].tolist()
for i,name in enumerate(students):
    last_name = name.split(' ',1)
    if len(last_name) > 1:
        students[i] = last_name[1]
    else:
        students[i] = last_name[0]

scores   = df['Total'].tolist()
positions = [2*i for i in range(0,len(students))]

plt.xlabel('Student')
plt.ylabel('Score')
plt.title('Score Distribution')
plt.xticks(ticks=positions,labels=students,rotation=0, ha="center")
plt.bar(positions, scores , width=1.0 , color='yellow' , edgecolor='red')
plt.savefig('score_dist.png',dpi=400)
plt.close()


