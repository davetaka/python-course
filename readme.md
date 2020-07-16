# Python for beginners
  
the content is from Programming with Mosh [here](https://www.youtube.com/watch?v=_uQrJ0TkZlc)  
  
begin with install python with package manager  
```console
$ sudo apt-get python
```
  
i'm using python 3.8 and visual studio code  
  
i've installed python extension from vscode and pylint  
  
   
### notes
* can multiply strings like 'a' * 3 == 'aaa'  
* recommended snake case for variables like first_name
* True/False with uppercase first letter
* float for numbers with decimal places
* three quotes (""") for string like @" in C#
* (//) division operator to get integer part like floor
* a module is a separate file with some reusable code, to organizing code in different files
* [math module used in course](https://docs.python.org/3/library/math.html)
* else if = elif
* basically "then" keyword or the open "{" in python is ":" (this note will help me to remember)
* unfortunately the logical operators' syntax remembers me of asp 3.0, microsoft's classical asp
* exists an else in while loop that will be executed only when the while loop reach all executions without a break
* tuples are immutable in python
* dictionary is the variable form of classes (with json format)
* by default python return None (it's a type like null)
* UpperCamelCase for classes
* python doesn't accept empty class, there's a keyword to accept, "pass" keyword
* modules built in python [here](https://docs.python.org/3/py-modindex.html)


### steps for machine learning
1. import the data
2. clean the data
3. split the data into training/test sets
4. create a model
5. train the model
6. make predictions
7. evaluate and improve

### notes for ml
* libraries like: 
- numpy - provides multi-dimensional arrays
- pandas - provides data frame (like excel spreadsheet)
- matPlotLib - two dimensional plotting library for graph plots
- scikit-learn - it has most used and common algorithms
* IDE for ML = Jupyter, built over anaconda
* jupyter notebook starts notebook server
* kaggle site for download real data for tests

### notes for django
* it's using django version 2.1.5 because 2.1.0 have a problem with an old table in sqlite
* in the course video doesn't have instructions with django 3, so i followed with version 2