def chatbot():
    print("Hello! I'm your code alpha chatbot. How can I assist you today?")
    name = input("what is your name? ")
    while True:
        user = input("You: ")
        user = user.strip().lower()
        if user == "hello" or user == "hi":
            print(f"welcome to DANIEL'S CHATBOT! lets talk {name}.")
        elif user == "how are you?":
            print("i'm well, and you?")
        elif user == "i need your help":
            print("how can I help you?")
        elif user in ["mathematics", "science", "history", "geography", "literature"]:
            print("i cannot give subject or research related help. Although I am here to keep you entertained")
        elif user == "bye":
            print("sorry i cannot help, byee!")
            break
        else:
            print(f"I do not understand .{name}")
chatbot()
