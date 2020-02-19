import mysql.connector as sql
import numpy as np
import matplotlib.pyplot as plt  
 
################################################# Connecting to SQL Server ##################################################################

conn = sql.connect(host='localhost',database='STASTISTICAL_DATA_ANALYSIS',user='root',password='Raman@08')

if conn.is_connected():
	print("Connected to MySql Server")

cursor = conn.cursor()

out7 = []
out1 = []

cursor.execute("Select RollNo from CSE_Dual_2019 where Cgpi >= 3;")
a = cursor.fetchall()

out1 = [item for i in a for item in i]

for i in out1:
	out7 = out7 + [int(i)%100]
	
out7=np.array(out7) 

##############################################################     Dynamic input ##################################################################

roll_1=[]

roll = input("Enter:")
cursor.execute(f"select Cgpi from CSE_Dual_2019 where Rollno = {roll};")

roll_1.append(roll)

roll_1=np.array(roll_1)

a = cursor.fetchall()

cgpa_entered = [item for i in a for item in i]

cgpa_entered[0] = float(cgpa_entered[0])


cgpa_entered = np.array(cgpa_entered)

cursor.execute(f"select Name from CSE_Dual_2019 where Rollno = {roll};")
z = cursor.fetchall()

name_entered = [item for i in z for item in i]

name_entered = np.array(name_entered)

cursor.execute("Select Cgpi from CSE_Dual_2019 where Cgpi >= 3;")
b = cursor.fetchall()

out2 = []

out2 = [item for i in b for item in i]

out2 = np.array(out2)

out3 = []
for i in out2:
	out3 = out3+[float(i)]


cursor.execute("Select RollNo from CSE_Dual_2019 where Cgpi < 3;")
c = cursor.fetchall()

out4 = [item for i in c for item in i]

cursor.execute("Select Cgpi from CSE_Dual_2019 where Cgpi < 3;")
d = cursor.fetchall()

out5= [item for i in d for item in i]

out6 = []

for i in out5:
	out6 = out6+[float(i)]


###################################################### Details of Student With Respect TO Class ###############################################################
demo=[]                                     #pass roll number in str
for i in out1:
	demo=demo+[str(int(i)%100)]

demo_1=[]
for i in out4:
	demo_1=demo_1+[str(int(i)%100)]

demo=np.array(demo)
demo_1=np.array(demo_1)

demo_fail=[]

net=[]
net=out3+out6


out3 = np.array(out3)

student_name_pass=demo
student_name_pass=student_name_pass[::-1]

student_cgpa_pass=out3
student_cgpa_pass=student_cgpa_pass[::-1]

plt.xlabel(" Rollnumber of Student ")
plt.ylabel(" CGPA of each student  ")
plt.title(" Data Analysis ")
plt.ylim(0,11)
plt.plot(student_name_pass,student_cgpa_pass,color="orange",label='Student pass',linestyle='dashed',marker='o',markerfacecolor='red',markersize=12)
plt.plot(demo_1,out6,color='black',label='student fail',linestyle='dashed',marker='o',markerfacecolor='grey',markersize=10)
plt.plot(roll_1,cgpa_entered,color='purple',label=(f'Name:{name_entered[0]}, Roll number:{roll_1[0]}, CGPA:{cgpa_entered[0]}'),marker='o',markerfacecolor='green',markersize=14)
plt.legend()
plt.show()

#################################################         CLASS AVRAGE VS YOUR CGPA    ################################################################

student_name_pass=out1
student_cgpa_pass=out3
average_of_all_pass_students=0
for i in student_cgpa_pass:
	average_of_all_pass_students=i+average_of_all_pass_students


av=average_of_all_pass_students/len(student_cgpa_pass)

height= [av,cgpa_entered]   
left=[1,5]
tick_label=[f'Average of all students\n{av}',f'Name:{name_entered[0]}\nroll number:{roll_1[0]}\nCGPA:{cgpa_entered[0]}']
plt.xlabel(" STUDENTS     DETAILS")
plt.ylabel(" CGPA   ")
plt.title(" Data Analysis ")
plt.ylim(0,11)
plt.xlim(0,9)
plt.bar(left,height,tick_label=tick_label,width=0.4,color=['orange','green'])
plt.show()



#####################################################################################   FREQUENCY OF STUDENTS  #############################################################################################################################3

net1=[]
for i in net:
	net1=net1+[int(i)]

li=0   # 10
li1=0 # 9-10
li2=0 # 8-9
li3=0 # 7-8
li4=0 # 6-7
li5=0 # 5-6
li6=0 # 4-5
li7=0 #3-4
li8=0 #2-3
li9=0 #1-2
li10=0 #0-1
for i in net1:
    if i==10:
        li+=1
    if i>=9 and i<10:
        li1+=1
    if i>=8 and i<9:
        li2+=1
    if i>=7 and i<8:
        li3+=1
    if i>=6 and i<7:
        li4+=1
    if i>=5 and i<6:
        li5+=1
    if i>=4 and i<5:
        li6+=1
    if i>=3 and i<4:
    	li7+=1    
    if i>=2 and i<3:
    	li8+=1
    if i>=1 and i<2:
    	li9+=1
    if i>=0 and i<1:
    	li10+=1	

	    
left=[1,2,3,4,5,6,7,8,9,10,11]
tick_label=['10','9-10','8-9','7-8','6-7','5-6','4-5','3-4','2-3','1-2','1-0']
height=[li,li1,li2,li3,li4,li5,li6,li7,li8,li9,li10]
plt.xlabel('CGPA range')
plt.ylabel('Number of students lying in given CGPA range')
plt.title('Frequency of CGPA')
plt.bar(left,height,tick_label=tick_label,width=0.6,color=['red','purple'])
plt.show()



############################################################   Pie Chart  of Class  #########################################################

activities=['Top-10','Below -average','Above-average','Fail']
student_cgpa_pass=np.sort(student_cgpa_pass)
student_cgpa_pass=student_cgpa_pass[: : -1]
sum_1=0

for i in range(10):
    sum_1=student_cgpa_pass[i]+sum_1

total_average=0
for i in student_cgpa_pass:
    total_average=total_average+i
total_average=total_average/len(student_cgpa_pass) 

sum_2=0
sum_3=0
sum_4=0

for i in student_cgpa_pass:
    if i<sum_1/10 and i>total_average:
        sum_2=sum_2+i
    if i<total_average and i>3:
        sum_3=sum_3+i
    if i<3:
        sum_4=sum_4+i

sum_1=(sum_1/(sum_1+sum_2+sum_3+sum_4))*100   
sum_2=(sum_2/(sum_1+sum_2+sum_3+sum_4))*100
sum_3=(sum_3/(sum_1+sum_2+sum_3+sum_4))*100
sum_4=(sum_4/(sum_1+sum_2+sum_3+sum_4))*100

###############   parts  #############

sum_1=sum_1*(0.24)

sum_2=sum_2*(0.24)

sum_3=sum_3*(0.24)

sum_4=sum_4*(0.24)

activities=['top ten','above average','below average']

slices=[sum_1,sum_2,sum_3]

colors=['r','y','g']

plt.pie(slices,labels=activities,colors=colors,startangle=90,shadow=True,explode=[0.3,0,0],radius=1.2,autopct='%1.1f%%')
plt.legend()
plt.show()