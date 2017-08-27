# ItemCatalog
Project 4 of Udacity's Fullstack Nanodegree.

## Project Overview
This is an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## What have I Learnt?
I learnt how to develop a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication, when to properly use the various HTTP methods available and how these methods relate to CRUD (create, read, update and delete) operations.

## How Does This Help My Career?
* Efficiently interacting with data is the backbone upon which performant web applications are built.
* Properly implementing authentication mechanisms and appropriately mapping HTTP methods to CRUD operations.


## Installation and Requirements :

1.Install the Vagrant & VirtualBox 5.1. <br>
2.Clone the Udacity Vagrantfile. <br>
3.Clone this repo in the vagrant dir. <br>
4.Launch the Vagrant VM by vagrant up command. <br>
5.Log into Vagrant VM vagrant ssh command. <br>
6.Navigate to cd /vagrant as instructed in terminal. <br>
7.Setup application's database by running ```python database_setup.py``` .This would create a database named catalogdb.db <br>
8.Insert sample data items by running ```python data.py``` . This would populate the database with some data. <br>
9.Run the application by running ```python project.py``` <br>

Access the application locally using http://localhost:5000


## Using Google Sign In
To get the Google login working there are a few additional steps:

1.Go to Google Dev Console. <br>
2.Sign up or Login in this. <br>
3.Go to Credentials. <br>
4.Select Create Crendentials > OAuth Client ID <br>
5.Select Web application. <br>
6.Enter name 'My Project' <br>
7.Authorized JavaScript origins = 'http://localhost:5000' <br>
8.Save Changes <br>
9.Copy the Client ID and paste it into the data-clientid in login.html present in the templates folder <br>
10. Authorized redirect URIs = 'http://localhost:5000/login' and 'http://localhost:5000/gconnect' and save it.<br>
11.On the Dev Console Select Download JSON <br>
12.Rename JSON file to client_secrets.json <br>
13.Place JSON file in your directory where project.py is present <br>
14.Run your application. Hope that runs well.

## LICENSE
The content of this program is licensed under a <a href="https://creativecommons.org/licenses/by/2.0/">Creative Common Attribution</a>
