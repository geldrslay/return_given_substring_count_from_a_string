# Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

# Defining function 
def count_substring (statement):
    # Display the given statement 
    print ("The given string is:", statement)
    # Determine the count of the given substring
    count = 0
    for i in range (len(statement)):
        count += statement [i:i+4] == "Emma"
    return count

# Determine and display count of the given substring from main string 
emma_count = count_substring("Emma is good developer. Emma is a writer")
print ("The word 'Emma' appeared", emma_count, "times.")