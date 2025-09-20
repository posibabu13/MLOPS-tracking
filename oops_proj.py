class messagebook:

    def __init__(self):
        self.username=''
        self.password='' 
        self.loggedin=False
        self.menu()

    
    def menu(self):
        user_input=input("""" This code will give the options to the user like
                              1.To signup
                              2.To signin
                              3.write a post
                              4.message a friend
                              5.press any key to exit:  press your value ---> """ )
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.sendmessage()
        else:
            exit()


    def signup(self):
        email=input("Enter your email id: ")
        pwd=input("Enter your password to login: ")
        self.username=email
        self.password=pwd
        print("\n")
        print("You have signed up successfully!! ")
        self.menu()

    def signin(self):

        if self.username=="" and self.password=="":
            print("please sign in with your credintials")
    
        else:
                uname=input("Enter your email id: ")
                pswd=input("Enter your password to login: ")

                if self.username==uname and self.password==pswd:

                    print("You have signed in sucessfully")
                    self.loggedin=True
                else:
                    print("please input your credintials : ")

        print("\n")
        self.menu()


    def my_post(self):
        if self.loggedin==True:
            txt=input("Enter your post here:")
            print(f"Your content has been posted {txt}")
        else:
            print("You need to sign to post something")

        print("\n")
        self.menu()

    def sendmessage(self):
        if self.loggedin==True:
            txt=input("Enter your message here :")
            frnd=input("whom to send the message ?")
            print(f"the message has been delivered to {frnd}")
        else:
            print("You need to sign in first to post something")
        
        print("\n")
        self.menu()

obj=messagebook()