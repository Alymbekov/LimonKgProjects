# LimonKgProjects
README file for {{ project_name }}

###DEVELOPMENT

    # Clone secrets and fablib repositories
    git clone https://github.com/Alymbekov/LimonKgProjects.git
    git clone https://github.com/Alymbekov/LimonKgProjects.git
    
    # Change into project directory
    cd <project_name>
    
    # Make and Activate virtual environment
    pipenv shell
    
    # Install requirements
    pipenv install or if you use different virtual environment you can use
    pip install -r requirements.txt
    
    #python manage.py migrate
    
    # Start the development server
    python manage.py runserver
    

For user-specific settings, do not modify the loc.py file. Rather, create a <username>.py settings file that imports the local settings. It is recommended that you push your user-specific settings into version control
along with everything else, **but should not include any secrets.**  To run the development server with your user-specific settings:

    python manage.py runserver 
   
    
###DEPLOYMENT

