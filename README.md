# Automata Project - README (អត់អានអត់ទៅ lolz)
**Intergrated with tailwindcss** <br/>

Is it your first time in Flask? to start implement this project you need to follow the steps below in order to initial your project directory.
## 1. Install Python (3.11.12)
For **Linux** user please follow the step below, for **Windows** or **macOS** please follow the official [document here](https://www.python.org/downloads/)
To install from official repository:
```
sudo apt update && sudo apt upgrade -y
```
```
sudo apt install python3
```
To check your installed python3:
```
python3 --version
```
## 2. Install flask
### 2.1 Set up python virtual environtment for project
#### macOS/Linux
```
$ mkdir myproject
$ cd myproject
$ python3 -m venv automata_venv
```
#### Windows
```
> mkdir automata_project
> cd automata_project
> py -3 -m venv automata_venv
```
### 2.2 Activate the envoironment
#### macOS/Linux
```
$ . automata_venv/bin/activate
```
#### Windows
```
> automata_venv\Scripts\activate
```
When your environment is activated you will see your environment name surrounded by parentheses before your current location in terminal like this:
`
(automata_venv) rayranger@rayranger:~/Desktop/automata_project$
`

***Note: Always activate your environment whenever you start doing the project to prevent package lost.***
## 3. Clone project
(You are now should be in automata_project directory)
```
git clone https://github.com/channudam2002/automata_project.git
cd automata_project
code .
```

## 4. Installing packages
Before you start application or implement it, please install the packages from package.json and requirements.txt
```
npm i
pip3 install -r requirements.txt
```
## 5. Running application
Please run two different commands below with separate terminal. 
### 5.1 Watch tailwind css style
```
npm run watch
```
### 5.2 Start application 
```
python3 run.py
```

















