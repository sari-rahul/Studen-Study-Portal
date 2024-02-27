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
![Jigsaw validation](static/images/readme_images/test-results/ssp-jigsawvalidation.png)

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



