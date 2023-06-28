# Step 1:
FROM python:3.9

# Step 2 : Package Install
RUN apt -y update && apt -y upgrade && apt -y install git net-tools vim

# Step 3 : Specify a working directory
WORKDIR '/root'

# Step 4 : Config file copy
COPY .bashrc .
COPY .exrc .
COPY hello.py .

# Step 5 : install bottle
RUN pip install bottle

# Step 6 : open port
EXPOSE 8000

# Step 7 : Execution Program
CMD ["python", "hello.py"]
