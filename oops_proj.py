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
                              5.press any key to exit""" )
        if user_input=="1":
            pass
        elif user_input=="2":
            pass
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()



obj=messagebook()