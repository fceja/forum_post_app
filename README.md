# Description
A forum-like app created with Django framework.<br/>
App allows users to create an account, login, and create posts on a community webpage.<br/> 

You can view implementation here -> [Forum Post App](https://django-user-post-a42f5d79d28f.herokuapp.com/)

<br/>

There are three types of users:
- Standard user
    - can create post
    - can remove their own posts
- Mod user
    - *same and standard user
    - can remove other users' posts
    - can ban a user from creating posts
- Banned user
    - can not create posts
    - can delete their own existing posts

<br/>

## Installation
![](https://img.shields.io/badge/OS-Linux%20%7C%20MacOS%20%7C%20Windows-eaeaea)

</br>
** Note: at project root, must rename `sample.env` file to `.env` and fill with valid values
</br>
</br>

1. Install Python3
    - ```
      https://www.python.org/downloads/
      ```
3. Clone repo
3. Create virtual environment
    1. Create virtual environment, at project root run:
        - Linux / macOS
            - ```
              python3 -m venv venv
              ```
        - Windows      
            - ```
              python -m venv venv
              ```
    2. Initialize virtual environment, at project root run:
        - Linux / macOS
            - ```
              source venv/bin/activate
              ```
        - Windows      
            - ```
              ./bin/activate
              ```
       - Note - you should see ```(venv)``` in terminal when successfully initialized
4. Install dependencies, at project root run:
    - ```
      pip install -r requirements.txt
      ```
5. Run development Django server
    - Linux / macOS
        - ```
          export DJANGO_ENV=development && python3 ./manage.py runserver
          ```
    - Windows
        - ```
          set DJANGO_ENV=development && python manage.py runserver
          ```
    - App should be running on http://127.0.0.1:8000/


<br/>

## Technologies & Tools
<a href="https://www.python.org/" target="_blank" rel="noreferrer">
    <img
      src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg"
      alt="python"
      width="70"
      height="70"
    /></a>
<a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer">
    <img
      src="https://www.djangoproject.com/favicon.ico"
      width="70"
      height="70"
      alt="Django Logo"
    /></a>
<a href="https://getbootstrap.com" target="_blank" rel="noreferrer">
    <img
      src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg"
      alt="bootstrap"
      width="70"
      height="70"
    /></a>
<a href="https://www.w3.org/html/" target="_blank" rel="noreferrer">
    <img
      src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg"
      alt="html5"
      width="70"
      height="70"
    /></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank" rel="noreferrer">
    <img
      src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original-wordmark.svg"
      alt="css"
      width="70"
      height="70"
    /></a>
<a href="https://www.postgresql.org/" target="_blank" rel="noreferrer">
    <img
      src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original-wordmark.svg"
      width="70"
      height="70"
      alt="posgres"
    /></a>
<a href="https://www.heroku.com/" target="_blank" rel="noreferrer">
    <img
      src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/heroku/heroku-original-wordmark.svg"
      alt="heroku"
      width="70"
      height="70"
    /></a>
</br>
</br>

<br/>

## Screenshots
![alt text](/screenshots/screenshot-ui-1.png "Screenshot of UI-1")
![alt text](/screenshots/screenshot-ui-2.png "Screenshot of UI-2")
![alt text](/screenshots/screenshot-ui-3.png "Screenshot of UI-3")
