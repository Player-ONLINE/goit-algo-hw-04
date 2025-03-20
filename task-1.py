info = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
"""

with open('demo_nom2.py', "w") as file:
    file.write(info)

def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, "r") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += float(salary)
                count += 1 

        average = total/count if count > 0 else 0
        return total, average
    
    except FileNotFoundError:  
        print("Takogo ne bachiv")
        return 0, 0
    
    except IOError:  
        print("Faily gapluk, gg")
        return 0, 0

            
total, average = total_salary("demo_nom2.py")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
 