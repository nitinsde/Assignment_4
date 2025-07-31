initial = input("Enter a text to write to the file: ")
try:
    with open("output.txt" , "w") as my_file:
        my_file.write(initial + "\n")
    print("Data successfully written to output.txt")
except Exception as e:
    print("Error writing to file" , e)

# Now for appending a data to our file
final = input("\n Enter additional text to append: ")      
try:
    with open("output.txt","a") as my_file:
        my_file.write(final + "\n" )
    print("Data successfully appended.")    
except Exception as e:
    print("Error appending to file.")

# Final Reading data
print("\nFinal content of output.txt")
try:
    with open("output.txt" ,"r" ) as my_file:
        data = my_file.read()
        print(data.strip())
except Exception as e:
    print("Error reading this file:",e)




