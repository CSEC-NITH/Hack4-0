# Statistical-Data-Analysis
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/raman08/Statistical-Data-Analysis)


This Project Help Students to analyze their progress concerning its class. This contains four main components:

1. Dot graph to compare its progress concerning the class.
2. Comparison of its CGPA with class Average CGPA.
3. Frequency distribution of Class scoring different CGPA.
4. Pie chart showing whole class performance




# Usage
This uses python3 as the main language and uses MySQL as a database.

You need to require both of them to run the project.


First, u need to install the requirements required for this project via pip
(Use the virtual environment in the project folder)

```
git clone https://github.com/raman08/Statistical-Data-Analysis.git
cd  Statistical-Data-Analysis

# Creating a virtual environment and activated it

python3 -m venv venv
source venv/bin/activate
```

```
# Installing Requirments

pip install -r requirments.txt

```

Also, you need to create the database of your class by using tableCreator.py

Change the information where it is written change it

To create tables first create a database named STASTISTICAL_DATA_ANALYSIS in your MySQL server and then run the tableCreator.py
```
# Creating a database in MySQL

mysql> create database STASTISTICAL_DATA_ANALYSIS;
mysql> use STASTISTICAL_DATA_ANALYSIS;


```


```
# using tableCreator.py to create the table

python3 tableCreator.py

```


```

# using the graphmaker file to see your performance

python3 graphmaker.py

```

Now just enter your Rollo and your progress is displayed

### Contact / Social Media

[![Github](https://raw.githubusercontent.com/srbcheema1/CheemaFy/master/myPlugins/extra_things/png_images/social/github.png)](https://github.com/raman08/)
[![LinkedIn](https://raw.githubusercontent.com/srbcheema1/CheemaFy/master/myPlugins/extra_things/png_images/social/linkedin-48x48.png)](https://www.linkedin.com/in/raman-preet-singh-314206195/)

## Contributors

1. Anurag Verma 
2. Ishan Aggarwal 

### Special Thanks 

Special Thanks to [Srb Cheema](https://github.com/srbcheema1/) for giving the Nith result JSON files.