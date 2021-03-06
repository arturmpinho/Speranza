![DB Structure](static/images/speranza_logo.png)
# **SPERANZA**

***To my father, recently diagnosed with a squamous cell carcinoma, that inspired me on pursuing this project with his hope of finding a suitable immunotherapy clinical trial to participate in case the conventional treatment does not erradicate the tumor.***

![Mockup Image](wireframes/mockup.png)

---

## **Project Goal** 

***Speranza***, the Italian word for ***Hope***.

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

2. [Wireframes and DB structure](#wireframes-and-DB-structure)
3. [Features](#features)
 
    3.1 [Existing Features](#existing-features)
 
    3.2 [Future Features](#future-features)

4. [Languages, Libraries, Frameworks and Tools](#languages-libraries-frameworks-and-tools)
 
    4.1 [Languages](#languages)
 
    4.2 [Libraries](#libraries)
 
    4.3 [Frameworks and Databases](#frameworks-and-databases)
 
    4.4 [Tools](#tools)

5. [Testing and Debugging](#testing-and-debugging)
 
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
* Share and edit my opinions and see other users comments/reviews concerning a specific clinical trial.

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

* Provide healthcare patients, their family and friends, with the necessary information about clinical trials working with immunotherapy.
* Give doctors an easy way to look for potential clinical trials to recommend their patients.
* Advocate online for the immunotherapy approach as the future of medicine.
* Provide a safe space for users to share their stories and experiences in regard to a specific clinical trial.
* Engage the community in active discussions and in sharing their experiences/testimonies.


[[Back to top]](#table-of-contents)

<a></a>

### **Design Choices**
#### Fonts
![Mockup Image](wireframes/speranza_fonts.png)

#### Icons
Throughout out the website, I will be using icons provided by [FontAwesome](https://fontawesome.com/ "FontAwesome").

The icons used are self-explanatory and aid the navigation of the user, bringing an intuitive imagery to the website.

#### Colors
![Mockup Image](wireframes/speranza_color_palette.png)

[[Back to top]](#table-of-contents)

#### Structure

The structure of this website will be quite simple as the main focus is on the data handling. Therefore, the website will consist of mainly 3 pages, the Landing Page, the Clinical Trials and the User's Dashboard page, as know as "My Trials & Reviews".

##### Navigation bar and Footer
Throughout the entire website, the user will constantly have access to the Navigation bar, displaying according to the need the necessary sections. 

Concerning the footer, it will display some contact information and any other less relevant content.

##### Landing Page
The Landing page will showcase the immunotherapy as the future of cancer fighting with a brief introduction and promoting the website as a safe space for the community to share their experiences. Also, an inspirational sentence will give the user the proper perception of the web page intent.

Below, the user will be able to see the most recent comments to the clinical trials. If the user wants to participate, they will have to properly register afterwards in order to access the entire set of clinical trials with the comments section feature available.

Also, on top of the landing page, two call-to-action buttons will be displayed to transmit the user the right perception of the need to create a user account to be able to access the full features of the website. 

##### User's authentication
The user's authentication method used on this website is adapted from the corresponding lesson of the [Code Institute](https://codeinstitute.net/ "Code Institue") Full Stack Software Development Course.

##### Clinical Trials
After a user is registered and logged in, it will not only have full access to the entire set of clinical trials but also access the comments section per trial.

Whilst the user is not registered/logged in, he can only access the general information but will not be able to participate in the discussions.

This page is powered by a search feature in order to easily find the most suitable clinical trial for its needs.

All the clinical trials will be displayed as cards that will include an icon to shortlist the clinical trial or a trash bin icon if the user wants to remove it from through this page and not through its own dashboard.

##### My Trials & Reviews (User's Dashboard)
The user's dashboard will display the shortlisted clinical trials, as well as all the contributions that the user gave to the community.

##### Comments Section
The comments section will only be displayd when the user is logged in, and will be available through a modal where all the comments for any given clinical trial will be displayed, sorted by date (the newest first).

#### Edit Comments/Reviews
A simple edit page as been created during the development process in order to tackle the difficulties originated by having an edit section in a second modal.
The page retrieves the user comment within a text area that the user chose to edit, giving him the option to edit the comment in a simple efficient way.


[[Back to top]](#table-of-contents)

---
<a></a>

## **Wireframes and DB Structure**
[[Back to top]](#table-of-contents)

### **Wireframes**

[Small devices](wireframes/small-devices.png)

[Medium Devices](wireframes/medium-devices.png)

[Large devices](wireframes/large-devices.png)

### **DB Structure**
![DB Structure](static/images/speranza_dbstructure.png) 

[[Back to top]](#table-of-contents)
<a></a>

---

<a></a>

## **Features**

[[Back to top]](#table-of-contents)

<a></a>

### **Existing Features**

* Sharing Comments: Users can share their experiences/testimonials/reviews/opinions with every registered user for any given clinical trials.

* Last 5 Comments Preview: Gives every user a sneak peek about the ongoing discussions within the community making them wanting to participate and be part of it.

* Flash Messages: Provides immediate feedback to the user on the CRUD functionalities across the webpage.

* [Open Trials](https://opentrials.net/api.html "Open Trials") API: Provides the website with all the public information available regarding the clinical trials. 

* User Authentication: Limiting/Providing some users access to website resources.

* Dynamic Navbar: Adaptive Navbar based on User's Authentication.

* Clinical Trials Shortlist: Provides the user with direct access to the trails bookmarked as favourites for an easier access to the discussions.

* Search Bar: Facilitates the user to find the most relevant clinical trial in order to engage with the community on that specific topic.

* Trials Counter: Gives the user a quick overview of the amount of trials that are potentially relevant.

* Error Handlers: Allow user to navigate back to the homepage in case of a 404 or 500 errors.

* Randomized [Unsplash](https://source.unsplash.com/ 'Unsplash') pictures from my [Clinical Trials Public Collection](https://unsplash.com/collections/61510941/clinical-trials 'Unsplash'): Gives the clinical trials cards a random picture from that collection, allowing the user to be less scared about the medical terms displayed that might scare the user of trying to interact with the website and community.

[[Back to top]](#table-of-contents)

<a></a>

### **Future Features**
* Comments counter on every clinical trial card for user to assess the activity level of a discussion, visible to all the users. 

* Amount of users that shortlisted a specific trial, visible on each specific card to all the users.

* Pagination in Clinical Trials and My Trials & Reviews pages, as well as in the Add Trial Modal where comments are displayed.

* Automatic cookies deletion after a certain idle time to increase security.

* Request a confirmation about the correctness of the user's action prior deleting a comment or saving a comment edition, or remove clinical trial from the shortlist.

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
* [RandomKeygen](https://randomkeygen.com/ "RandomKeygen")
* [Swagger](https://swagger.io/ "Swagger")
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
| Get a brief introduction about what is immunotherapy | clinical_trials.html | When the user accesses this page, it is shown with a brief introduction to what is the "Immunotherapy". This allows the user to better understand better the scope of the website, together with the Intro text on the homepage. | To tackle this user story, I have placed an introductory paragraph to the Clinical Trials Page. This introduction has a link to the [NCI](https://www.cancer.gov/ 'National Cancer Institute') where more information can be found. | I have navigated through the website and found it easy to get a grip on what is immunotherapy. On top of it, understand that by the amount of clinical trials available, the immunotherapy is not yet the first choice in cancer treatments but it has an immense potential.   	| 1- Navigation is easy and intuitive. <br> 2- User can easily get the information required and access the [NCI](https://www.cancer.gov/ 'National Cancer Institute') for more information. <br> 3- External link is working properly. |  Test meets criteria |
| Access the most recent clinical trials available regarding immunotherapy  | clinical_trials.html | When the user accesses the Clinical Trials Page, it is confronted with a page full of cards, each one displaying a unique clinical trial, but all related to immunotherapy & cancer.  | In order to display the most relevant information to the user, I have used the [Open Trials](https://opentrials.net/api.html "Open Trials") API to fetch the clinical trials' data. As these come along with a lot of information that is not so relevant to the user, I have used an [Elastic Search](https://www.elastic.co/ 'Elastic') where all the [Open Trials](https://opentrials.net/api.html "Open Trials") trial data is indexed, to construct a query. This query is also used to power the search bar. | Due to the importance accessing this info by any kind of user, this feature was made available to all the users, with or without logging in. A search bar was implemented to facilitate the user finding the most appropriate trial. The user can also see the amount of trials that match the searching criteria via the trial counter. The main information about the trial can be found in the modal after pressing the "Check this trial" button. | 1- The user has visibility of 100 trials out of 539 trials (Pagination is a feature to be implemented in the future!) and can access each trial individually. 2- More detailed information about the trial is provided in the modal. 3- The search bar works well and retrieves the proper trials respecting the query (Immunotherapy&Cancer&'User search criteria"), and the counter shows amount of trials that meet this criteria. 4- When no trials are found, the counter displays "We have 0 trials available for you". |  Test meets criteria  |
| Shortlist the most interesting clinical trials into my dashboard and check all my contributions to the community 	|   clinical_trials.html <br> add_trial.html <br> mytrials.html   |  When the user notices a clinical trial of interest, this trial can be added to the user's favourites clicking on the 'Add to favourites' button in each clinical trial modal. This trial is automatically added to the user's dashboard that can be checked under the 'My Trials & Reviews' page. If the user is not authenticated or registered, the add to favourites feature is not displayed. The same goes for the comments/reviews (see below) which share the page with the 'favourites'. When these are nonexistant, the user sees a message redirecting them to the Clinical Trials page, so they can shortlist a trial.  | In order to meet this criteria, I have made available an "Add to Favourites" button in each clinical trials modal. After this is done, the user can navigate to "My Trials & Reviews" in order to consult these. Also, when the user has no more interest in the trial, removal is possible. The comments added, as per below User Story, function in a similar way and are displayed below the shortlist of the clinical trials.   | I have picked several trials and add them to my favourites. These are well displayed in "My Trials & Reviews" page and able to access the trials' information as if in the "Clinical Trials" page. The comments generated, if any, are also displayed chronologically in this page.    |   1- User can shortlist all the trials. <br> 2- User can see all 'favourites' in one page. <br> 3- User Comments are all displayed in one place.  |   The test passes all the requirements.    |
| Share and edit my opinions and see other users comments/reviews concerning a specific clinical trial 	|   clinical_trials.html <br> add_trial.html <br> mytrials.html <br> comments.html <br> edit_reviews <br> home.html   |  If the user wants to contribute to the community, he can do so via the comment section available in the modals of each clinical trial. All the comments are then available to all registered users and the last 5 of all users available as a preview in the home page. In the 'My Trials & Reviews' page the user can find all the contributions done to date.	|   To comply with this user story, I have made available a comment section in the 'add_trial modal' composed by a textarea element and a 'Post' button. Moreover, in the modal, the user can read all other users, as well as its own, contributions in each specific trial above the text area. When a contribution is posted, it is 'saved' in the user's "My Trials & Reviews" page. Non authenticated user can only get a sneak peek of other user's comments in the homepage, where the last 5 are displayed, but can not interact with the other users. If authenticated, the user can post comments/reviews in every trial of interest. If the user thinks that any of its own comments need to be edited, he can access the editing page by pressing the 'edit' button present next to every own comment (deletion is also always possible on the same moments the edit option is available). Afterwards, the user is redirected to the edit page where the comment can be updated. | Chose several trials of interest and commented on them. Comments are saved and displayed in the modal of corresponding clinical trials and under 'My Reviews' in the 'My Trials and Reviews' page for future consultation.    |   1- User has a specific place to share the contributions per specific trial. <br> 2- User has a dedicated page to edit own comments. <br> 3- Users can benefit from other users contributions.  	| Test fully meets requirements 	|

---

| Navigation & Responsiveness 	| Page(s) 	|  Devices 	| Browsers 	| Test Result 	| Conclusion 	|
|-	|-	|-	|-	|-	|-	|
| Test 1  |   home.html   | Acer Spin (laptop) <br> Acer Spin (tablet) <br> Iphone 8 <br> iPhone 6S <br> iPhone 11 Pro <br> Developer Tools   | Chrome <br> Firefox <br> Opera      | User can easily get a grip of how the navigation is structured as it respects the current standards. Responsiveness is excellent across devices and browsers.      | Pass  |
| Test 2  |   clinical_trials.html   | Acer Spin (laptop) <br> Acer Spin (tablet) <br> Iphone 8 <br> iPhone 6S <br> iPhone 11 Pro <br> Developer Tools     | Chrome <br> Firefox <br> Opera      | Cards are well arranged and responsiveness is excellent across devices and browsers. Intuitive call-to-action buttons facilitate the navigation and engagement of the users      | Pass   |
| Test 3  |   add_trials.html   | Acer Spin (laptop) <br> Acer Spin (tablet) <br> Iphone 8 <br> iPhone 6S <br> iPhone 11 Pro <br> Developer Tools     | Chrome <br> Firefox <br> Opera      | Modals are working wihtout any issue and have intuitive call-to-action buttons easing the navigation. Modals respond well across browsers and different devices       | Pass   |
| Test 4  |   comments.html   | Acer Spin (laptop) <br> Acer Spin (tablet) <br> Iphone 8 <br> iPhone 6S <br> iPhone 11 Pro <br> Developer Tools     | Chrome <br> Firefox <br> Opera      | Text area within modal does not present any issue and comments/reviews section is easy to read. Responsiveness is very good.      | Pass   |
| Test 5  |   mytrials.html   | Acer Spin (laptop) <br> Acer Spin (tablet) <br> Iphone 8 <br> iPhone 6S <br> iPhone 11 Pro <br> Developer Tools     | Chrome <br> Firefox <br> Opera      | Cards are well arranged, easing the navigation and intuitive call-to-action buttons to support the user. Modals work without any problem. Page and Modals respond well across browsers and different devices       | Pass   |
| Test 6  |   edit_reviews.html   | Acer Spin (laptop) <br> Acer Spin (tablet) <br> Iphone 8 <br> iPhone 6S <br> iPhone 11 Pro <br> Developer Tools     | Chrome <br> Firefox <br> Opera      | Simple, straight to the point page. User understands 100% the intent of the page. Responsiveness across devices and browsers is excellent       | Pass   |
| Test 7  |   login.html   | Acer Spin (laptop) <br> Acer Spin (tablet) <br> Iphone 8 <br> iPhone 6S <br> iPhone 11 Pro <br> Developer Tools     | Chrome <br> Firefox <br> Opera      | Simple form with validation working properly. Responds well across multiple browsers and devices       | Pass   |
| Test 8  |   register.html   | Acer Spin (laptop) <br> Acer Spin (tablet) <br> Iphone 8 <br> iPhone 6S <br> iPhone 11 Pro <br> Developer Tools     | Chrome <br> Firefox <br> Opera      | Simple form with field validation and key placeholders facilitate the user interaction/navigation. Responds well across multiple browsers and devices        | Pass   |
| Test 9  |   navbar.html   | Acer Spin (laptop) <br> Acer Spin (tablet) <br> Iphone 8 <br> iPhone 6S <br> iPhone 11 Pro <br> Developer Tools     | Chrome <br> Firefox <br> Opera      | Navbar dynamically adjusts to user authentication supporting the navigation. It is present throughout the entire application. Navbar also collapses into an hamburger icon in small and medium devices. Responsiveness is excellent in all browsers and devices.       | Pass   |
| Test 10  |   footer.html   | Acer Spin (laptop) <br> Acer Spin (tablet) <br> Iphone 8 <br> iPhone 6S <br> iPhone 11 Pro <br> Developer Tools     | Chrome <br> Firefox <br> Opera      | Less relevant information held in this component but gives the user the chance to connect with the business via the social links. Great responsiveness across devices.       | Pass   |
| Test 11  |   flash_msgs.html   | Acer Spin (laptop) <br> Acer Spin (tablet) <br> Iphone 8 <br> iPhone 6S <br> iPhone 11 Pro <br> Developer Tools     | Chrome <br> Firefox <br> Opera      | Flash messages give the user immediate feedback assuring the user about the action taken or giving tips. Fundamental piece of a good navigation. It is working properly and responsiveness across browsers and devices is extremely good.      | Pass   |
| Test 12  |   error.html   | Acer Spin (laptop) <br> Acer Spin (tablet) <br> Iphone 8 <br> iPhone 6S <br> iPhone 11 Pro <br> Developer Tools     | Chrome <br> Firefox <br> Opera      | Another fundamental feature of an application is the error handlers. This page guarantees that the user, in case a 404 or 500 error happens, that he can always go back to the homepage. Tested by altering the code and forcing these errors. Working perfectly in all tested devices and browsers.        | Pass   |

<br>

*Note 1:* Bootstrap was used throughout the entire application guaranteeing an excellent responsiveness.

*Note 2:* In order to improve the UX, in case that one day a trial is deleted from the API, I wanted to make sure that the user would not face an error preventing him of accessing its dashboard. Therefore I rearraged the 'View Trial' view and added an else statement in case the result attained is 0.

*Note 3:* After running the [Google-Lightouse](https://developers.google.com/web/tools/lighthouse "Google Lighthouse") Tool, I noticed that the Unsplash API, considering the amount of results retrieved in the 'Clinical Trials' is having a strong negative impact in the loading performance, especially in mobiles. Thereof, in the future, I intend to save locally all the images of [this](https://unsplash.com/collections/61510941/clinical-trials 'Unsplash') collection in order to enhance the loading time of this page.

![Lighthouse](static/images/clinical_trials_mobile_lighthouse.PNG) 

*Note 4:* The usage of modals came with additional challenges, especially due to the fact of the dynamic IDs. 
Moreover, when the authenticated user performs an action inside the modal, namely commenting or adding/removing the trial to/from the favourites, the modal closes and redirects the user to the Clinical Trials Pages, not keeping the user inside the modal, which may cause some discomfort. 
The same goes for when the user performs these same actions, starting from the 'My Trials & Reviews' page. Nonetheless, here it is aggravated by the fact that the user is redirected to another page and not to the one he started at.
Because modals are an excellent visual tool to any website, I would like to keep it. Therefore, in the future I want to deep dive into this issue in order to increase the UX without sacrificing this feature. If in the end this will not be possible, I can make sure all actions have dedicated pages so the re directions won't affect too much the UX.

---

[[Back to top]](#table-of-contents)

<a></a>

### **Debugging**

| Bugs 	| Description and Fixes |  Sources 	|   Result
|-	|-	|-	|-	|
| Some modals are not opening when user clicks on "Check this trial button"	| According to [this](https://stackoverflow.com/questions/37270787/uncaught-syntaxerror-failed-to-execute-queryselector-on-document/37271406 'Stack Overflow') discussion, IDs cannot start with a number, which is the case for some trial IDs provided by the [Open Trials](https://opentrials.net/api.html "Open Trials") API. The suggested and applied fix was to start all the modal IDs with the letter 'a'.  	| [Stack Overflow](https://stackoverflow.com/questions/37270787/uncaught-syntaxerror-failed-to-execute-queryselector-on-document/37271406 'Stack Overflow')	| **Fixed**	|
|For loop within another for loop in order to get correct comments to the correct trial not working	| By making sure both loops went through a list instead of 1 list and 1 dictionary, the correct comment shows at the corresponding trial	|   N/A	|   **Fixed**	|
|   Search displaying more than 100 trials	| Due to the limit of the amount of trials that can be displayed per page, in case a user uses a keyword like 'lung' which will retrieve more than 100 results, the counter would still catch those above the limit of 100. Therefore, I have used the following if statement to fix this bug: "if count > 100: count = 100", and not mislead the user. | N/A	| **Temporary fix**	|
| Broken Links coming from the API	| Data coming from the OpenTrials API can be manipulated but not changed. Nonetheless, some of these links are broken, resulting the user to open a nonfunctional page.	| N/A	| **Not fixed**. In the future maybe place a warning below the corresponding link in the modal. |
| Clinical trials cards all display the same picture.   |Images from [Unsplash](https://source.unsplash.com/ 'Unsplash') API are not being randomized transmitting the looks that a placeholder image was left in place. By using Jinja2 templating language, I was able to generate a random number to append to the src of the img   | [Stack Overflow](https://stackoverflow.com/questions/36683951/generate-random-number-with-jinja2 'Stack Overflow') | **Fixed** 	|
| Footer in the middle of the page.   |When the page does not have enough content, as in the [Login Page](http://speranza.herokuapp.com/login 'Speranza'), the footer dos not saty at the bottom.	|  N/A	| **Not fixed** 	|
| Not all trials can be displayed   | OpenTrials API only displays m??x. 100 results per page	|[OperTrials API Documentation](https://api.opentrials.net/v1/docs/#!/trials/searchTrials 'Swagger')	| **Not fixed**. To solve this issue, I intend to implement a pagination feature in a future release.	|
|   Data provided by [Open Trials](https://opentrials.net/api.html "Open Trials") API is not updated    | Data from [Open Trials](https://opentrials.net/api.html "Open Trials") API is not being updated on a regular basis.	|  N/A | **Not fixed**. |
|   With some comments, the corresponding trial name is not showing	|   This bug was caused by the limit of 100 results per query. When the user comments on a trial he found using various filters, the trial was not found in the general query (limited to the 1st hundred). Instead of the general query, I looped through the comments and for each comment, queried the API data to get that specific trial matching the comment. This way, the query maximum contains 1 result and added these results to a list in case trial was not yet in that list.  	|   N/A	|   **Fixed**  	|
|After editing a comment, the comment shows with the new date/time, altering the order of conversations.	|When e.g. two users engage in a conversation it should be interposed. Nonetheless, when one of the users edit a comment/review, this will acquire the new time/date info, altering the order of the conversations.	| N/A   |**Not fixed**. In the future I want to order the comments by the 'posted_on' field and create an additional field - last_edit - grabing the editing date/time. This way, the conversations will always be interposed and won't create any confusion to the user.	|
    
    all_trials = []
        for comment in comments:
            result = client.trials.searchTrials(
                q=comment["trial_id"]).result()
            if result not in all_trials:
                all_trials.append(result)


[[Back to top]](#table-of-contents)

---

<a></a>

## **Deployment**

### Local Deployment

I have created Speranza using [Github](https://github.com/ 'Github') and [Gitpod](https://gitpod.io/ 'Gitpod') to write my code. 

Then, I used commits to git followed by "git push" to my GitHub repository.

This project has been deployed to [Heroku](https://www.heroku.com/ 'Heroku') which was previously connected with the [Speranza Repository in Github](https://github.com/arturmpinho/Speranza 'Speranza') to automatically get all the pushes done in [Github](https://github.com/ 'GitHub'). 

To run this project locally, follow the next steps:

This project can be run locally by following the following steps: ***(
as I have user used [Gitpod](https://gitpod.io/ 'Gitpod') for development, the next steps are specific to it. Adjustment may be necessary depending on your IDE. More information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)***.


To clone the project: 

1. From the application's repository, click the "code" button and download the zip of the repository.
    You can also clone the repository using the following command in your terminal:

    ``` 
    git clone https://github.com/arturmpinho/Speranza.git
    ``` 

1. Access the folder in your terminal window and install the application's [required modules](https://github.com/arturmpinho/Speranza/blob/master/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

1. Sign-in or sign-up to [MongoDB](https://www.mongodb.com/2 'MongoDB') and create a new cluster
    * Within the Sandbox, click the collections button, folowed by a click in Create Database (Add My Own Data) called speranza
    * Set up the following collections: users, trials and comments [Click here to see the exact Database Structure](#wireframes-and-db-structure)
    * Under the Security Menu on the left, select Database Access.
    * Add a new database user, and keep the credentials secure
    * Within the Network Access option, add IP Address 0.0.0.0

1. In your IDE, create your env.py file at the root level of the application, containing the following lines and variables:
    ```
    import os

    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")
    os.environ.setdefault("MONGO_URI", "YOUR_MONGODB_URI")
    os.environ.setdefault("MONGO_DBNAME", "DATABASE_NAME")

    ```

    Please note that you will need to update the **"YOUR_SECRET_KEY"** with your own secret key, as well as the **YOUR_MONGODB_URI** and **DATABASE_NAME** values with those provided by [MongoDB](https://www.mongodb.com/2 'MongoDB').
    
    Tip for your **YOUR_SECRET_KEY**:  you can use a [Password Generator](https://randomkeygen.com/ 'Random Keygen') in order to have a secure secret key.

    It is recommended to use minimum the 'Fort Knox Passwords'.

    To find your **YOUR_MONGODB_URI**, go to your clusters and click on 'connect'. Choose 'connect' your application and copy the link provided. 
    Don't forget to update the necessary fields such as password and database name.

    If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file in order to safeguard your sensitive information.

1. Run your application locally typing the following command in your terminal. 
    ```
    python3 app.py. 
    ```
    
### To deploy your project on Heroku, use the following steps: 

1. Login to your [Heroku](https://www.heroku.com/ 'Heroku') account and create a new app. Preferably, choose the region where you are located. 

1. Ensure the Procfile and requirements.txt files are created and updated in your local repository.  

    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```

1. The Procfile should contain the following line:
    ```
    web: python app.py
    ```

1. Go to your "deployment method"-section and Choose "Github" for automatic deployment.

1. Below, make sure your Github user is selected, and then enter the name of your repository. Click "search". When it finds the repository, then click the "connect" button.

1. Go up and click "settings" and then scroll down and click "Reveal config vars".
 
 Set up the same variables as in your env.py (IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME): 

    IP = 0.0.0.0
    MONGO_DBNAME = DATABASE_NAME
    MONGO_URI = YOUR_MONGODB_URI
    PORT = 5000
    SECRET_KEY = YOUR_SECRET_KEY
    

1. Click in "Deploy" tab. Scroll down and click "Enable automatic deployment".

1. Just beneath, click "Deploy branch". Heroku will now start building the app. 

1. In order to commit your changes to the branch, use git push to push your changes via your IDE.


[[Back to top]](#table-of-contents)

---

<a></a>

## **Credits and Acknowledgments**

[[Back to top]](#table-of-contents)

<a></a>

### **Credits**
* All software and applications used to create this website are mentioned above in section [Languages Libraries Frameworks and Tools](#languages-libraries-frameworks and-tools).
* [MDN WebDocs](https://developer.mozilla.org/ "MDN WebDocs")

#### **Media**
* You can find all the images sources through the Unslplash collection prepared [here](https://unsplash.com/collections/61510941/clinical-trials "Unsplash").

#### **Content**
* [OpenTrials](https://opentrials.net/api.html "OpenTrials") and their article made available [here](https://trialsjournal.biomedcentral.com/articles/10.1186/s13063-016-1290-8 "OpenTrials").

[[Back to top]](#table-of-contents)

<a></a>

### **Acknowledgments**
To [Stackoverflow](https://stackoverflow.com/ "Stackoverflow") community and to [W3Schools](https://www.w3schools.com/ "W3Schools") for all the content made publicly available.

To [Julian Nash](https://www.youtube.com/channel/UC5_oFcBFlawLcFCBmU7oNZA 'Youtube') for the great tutorial [Working with Jinja templates - Python on the web - Learning Flask Series Pt. 6](https://www.youtube.com/watch?v=mqrbF0qGSLI "Youtube").

To [Paul Walsh](https://github.com/pwalsh 'Github') on the handy [notebook](https://github.com/pwalsh/notebooks/blob/master/opentrials/opentrials.ipynb 'Github') on how to handle the [OpenTrials](https://opentrials.net/api.html "OpenTrials") API.

To my mentor, [Anna_Villanueva](https://github.com/annavillanueva "GitHub"), for all the inputs and guidance throughout this project.

To my friends and family that took time to test the website and for their valuable recommendations and insights.

A special thanks to [Anouk](https://github.com/AnoukSmet/ "GitHub"), for all the support given suring these difficult past months and for all the suggestions and guidance during the implementation of this project.

[[Back to top]](#table-of-contents)