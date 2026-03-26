'''WAP to find out whether a given post is tal;king about 
"Ritesh" or Not '''
post = input("Enter the post: ")

if("Ritesh".lower() in post.lower()):
    print("This post is talking about Ritesh")
else:
    print("This post is not talking about Ritesh")