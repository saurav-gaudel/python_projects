def split_expenses(total_expenses:float, number_of_people:int, currency:str):

    if number_of_people<1:
        print("Number of person should be greater than one..")

    share_per_person:float= total_expenses/number_of_people
    print("----------------------------------------------------")
    print(f"total expenses is {currency}{total_expenses:,.2f}")
    print(f"Number of people to split money: {number_of_people}")
    print(f"Each person should pay: {currency}{share_per_person:,.2f}")
    print("----------------------------------------------------")


def unequal_share(n,splits:list,total_expenses,currency:str):
   
    for i, split in enumerate(splits):
        share = total_expenses * (split / 100)
        print(f"Person {i + 1} should pay: {currency}{share:,.2f}") 

    

def main()->None:
    try:
        ask= input("do every one in group should share equally:")
        if (ask.lower()=='yes'):
            total_expenses:float= float(input("Enter total Expenses: "))
            number_of_people:int= int(input("Enter number of people to whome money is to be splitted:"))
            split_expenses(total_expenses,number_of_people,currency='NRS.')
        else:
             n=float(input("Enter number of people:"))
             splits = input("Enter the splits as percentages (e.g., 20,40,40): ").split(',')
             splits = [float(split) for split in splits]  # to convert string to float using list comprehention
             total_expenses:float= float(input("Enter total Expenses: "))
             unequal_share(n,splits,total_expenses,currency="NRS.")
             split_expenses(total_expenses,number_of_people,currency='NRS.')

    except ValueError as e:
        print(f"Error{e}")
    

if __name__=="__main__":
    main()
# Edit the script to give the user the option to enter uneven splits, such as 20%, 40%, 40%.