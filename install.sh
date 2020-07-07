sudo yum install git
sudo yum install python3
sudo git clone https://github.com/krishnasism/the-summary-project.git
cd the-summary-project
sudo python3 -m pip install -r requirements.txt 
sudo python3 -m pip install lxml
sudo python3 -m pip install -U scikit-learn
echo "import nltk \nnltk.download('all')" > install_nltk.py
sudo python3 install_nltk.py 
sudo python3 manage.py runserver 0.0.0.0:80
