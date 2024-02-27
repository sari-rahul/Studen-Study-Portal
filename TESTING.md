Go back to [README.md](/README.md)

# Testing
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
- [Responsiveness](#responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Lighthouse](#lighthouse)
- [Manual Testing](#manual-testing)

## Code Validation
### HTML

This project has been validated and passed through W3School Validator without any errors.
![HTML validation](static/images/readme_images/test-results/ssp-html-validator.png)

### CSS
This project has been validated and passed through Jigsaw Validator without any errors.
![Jigsaw validation](static/images/readme_images/test-results/ssp-jigsaw-validation.png)

### Javascript
The javascript files were tested using Jshint and has passed without any errors.
![JShint validation](static/images/readme_images/test-results/ssp-jshint.png)


### Python
|Page   | Validation   | Result  |
|--- |--- |---|
| Dashboard forms.py|![forms.py validation image](static/images/readme_images/test-results/ssp-dash-forms.png)|PASS|
|Dashboard models.py |![models.py validation image](static/images/readme_images/test-results/dashboard-models-vali.png)|PASS|
|Dashboard urls.py|![urls.py validation image](static/images/readme_images/test-results/dashboard-urls.png)|PASS|
|Dashboard test_form.py|![test_forms.py validation image](static/images/readme_images/test-results/dashboard-testform-vali.png)|PASS|
|Dashboard test_views.py|![test_views.py validation image]()|PASS|
|Dashboard views.py|![views.py validation image ]()|PASS|
|Discussion forms.py|![forms.py validation image](static/images/readme_images/test-results/discussion-forms.py.vali.png)| PASS|
|Discussion models.py |![models.py validation image](static/images/readme_images/test-results/discussion-models-vali.png)|PASS|
|Discussion urls.py|![urls.py validation image](static/images/readme_images/test-results/discussion-urls-vali.png)|PASS |
|Discussion views.py|![views.py validation image](static/images/readme_images/test-results/discussion-views-vali.png)|PASS |

## Responsiveness
During development each page was tested using dev tools in Google Chrome. The strategy involved ensuring that every page would adapt to various screen sizes beyond a width of 320px, as opposed to relying on fixed device-specific widths.
Further testing was done on mobile to confirm all is working as expected.

|Device|Screen Size|Pass/Fail|Comment|
| --- | --- | --- | ---|
| Iphone SE | 375x667 | PASS | All sections are displayed correctly. All features work|
| Iphone 12 Pro | 390x844 | PASS | All sections are displayed correctly. All features work|
| Samsung Galaxy s20U | 412x915 | PASS | All sections are displayed correctly. All features work|
| Galaxy Tab S4 | 712x1138| PASS | All sections are displayed correctly. All features work|
| Nest Hub | 1024x600 | PASS | All sections are displayed correctly. All features work|


## Browser Compatibility

|Browser|Result|Pass/Fail|Notes|
| --- | --- | --- | ---|
| Google Chrome | All pages, load as expected. All features work as expected | PASS | --- |
| Safari | All pages, load as expected. All features work as expected | PASS | --- |
| Edge | All pages, load as expected. All features work as expected | PASS | --- |


## Lighthouse
|Page |Validation| Result|
|---|---|---|
|Home Page|![homepage lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-homepage.png)|PASS|
|Notes Page|![notes page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-create-notes.png)|PASS|
|Homework Page|![homework page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-homework.png)|PASS|
|Todo Page|![todo page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-todo-page.png)|PASS|
|Books Page|![books page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-books.png)|PASS|
|Youtube Page|![youtube page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-youtube.png)|PASS|
|wikipedia Page|![wikipedia page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-wiki.png)|PASS|
|Calculator Page|![calculator page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-calculator.png)|PASS|
|Discussion Page|![discussion page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-discussion.png)|PASS|
|Question Answer Page|![Question Answer page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-questionanswer.png)|PASS|
|Ask a Question|![Ask a Question page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-askaquestion.png)|PASS|
|Profile Page|![profile page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-profile.png)|PASS|
|Password reset Page|![Password reset page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-passwrdreset.png)|PASS|
|Sign Up Page|![Sign In  page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-signup.png)|PASS|
|Login Page|![Log In page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-signin.png)|PASS|
|Signout Page|![Signout page lighthouse validation](static/images/readme_images/test-results/ssp-lighthouse-signout.png)|PASS|


## Manual Testing
- Home Page

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Navbar (Registerd user)|Click on logo in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on Home link in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on the Services button in Navbar|Dropdown menu appears| Pass|Navbar present on all pages |
||Click on the Profile button in Navbar |Dropdown Menu appears |Pass |Navbar present on all pages |
|| Click on the Logout button in Navbar |Redirect to logout screen |Pass | Navbar present on all pages|
|Navbar (Unregisterd user)|Click on logo in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on Home link in Navbar|Redirect to Home |Pass|
|| Click on the Register/Signup button |Redirect to Signup page| Pass|
|| Click on the Login button | Redirect to Login page|Pass|
|Landing Page (Registered user)| Click on Notes card |Redirected to create notes page| Pass |
|| Click on the Homeworks Card|Redirected to homework page| Pass |
|| Click on the To-Do Card|Redirected to To-Do page| Pass | 
|| Click on the Discussion Card|Redirected to Discussions Dashboard| Pass | 
|| Click on the Youtube Card|Redirected to Youtube Search page| Pass |
|| Click on the Wikipedia Card|Redirected to Wikipedia Search page| Pass |
|| Click on the Books Card|Redirected to Books search | Pass | 
|| Click on the Calculator Card|Redirected to Calculator| Pass | 
|Landing Page (Unregistered user)| Click on Notes card |Redirect to Sign Up page |Pass | 
||Click on Homework card |Redirect to Sign Up page |Pass | 
||Click on To-Do card |Redirect to Sign Up page |Pass | 
||Click on Youtube card |Redirect to Sign Up page |Pass | 
||Click on Books card |Redirect to Sign Up page |Pass | 
||Click on Wikipedia card |Redirect to Sign Up page |Pass | 
||Click on Calculator card |Redirect to Sign Up page |Pass |
||Click on Discussion card |Redirect to Discussion Dashboard page |Pass | Unregistered users can also access discussion page|  
|Footer| Click on the Github icon on footer| Redirect to Github repository of the project| Pass| Footer is present on all pages|
|Profile| Click on the 'Your Profile' Button from the Dropdown|Redirect to profile page|Pass|
|Delete Account| Click on the 'Delete Account' from the dropdown menu| Redirect to Delete account page| Pass| Delete account button is present on all pages except Discussion|
|Reset Password| Click on the reset password button from the dropdown menu| Redirects to reset password page and asks for email address|Pass |Reset Password button is present on all pages except Discussion|



- Create Notes Page


|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Create Notes | Fill in the form and click the Create button | A card with title,description and trash bin icon appears above.A success message is displayed|Pass |
|| Submit the form with empty data or space. | The data is not submitted. | Pass | The form fields are required.|
|| Click on the cards of Notes.|Redirected to page with full view of created Notes | Pass |
|| Click on the trash-bin icon on the cards.| Delete the corresponding note with a success message on the message bar. | Pass |

- Homework Page


|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
| Homework Page | Fill in the form and submit the form .| A table appears above with all the details.| Pass| The description is avoided from the table|
|| Submit the form with empty data or space|The data is not submitted.|Pass|The form fields are required.
||Click on the trash-bin icon on the cards.|Delete the corresponding homework with a success message on the message bar.| Pass|
||Click on the View now Button | Redirected to a page with complete view of the Homework| Pass |
||Click on the Mark as completed button | Status of the Homework is Updated| Pass | The 'Mark as Completed 'button has to be clicked|

- To-Do List Page


|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|To-Do List |Fill in the form and submit the form .|A table appears above with all the details.|Pass|
||Submit the form with empty data or space|The data is not submitted.| Pass |The form fields are required.|
||Click on the trash-bin icon on the cards.|Delete the corresponding homework with a success message on the message bar.|Pass|
||Click on the Mark as completed button|Status of the Homework is Updated| Pass|The 'Mark as Completed 'button has to be clicked|

- Youtube Search  Page


|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Youtube Page |Fill in the search box and hit the submit button. | The top 10 search results appear below. |Pass |
|| Hit the submit button without any text.| The search field is required message is displayed. |Pass |

- Book search Page

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Book Page |Fill in the search box and hit the submit button. | The top 10 search results appear below. |Pass |
|| Hit the submit button without any text.| The search field is required message is displayed. |Pass |
- Wikipedia Search Page


|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Wikipedia Page |Fill in the search box and hit the submit button. | The top 10 search results appear below. |Pass |
|| Hit the submit button without any text.| The search field is required message is displayed. |Pass |
- Calculator Page


|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Calculator Page| The numbers and symbols clicked appears on the calculator screen| Pass |
|| On clicking the '=' button the result appears| pass|
|| entering no numbers and by simply hitting'=' undefined is displayed| Pass|

- Discussion Page


|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Navbar (Registerd user)|Click on logo in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on Home link in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on Dashboard link in Navbar|Redirect to Dashboard |Pass|Navbar present on all pages |
|| Click on the Logout link | Redirected to Logout page | Pass |
|Navbar (Unregisterd user)| Click on the Register/Signup button |Redirect to Signup page| Pass|
|| Click on the Login button | Redirect to Login page|Pass|
||Click on logo in Navbar|Redirect to Home |Pass|Navbar present on all pages |
|Landing Page | Click on the cards with Discussion titles| Redirect to the Discussion forum with questioon and answers| Pass |
|| Click on the Next button | The second page of discussion dashboard is displayed| Pass | 

- Question and Answer Page


|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Discussion forum (Unregistered user)| Click the login link.| Redirect to login page| Pass |
|Discussion forum (Registered user)| Click the submit button without filling the Answer form.| The form is not submitted .| Pass |Fields in the form is marked as required.|
|| Populate the form with data and click the submit button.| The answer is submitted with a success message.| Pass |
|| Click the Delete button below the submitted answer.| A confirmation modal appears and asks for confirmation.| Pass |
|| Click the Delete button on the Modal | The Answer is deleted.| Pass |
|| Click the Edit button below the submitted Answer.| The Answer form is populated with the current answer.| Pass |
|| Edit the current Answer and click the Update button.|The new answer is submitted.| Pass |
|| Edit the current Answer to empty form and click the Update button.|The new answer is  not submitted.| Pass | All the fields are marked required.|

- Ask a Question Page


|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
| Question page | Submit the form without any data. |The form is not submitted .| Pass | The fields are marked required.|
||Submit the form with data .| The Question is submitted with a sucess message.|Pass |

- Profile Page


|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|To-Do secton| Click the create To-Do list button.| The user is redirected to  To-Do Page| Pass |
|| Add new items to to-do list.| The unfinished items appears in a table on profile page.| Pass |
|| Mark all items as completed. | "All To-Dos Completed " message appears on the screen.| Pass|
|| Click the trash-bin icon to delete the To-Do item |The item is deleted with a success message.| Pass |
|| Click the 'Mark as Completed' button. | The status is updated.| Pass |
|Homework secton| Click the create Homework list button.| The user is redirected to  Homework Page| Pass |
|| Add new items to Homework list.| The unfinished items appears in a table on profile page.| Pass |
|| Mark all items as completed. | "All Homeworks are Completed " message appears on the screen.| Pass|
|| Click the trash-bin icon to delete the Homeworks item |The item is deleted with a success message.| Pass |
|| Click the 'Mark as Completed' button. | The status is updated.| Pass |









