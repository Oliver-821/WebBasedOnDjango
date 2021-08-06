# WebBasedOnDjango

django==2.1.5
Python==3.7.5

​	git clone https://github.com/Oliver-821/WebBasedOnDjango.git

After cloning the code from github to your workplace, go to the Anaconda Prompt (Anaconda) and enter the following code in order

    conda activate rango     
    
    cd WebBasedOnDjango
    
    pip install -r requirements.txt
    
    python manage.py makemigrations rango
    
    python manage.py migrate
    
    python population_script.py
    
    python manage.py runserver 127.0.0.1:8000
    
    open http://127.0.0.1:8000/
