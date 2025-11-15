import os

ctx = input("Enter commit message: ")

os.system("git add .")
os.system(f'git commit -m "{ctx}"')
os.system("git push origin main")

print("Changes Have Been Commited!")