import  csv
with open('emp_data.csv','w',newline="")as csvfile:
    header=["emp_id",'name',"department","place","salary"]
    csv_writter=csv.DictWriter(csvfile,fieldnames=header)
    csv_writter.writeheader()