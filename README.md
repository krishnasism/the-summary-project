# Minor Project for BCA 5th Semester

## Summarizer

A webapp which will make it easier for students to gather and learn vital information about a particular topic. The interface will allow the user to look for a topic and then return vital information present about it to the user. The aforementioned ‘vital information’ will be a summary that will be generated by a novel machine learning based summarizing algorithm, which will be easy to learn by the user due to the short length and the presence of less redundant information. Thus, allowing the user to understand a topic in a shorter time span, allowing him to retain the information more effectively, and allow the user to focus more on more tasks at hand.

## About the Algorithm
The algorithm is a novel cluster based summarization tool that was conceieved as a part of a research project. The paper was presented at the IEMIS 2018, organized by the School of Information Technology (Ashram Campus), a unit of Institute of Engineering & Management, Kolkata.

### Installing

### Prerequisites
Browse to the cloned directory.

```
cd minor-project
```
requirements.txt lists all the dependencies that need to get the project up and running on your local server
```
pip install -r requirements.txt
```
install lxml module
```
pip install lxml
```



## Running
Run the app
```
python manage.py runserver
```
```
System check identified no issues (0 silenced).
August 25, 2018 - 22:27:13
Django version 2.0.5, using settings 'Summary.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

If it runs properly, you will see the page on the local server IP that was assigned in the aforementioned step.
![summm](https://user-images.githubusercontent.com/21293324/44620713-da03da80-a8b6-11e8-8daf-844311183831.png)

### NOTE
You might face an Import Error.
This is caused by -> ImportError("cannot import name 'murmurhash3_32'",)

To resolve this, simply execute this command
```
pip install -U scikit-learn
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Anaconda](https://anaconda.org/) - IDE
* [Python](https://www.python.org/) - I don't need to explain why ☺

## Authors

* **Krishnasis Mandal**
