import csv

print("Monthly Sales program\n")
print("COMMAND MENU")
print("monthly - View  monthly sales")
print("yearly  - View yearly summary") 
print("edit    - Edit sales for a month")
print("exit    - Exit program")


while(True):
    dataSale = []
    with open("../data/monthly_sales.csv", mode = "r", newline="") as Sales:
        reader = csv.reader(Sales)
        for row in reader:
            dataSale.append(row)
    Sales.close()       
    command = input("\nCommand: ")
    if command.lower() == "monthly":
        for row in dataSale:
            print(f"{row[0]} - {row[1]}")
    if command.lower() == "yearly":
        sum =0
        average=0
        for row in dataSale:
            sum = sum + int(row[1])
        average = sum/12.
        print(f"Yearly total:\t", (f"{str(sum)}"))
        print("Monthly average:", (str(round(average,2))))

      
    if command.lower() == "edit":
        monthlySales = []
        for month in dataSale:
            monthlySales.append(month[0])
        userEdit1 = input("Three-letter Month: ")
        if userEdit1 in monthlySales:
             editSale = int(input("Sale amount: "))
             for x in dataSale:
                 if x[0] == userEdit1:
                        x[1] = editSale
                        with open("../data/monthly_sales.csv", mode ="w", newline= "")as rewrite:
                            y = csv.writer(rewrite)
                            y.writerows(dataSale)
                        rewrite.close()
                        
        else:
            print("Invalid three-letter month.")

    if command.lower() == "exit":
        print("Bye!")
        break;

                        
             

              

                   
            
            

            
            
        
    
                
