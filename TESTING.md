Go back to [README.md](/README.md)

# Testing
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#JavaScript)
    - [Python](#python)
- [Responsiveness](#Responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Lighthouse](#Lighthouse)
- [Manual Testing](#manual-testing)

## Code Validation
### HTML

This project has been validated and passed through W3School Validator without any errors.
![HTML validation](static/images/readme_images/ssp-html-validator.png)

### CSS
This project has been validated and passed through Jigsaw Validator without any errors.
![Jigsaw validation](static/images/readme_images/ssp-jigsawvalidation.png)


### Javascript
The javascript files were tested using Jshint and has passed without any errors.
![JShint validation](static/images/readme_images/ssp-jshint.png)


### Python
|Page   | Validation   | Result  |
|--- |--- |---|
| Dashboard forms.py|![forms.py validation image](static/images/readme_images/ssp-dash-forms.png)|PASS|
|Dashboard models.py |![models.py validation image](dashboard/__pycache__/dashboard-models-vali.png)|PASS|
|Dashboard urls.py|![urls.py validation image](static/images/readme_images/dashboard-urls.png)|PASS|
|Dashboard test_form.py|![test_forms.py validation image](static/images/readme_images/dashboard-testform-vali.png)|PASS|
|Dashboard test_views.py|![test_views.py validation image]()|PASS|
|Dashboard views.py|![views.py validation image ]()|PASS|
|Discussion forms.py|![forms.py validation image](static/images/readme_images/discussion-forms.py.vali.png)| PASS|
|Discussion models.py |![models.py validation image](static/images/readme_images/discussion-models-vali.png)|PASS|
|Discussion urls.py|![urls.py validation image](static/images/readme_images/discussion-urls-vali.png)|PASS |
|Discussion views.py|![views.py validation image](static/images/readme_images/discussion-views-vali.png)|PASS |


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