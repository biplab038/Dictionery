#Python exercise 1 tutorial, we have to create a dictionary similar to the real-world dictionary.
# There is no limit to the definition you provide to any word, as this exercise is just for your practice.
# The details and functionalities that are essential and must be present are:
# The user will give the word as input.
# Suppose that the word is present in your dictionary along with its definition or meaning.
# The program will print the meaning or definition of that word.

dict={}

print("Indian Dictionery")
n1=str(input("Enter word\n"))
# print(dict[n1])
if n1 in dict:
      print(dict[n1])
else:
      f=open("data1.txt","a")
      f.write(n1)
      f.write("\n")
      print("We Updated our dictionery as soon as poosible!")
