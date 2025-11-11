import findTemperatureLive
import sentence

def createHomePage(emailuser):
    firstname, lastname = emailuser.split(".")
    firstname = firstname.capitalize()
    lastname = lastname.capitalize()
    filename = f"{emailuser}.html"
    
    with open(filename, 'w') as file:
        file.write("<!DOCTYPE html>\n")
        file.write("<html>\n")
        file.write("<head>\n")
        file.write(f"<title>Simon's Home Page</title>\n")
        file.write("</head>\n")
        file.write("<body>\n")
        file.write(f"<h3>Welcome to Simon Land</h3>\n")
        file.write(f"<p>This is a picture of The Simon Voyer</p>\n")
        file.write(f"<img src='Simon.Voyer.jpg'/>\n")
        temp = findTemperatureLive.findTemperatureLive()
        file.write(f"<p>Temperature in Boston is {temp} degrees.</p>\n")
        sent = sentence.sentence()
        file.write(f"<p>{sent}.</p>\n")
        file.write("</body>\n")
        file.write("</html>")       
    
if __name__ == "__main__":
    createHomePage("Simon.Voyer")

    


