#base image for linux distribution
FROM apline:3.1

#Update - add language
RUN apk add --update python3 py-pip3

#install app dependency
RUN pip install -r requirement.txt

#bundle app source
COPY simpleApp.py /src/simpleApp.py

#expose port and run coomand
EXPOSE 9000
CMD ["python", "/src/simpelApp.py", "-p 9000"]
