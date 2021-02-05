


print("reboot the computer and try to connect ")
condition = input("did that fix the problem ").strip().lower()


if not condition == "yes":

    print("reboot the computer and try to connect ")

    condition = input("did that fixed the problem ").strip().lower()

    if not condition == "yes":
        print("make sure the cables between the router and modem aare plugged in firmly")

        condition = input("did that fixed the problem ").strip().lower()
    
        if not condition == "yes":
            print("move the router to a new location and ty to connect")

            condition = input("did that fixed the problems ").strip().lower()

            if not condition == "yes":

              print("get a new router")
            
            else:
              print("the problem solved".title())

        else:
          print("the problem solved")
    else:

      print("the problem solved")
            

else:

    print("the problem solved ")


