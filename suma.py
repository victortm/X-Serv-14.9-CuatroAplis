#!/usr/bin/python


class suma:

    def parse(self, request, rest):
        #try:
        num1 = int(rest.split("/")[1])
        num2 = int(rest.split("/")[2])
        #except ValueError:
         #   return ("HTTP/1.1 400 Bad Request\r\n\r\n" +
                  #  "<html><body>Input error</body></html>\r\n", rest.split("/")[0])
        return (num1, num2)

    def process(self, parsedRequest):
            add = parsedRequest[0] + parsedRequest[1]
            reply = "Solution: " + str(parsedRequest[0]) + 
                               " + " + str(parsedRequest[1]) + 
                               " = " + str(add)
           
            return ("200 OK", "<html><body>" + reply + "</body></html>\r\n")
