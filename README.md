# This is the README for the CI/CD project

Hello there! This is my repository practice and showcase some of the CI/CD that I have learnt in the **DevOps** course I'm currently in.<br>

Here's the bit about Continuous Deployment using docker.
With your VM or local machine, execute these commands to run the python script that will give you the prices of STI, AAPL and Gold.

First, clone this repository into your preferred directory and change directory into the cloned folder
```
git clone https://github.com/hajimss/CI-CD-Project.git
```
```
cd CI-CD-Project
```

```
docker build -t "app" .
```

```
docker run -ti app
```

