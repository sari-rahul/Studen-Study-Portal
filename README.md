# Student Study Portal

[Live Deployed site](https://student-study-portal-9cc1c977016f.herokuapp.com/)

Student Study Portal is a full stack project which allows the students to create notes,save homeworks,Create To-Do list,Search in books, Youtube and Wikipedia.It also has a calculator built-in. One of the major feature of this project is It has a built in discussion forum where students can ask doubts to others people and get answers. The Project was created as apart is Fullstack Software Development Course at Code Institute.

![responsive image](static/readme_images/ssp1.png)

## Contents

- [User Experience](#user-experience)
    -   [User Stories](#user-stories)
    -   [Site Goals](#site-goals)
    -   [Scope](#scope)

- [Design](#design)
    -   [Colour Scheme](#colour-scheme)
    -   [Database Schema](#Database-Schema)
    -   [Fonts](#Fonts)
    -   [Wireframes](#Wireframes)
    -   [Agile Methodology](#Agile-Methodology)
         -   [Overview](#overview)
         -   [EPICS(Milestones)](#epicsmilestones)
         -   [MoSCoW prioritization](#moscow-prioritization)
         -   [GitHub Projects](#github-projects)
[Features](#features)
    -   [Navbar](#Navbar)
    -   [Footer](#Footer)

-   [Home](#Home)
        -   [Hero Section](#hero-section)
        -   [Search Form](#search-form)
        -   [Recent Listings](#recent-listings)
        -   [Listing Card](#listing-card)
    -   [Listings Page](#listings-page)
    -   [Create Listing](#create-listing)
    -   [Profile Page](#profile-page)
    -   [My Listings](#my-listings)
    -   [My Favourites](#my-favourites)
    -   [Remove From Favourites](#remove-from-favourites)
    -   [Edit Listing](#edit-listing)
    -   [Delete Listing](#delete-listing)
    -   [View Listing](#view-listing)
    -   [User account and User account listings](#user-account-and-user-account-listings)
    -   [Sign In Page](#sign-in-page)
    -   [Sign Up Page](#sign-up-page)
    -   [Sign Out Confirmation](#sign-out-confirmation)
    -   [Edit Profile](#edit-profile)
    -   [Delete Profile Confirmation](#delete-profile-confirmation)
    -   [We are sorry to see you go](#we-are-sorry-to-see-you-go)
    -   [Password reset](#password-reset)
    -   [Password reset email sent](#password-reset-email-sent)
    -   [Enter a new password](#enter-a-new-password)
    -   [Password Reset Completed](#password-reset-completed)
    -   [Error Pages](#error-pages)
-   [Future Features](#future-features)
-   [Testing](#testing)
-   [Bugs](#Bugs)
-   [Technologies And Languages](#technologies-and-languages)
    -   [Languages Used](#languages-used)
    -   [Python Modules](#python-modules)
    -   [Technologies and programs](#technologies-and-programs)
-   [Deployment](#deployment)
    -   [Before Deployment](#before-deployment)
    -   [Deployment on Heroku](#deployment-on-heroku)
    -   [Creating A Fork](#creating-a-fork)
    -   [Cloning Repository](#cloning-repository)
-   [Credits](#credits)
    -   [Media](#media)
    -   [Code](#code)
    -   [Acknowledgements](#acknowledgements)
    -   [Comments](#comments)

## User Experience

### User Stories
1. As a developer I can setup a new Django project so that I can create the project's structure.
2. As a developer I can setup a new Django project so that I can create the project's structure.
3. As a developer I can connect database and media storage so that the user's stored data is stored successfully.
4. As a developer I can create wireframes so that the layout of the website is clear for desktop and mobile.
5. As a User I can navigate through the website so that I can access different sections efficiently.
6. As a user I want the website to be responsive so that I can view it on my mobile.
7. As a registered user I want to add notes to the notes section so that I can stores notes about various subjects.
8. As a Registered User I want to open the Home works Page so that I can add Home works to it.
9. As a Registered User I want to have a page for you tube search so that I can search for information in You tube easily.
10. As a Registered User I want to a To-Do Page so that I can add and delete items to it.
11. As a Registered User I want a page for books so that I can search for various books as per requirement.
12. As a Registered User I want a page for Dictionary so that I can search for different word meanings and their pronunciations as per requirement.
13. As a Registered User I want a page for Wikipedia so that I can search for different topics.
14. As a User I want to Register in to have an account so that I can have access to all the features of this website.
15. As a User I want to have a Profile Page so that I can instantly see my pending works.
16. As a User I want to have an account setup so that I can Delete my account if needed.
17. As a User I want to have a Password reset Facility so that I can reset my password if needed.
18. As a Unregistered User I want to redirected to Sign Up page so that I can Instantly Sign up and get access to the website facilities.

### Site Goals

1. To provide students with a place store their Notes and Homeworks.
2. To provide an to create ToDo List and update it.
3. To provide a place for the students where they can browse in YouTube ,Wikipedia and various Books as per requirement.
4. To provide a discussion forum for students to asks questions and to answrer them.
5. To make the website available and functional on every device.

### Scope
The project aims to develop an online platform called "Student Study Portal" that facilitates students in Storing Notes, Homeworks , creating ToDo list and to search in different inbuilt services. It also provides a discussion forum where student can ask questions and also answer others questions.The platform will be responsive and user-friendly, providing features for user registration, creating notes, homeworks and updating them, creating todo list and updating them, searching in wikipedia,Youtube and books. It give access to all users to the discussion forum without registration.

Key Features:
1. Initial Project Setup:

- Developers can set up a new Django project to create the project's structure.
- Database and media storage will be connected to ensure data storage and retrieval.
- An early deployment of the application will be carried out to confirm the initial setup's functionality
.
2. Responsive Design:

-The website will be responsive, allowing users to access it on both desktop and mobile devices.

3. User Authentication:
- Users can register an account, providing access to all functionality of Student Study Portal.
- Registered users can log in to view their homeworks left to be done and other things in the todo list.

4. Profile Management:
- Users can reset their passwords in case they forget them.
- Users can delete their profiles.

8. Notification Messages:
- Users will receive notification messages when performing CRUD operations, login/logout, and signup actions.

## Design
The website features a calming and professional color palette that combines shades of blue, green, and pink with complementary neutrals. <br>

![Colour Scheme](static/images/readme_images/ssp-colorscheme.png)

### Database Schema
![database schema]()

#### Models
1. Allauth User Model

The User model is part of Django Allauth. The model comes with predefined fields as standard. Some of them are username, email, name, password, and more. This model is used for user authentication, that's why changes directly to this model are not advised. The User model is connected to the Notes model as a Foreignkey. 

2. Note Model 

The Note model was created to store all the information related to notes created by the user.It is connectes to User model as a ForeignKey.

3. Homework Model

The Homework model was created to store all the information related to Homeworks created by the user.It is connectes to User model as a ForeignKey.

4. Todo Model

The Todo model was created to store all the information related to Todo list created by the user.It is connectes to User model as a ForeignKey.

5. Question Model
The question model was created to store the questions asked by the user.It is connected to the User model as Foreign key.

6. Answer Model
The Answer model was created to store the answers given by the users.It is connected to the User model and Question as Foreign keys.


### Fonts
The font used in this project is fjalla one and Barlow, which compliments the design of the website. <br>

![Font](static/images/readme_images/ssp-font.png)

### Wireframes
- Home
- Notes
- Homework
- Todo
- Search
- Discussion forum dashboard
- Discussion form with answer form
- Profile
- Login and Register

### Agile Methodology
#### Overview
This project was created using agile principles. This was a big learning curve together with my very first full-stack project. Using the agile approach allowed me to plan all the features of the website through user stories. Each user story has acceptance criteria and tasks to clearly outline the requirements for each feature to be completed.

#### EPICS(Milestones)
The user stories are grouped into seven EPICS or Milestones.
![Milestones]()

#### MoSCoW prioritization
This prioritization technique was used to effectively prioritize the features and requirements of the project based on their importance. The acronym "MoSCoW" stands for "Must have, Should have, Could have, and Won't have." Each category helps categorize and prioritize features to guide the development process and ensure that the most critical elements are addressed first. <br>
![User Story]()

#### GitHub Projects
The project was created using a basic Kanban Board structure, divided into columns such as Todo, In Progress and Done. This setup provides a clear and organized way to track the status of tasks and visualize and manage the workflow. <br>
![User Story]()

## Features
### Navbar
The navbar is a component that is present on all pages. It was created using Bootstrap and is fully responsive. The 'STUDENT STUDY PORTAL' logo which serves as a link to the homepage is located on the left side on the navbar. On the right are the nav links which allow the user to easily navigate through the website from any point. If the user is not authenticated the links displayed are Home, Register/Signup and Login on the Home and on discussion page Dashboard is also included.

![nav logged out]()

 If the user is authenticated they will see Home, Services,Profile and Logout. The profile link will have the user's username displayed to indicate that the user is logged in. For a better user experience, the Services and Profile button has a dropdown menu with all the facilities denoted. The Home and Logout pages, when active is white and brighter to let the user know the page they are currently on.

 ![nav logged in]()
 ![nav mobile]()

 ### Footer
 The Footer is consistent throughout the website with a link to github repository of this project

 ![Footer]()