# **![Logo](assets/images/speranza_logo.png) SPERANZA**

![Mokup Image](wireframes/mockup.png)

---

## **Project Goal** 

***Speranza***, the italian word for ***Hope***.

The main goal of this project is to give a pinch of hope to cancer patients and their friends and relatives by introducing them to the latest advancements within the *immunotherapy* world, contributing to an easier access to clinical trials information available worldwide.

On top of this, provide registered users to share their stories/testemonies/comments about any given clinical trial.

***"Hope is the life we live, the attitude we carry, the gift we give others. Hope is the energy, the courage and the strength to keep believing in the goodness of life, God and the people around us."***

***Froyle Davies***

---
<a></a>

## **Table of contents**

1. [UX](#ux)

    1.1 [User Goals and Stories](#user-goals-and-stories)

    1.2 [User Requirements and Expectations](#user-requirements-and-expectations)
    
    1.3 [Company Goals](#company-goals)
    
    1.4 [Design Choices](#design-choices)

2. [Wireframes](#wireframes)
3. [Features](#features)
 
    3.1 [Existing Features](#existing-features)
 
    3.2 [Future Features](#future-features)

4. [Languages, Libraries, Frameworks and Tools](#languages-libraries-frameworks-and-tools)
 
    4.1 [Languages](#languages)
 
    4.2 [Libraries](#libraries)
 
    4.3 [Frameworks and Databases](#frameworks-and-databases)
 
    4.4 [Tools](#tools)

5. [Testing and Debugging](#testing-and-debugging)
 
    5.1 [Test 1](#)
 
    5.2 [Test 2](#)
 
    5.3 [Test 3](#)

    5.4 [Test 4](#)
 
    5.5 [Test 5](#)
 
6. [Deployment](#deployment)

7. [Credits and Acknowledgments](#credits-and-acknowledgments)
 
    7.1 [Credits](#credits)
 
    7.2 [Acknowledgments](#acknowledgments)

---

<a></a>

## **UX**

---
[[Back to top]](#table-of-contents)

<a></a>

### **User Goals and Stories**
#### **Goals**
As a user I aim for:
* A simple and intuitive website.
* Easy navigation across pages.
* Visually attractive and accurate information.
* Appealing call-to-actions.

#### **Stories**
As a user, I want to:
* Get a brief introduction about what is immunotherapy.
* Access the most recent clinical trials available regarding immunotherapy.
* Shortlist the most interesting clinical trials into my dashboard and check all my contributions to the community.
* Share my opinion and see other users comments concerning a specific clinical trial.
* Access additional info about a certain clinical trial such as: 'recruitment status', 'study phase', 'country' requirements, amongst others.

[[Back to top]](#table-of-contents)

<a></a>

### **User Requirements and Expectations**
#### **Requirements**
* Easy navigation.
* Reliable information.
* Good responsiveness across multiple devices and browsers.
* Immediate feedback on data inputs and/or submissions.
* Call-to-actions functioning properly.

#### **Expectations**
* Updated and clear information about the clinical trials.
* Links must be working properly to reach the target with any setbacks.
* External links must open in a new tab.
* Easy interaction with other users.
* Proper feedback handling an error.
* See and edit my comments in an easy way.
* Access a specific clinical trial comment section easily.

[[Back to top]](#table-of-contents)

<a></a>

### **Company Goals**

* Provide healthcare patients, their family and firends, with the necessary information about clinical trials working with immunotherapy.
* Give doctors an easy way to look for potential clinical trials to recommend their patients.
* Advocate online for the immunotherapy approach as the future of medicine.
* Provide a safe space for users to share their stories and experiences in regard to a specific clinical trial.
* Engage the community in active discussions and in sharing their experiences/testimonies.


[[Back to top]](#table-of-contents)

<a></a>

### **Design Choices**
#### Fonts
![Mokup Image](wireframes/speranza_fonts.png)

#### Icons
Throughout out the website, I will be using icons provided by [FontAwesome](https://fontawesome.com/ "FontAwesome").

The icons used are self-explanatory and aid the navigation of the user, bringing an intuitive imagery to the website.

#### Colors
![Mokup Image](wireframes/speranza_color_palette.png)

#### Structure

The structure of this website will be quite simple as the main focus is on the data handling. Therefore, the website will consist of mainly 3 pages, the Landing Page, the Clinical Trials and the User's Dashboard page, as know as "My Trials & Reviews".

##### Navigation bar and Footer
Throuhgout the entire website, the user will constantly have access to the Navigation bar, displaying according to the need the necessary sections. 

Concerning the footer, it will display some contact information and any other less relevant content.

##### Landing Page
The Landing page will showcase the immunotherapy as the future of cancer fighting with a brief introduction and promoting the website as a safe space for the community to share their experiences. Also, an inspirational sentence will give the user the proper perception of the webpage intent.

Below, the user will be able to see the most recent comments to the clinical trials. If the user wants to participate, they will have to properly register afterwards in order to acess the entire set of clinical trials with the comments section feature available.

Also, on top of the landing page, two call-to-action buttons will be displayed to transmit the user the right perception of the need to create a user account to be able to access the full features of the webisite. 

##### User's authentication
The user's authentication method used on this website is adapted from the corresponding lesson of the [Code Institute](https://codeinstitute.net/ "Code Institue") Full Stack Software Development Course.

##### Clinical Trials
After a user is registered and logged in, it will not only have full access to the entire set of clinical trials but also access the comments section per trial.

Whilst the user is not registered/logged in, he can only access the general information but will not be able to participate in the discussions.

This page is powered by a search feature in order to easily find the most suitable clinical trial for its needs.

All the clinical trials will be displayed as cards that will include an icon to shortlist the clinical trial or a trash bin icon if the user wants to remove it from through this page and not through its own dashboard.

##### My Trials & Reviews (User's Dashboard)
The user's dashboard will display the shorlisted clinical trials, as well as all the contributions that the user gave to the community.

##### Comments Section
The comments section will only be displayd when the user is logged in, and will be available through a modal where all the comments for any given clinical trial will be displayed, sorted by date (newest first).

#### Edit Comments/Reviews
A simple edit page as been created during the development process in order to tackle the difficulties originated by having an edit section in a second modal.
The page retreives the user comment within a textarea that the user chose to edit, giving him the option to edit the comment in a simple efficient way.


[[Back to top]](#table-of-contents)

---
<a></a>

## **Wireframes**

[Small devices](wireframes/small-devices.png)

[Medium Devices](wireframes/medium-devices.png)

[Large devices](wireframes/large-devices.png)

<a></a>

---

<a></a>

## **Features**

[[Back to top]](#table-of-contents)

<a></a>

### **Existing Features**

* Sharing Comments: Users can share their experiences/testemonials/reviews/opinions with every registered user for any given clinical trials.

* Last 5 Comments Preview: Gives every user a sneak peek about the ongoing discussions within the community making them wanting to participate and be part of it.

* Flash Messages: Provides immediate feedback to the user on the CRUD functionalities across the webpage.

* [Open Trials](https://opentrials.net/api.html "Open Trials") API: Provides the website with all the public information available regarding the clinical trials. 

* User Authentication: Limiting/Providing some users access to website resources.

* Dynamic Navbar: Adaptative Navbar based on User's Authentication.

* Clinical Trials Shortlist: Provides the user with a direct access to the trails bookmarked as favourites for an easier access to the discussions.

* Search Bar: Facilitates the user to find the most relevant clinical trial in order to engage with the community on that specific topic.

* Trials Counter: Gives the user a quick overview of the amount of trials that are potentially relevant.

* Error Handlers: Allow user to navigate back to the homepage in case of a 404 or 500 errors.

* Randomized [Unsplash](https://source.unsplash.com/ 'Unsplash') pictures from my [Clinical Trials Public Collection](https://unsplash.com/collections/61510941/clinical-trials 'Unsplash'): Gives the clinical trials cards a random picture from that collection, allowing the user to be less scared about the medical terms displayed that might scare the user of trying to interact with the website and community.

[[Back to top]](#table-of-contents)

<a></a>

### **Future Features**
* Comments counter on every clinical trial card for user to assess the activity level of a discussion, visible to all the users. 

* Amount of users that shortlist a specific trial, visible on each specific card to al the users.

* Pagination in Clinical Trials and My Trials & Reviews pages, as well as in the Add Trial Modal where comments are displayed.

* Automatic cookies deletion after a certain idle time to increase security.

* Request a confirmation about the correctness of the user's action prior deleting a comment or saving a comment edition, or remove clinical trial from the shorlist.

* Counter for number of trials and contributions in user's My Trials & Reviews dashboard.

[[Back to top]](#table-of-contents)

---

<a></a>

## **Languages, Libraries, Frameworks and Tools**

[[Back to top]](#table-of-contents)

<a></a>

### **Languages**
* [HTML](https://www.w3.org/MarkUp/1995-archive/html-spec.html "HTML")
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html "CSS")
* [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript "Javascript")
* [Python](https://www.python.org/ "Python")
* [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/ "Jinja2")

[[Back to top]](#table-of-contents)

<a></a>

### **Libraries**
* [jQuery](https://jquery.com/ "jQuery")
* [FontAwesome](https://fontawesome.com/ "FontAwesome")
* [Google Fonts](https://fonts.google.com/ "Google Fonts")
* [Unsplash](https://unsplash.com/ "Unsplash")

[[Back to top]](#table-of-contents)

<a></a>

### **Frameworks and Databases**
* [Bootstrap](https://getbootstrap.com/ "Bootstrap")
* [MongoDB](https://www.mongodb.com/2 "MongoDB")
* [Flask](https://flask.palletsprojects.com/en/1.1.x/ "Flask")


[[Back to top]](#table-of-contents)

<a></a>

### **Tools**
* [Git](https://git-scm.com/ "Git")
* [Gitpod](https://gitpod.io/ "Gitpod")
* [Balsamiq](https://balsamiq.com/ "Balsamiq")
* [Coolors](https://coolors.co/ "Coolors")
* [Contrast-Checker](https://coolors.co/contrast-checker "Contrast Checker")
* [Free Logo Design](https://www.freelogodesign.org "Free Logo Design")
* [TinyPNG](https://tinypng.com/ "Tiny PNG")
* [Favicon](https://favicon.io/favicon-converter/ "Favcicon")
* [Techsini](http://techsini.com/multi-mockup/ "Techsini")
* [W3C-Markup-validation](https://validator.w3.org/ "Markup Validator")
* [W3C-Jigsaw](https://jigsaw.w3.org/css-validator/ "Jigsaw Validator")
* [W3C-Spell Checker](https://www.w3.org/2002/01/spellchecker "Spell Checker")
* [Google-Lightouse](https://developers.google.com/web/tools/lighthouse "Google Lighthouse")
* [JSHint](https://jshint.com/ "JSHint")

[[Back to top]](#table-of-contents)

---

<a></a>

## **Testing and Debugging**

[[Back to top]](#table-of-contents)

<a></a>

| User Stories 	| Page(s) 	| UX 	| Execution 	| Testing 	| Test Result 	| Conclusion 	|
|-	|-	|-	|-	|-	|-	|-	|
| Get a brief introduction about what is immunotherapy. | clinical_trials.html | When the user accesses this page, it is shown with a brief introduction to what is the "Immunotherapy". This allows the user to better understand better the scope of the website, together with the Intro text on the homepage. | To tackle this user story, I have placed an introductory paragraph to the Clinical Trials Page. This introduction has a link to the [NCI](https://www.cancer.gov/ 'NCI') where more information can be found. | I have navigated through the website and found it easy to get a grip on what is immunotherapy. On top of it, understand that by the amount of clinical trials available, the immunotherapy is not yet the first choice in cancer treatments but it has an immense potential.   	| 1- Navigation is easy and intuitive.  2- User can easily get the information required and access the [NCI](https://www.cancer.gov/ 'NCI') for more information.  3- External link is working properly. |  Test meets criteria |
| Access the most recent clinical trials available regarding immunotherapy.| clinical_trials.html | When the user accesses the Clinical Trials Page, it is confronted with a page full of cards, each one displaying a unique clinical trial, but all related to immunotherapy & cancer.  | In order to display the most relevant information to the user, I have used the [Open Trials](https://opentrials.net/api.html "Open Trials") API to fetch the clinical trials data. As these come along with a lot of information that is not so relevant to the user, I have used an [Elastic Search](https://www.elastic.co/ 'Elastic') where all the [Open Trials](https://opentrials.net/api.html "Open Trials") trial data is indexed, to construct a query. This query is also used to power the search bar. | Due to the importance accessing this info by any kind of user, this feature was made available to all the users, with or without logging in. A search bar was implemented to facilitate the user finding the most appropriate trial. The user can also see the amount of trials that match the searching criteria via de trial counter. The main information about the trial can be found in the modal after pressing the "Check this trial" button. | 1- The user has visibility of 100 trials out of 539 trials (Pagination is a feature to be implemented in the future!) and can access each trial individually. 2- More detailed information about the trial is provided in the modal. 3- The search bar works well and retrieves the proper trials respecting the query (Immunotherapy&Cancer&'User search criteria"), and the counter shows amount of trials that meet this criteria. 4- When no trials are found, the counter displays "We have 0 trials available for you". |  Test meets criteria  |
| Shortlist the most interesting clinical trials into my dashboard and check all my contributions to the community 	|  	|  	|  	|  	|  	|  	|
| Share my opinion and see other users comments concerning a specific clinical trial 	|  	|  	|  	|  	|  	|  	|
| Access additional info about a certain clinical trial such as: 'recruitment status', 'study phase', 'country' requirements, amongst others 	|  	|  	|  	|  	|  	|  	|

[[Back to top]](#table-of-contents)

<a></a>

### **Debugging**
#### **Known Bugs and Corrections** ####

##### **Bug** #####

##### **(Potential) Corrections** #####
https://stackoverflow.com/questions/37270787/uncaught-syntaxerror-failed-to-execute-queryselector-on-document/37271406

##### **Bug** #####
Get unique trial ID from the API in modal, after displaying API trials with for loop. All trials were getting the exact same trial id from the API.
##### **(Potential) Corrections** #####
Jinja2 template -> {trial.id} as value of a hidden input field with trial_id_api attribute name.

##### **Bug** #####
Textarea outside modal
##### **(Potential) Corrections** #####
textarea {max-width:95%;}

##### **Bug** #####
Form within form not possible
##### **(Potential) Corrections** #####
Comment section beloz modal footer

##### **Bug** #####
Textarea of second modal can not retreive data from the previous modal
##### **(Potential) Corrections** #####
jQuery>siblings

##### **Bug** #####
/workspace/Speranza/app.py:228: DeprecationWarning: update is deprecated. Use replace_one, update_one or update_many instead.
  mongo.db.comments.update({
##### **(Potential) Corrections** #####
To be updated


[[Back to top]](#table-of-contents)

---

<a></a>

## **Deployment**

[[Back to top]](#table-of-contents)

---

<a></a>

## **Credits and Acknowledgments**

[[Back to top]](#table-of-contents)

<a></a>

### **Credits**

#### **Media**

#### **Content**

[[Back to top]](#table-of-contents)

<a></a>

### **Acknowledgments**

[[Back to top]](#table-of-contents)