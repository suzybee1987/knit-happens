Back to [README](README.md)

## **Contents**

- [**Automated Testing**](#automated-testing)
  - [**Bag**](#bag)
  - [**Checkout**](#checkout)
  - [**Profile**](#profile)
  - [**Products**](#products)
  - [**Blog**](#blog)
  - [**Home*](#home)
- [**Manual Testing**](#manual-testing)
  - [**Browsers**](#browsers)
  - [**Devices Used**](#devices-used)
  - [**Navigation**](#navigation)
  - [**Home Page**](#home-page)
  - [**Register Page**](#register-page)
  - [**Log In Page**](#log-in-page)
  - [**Profile Page**](#profile-page)
  - [**Products Pages**](#products-pages)
    - [**Products**](#products)
    - [**Product Details**](#product-details)
    - [**Add Product**](#add-product)
    - [**Edit Product**](#edit-product)
  - [**Bag**](#bag)
  - [**Checkout**](#checkout)
  - [**Blog Page**](#blog-page)
- [**User Stories Testing**](#user-stories-testing)
- [**Wave**](#features)
- [**Lighthouse**](#lighthouse)
- [**Validators**](#validators)
  - [**HTML Validator**](#html-validator)
  - [**CSS Jigsaw**](#css-jigsaw)
  - [**JSHint**](#jshint)
  - [**PEP8**](#pep8])

### **Automated Testing**
#### **Bag**
#### **Checkout**
#### **Profile**
#### **Products**
#### **Blog**
#### **Home**


### **Manual Testing**
#### **Browsers**
The site was tested on:
- Safari
- Google Chrome
- Firefox

#### **Devices Used**
The site was tested on these devices:
- iPhone 12
- Huawei P30 Lite
- Samsung 10
- iPhone SE 2020
- iPad 5th Generation
- 27" iMac
- Acer Swift 3 running Windows 11

[Back to contents](#contents)

#### **Navigation**
    - all users

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Home button    | To redirect to home page | Click the home button | Button navigates to home | Pass |
| Navbar links | Clicking All Products takes user to All Products page | Click All Products | Redirected to All Products page | Pass |
|  | Clicking category takes user to the specific category page | Click each category in turn | Redirected to specific category page | Pass |
|   | Click Bag takes user to Bag page | Click Bag | Redirected to Bag page | Pass |
|   | Clicking Blog takes user to the Blog homepage | Click Blog | Redirected to Blog Page | Pass |
|   | Searching using Search Bar displays the product in the products page | Type wool in search bar | Redirected to Products page with all wool shown | Pass |
| Footer | Redirect to Facebook in new tab | Click Facebook icon | Facebook page opened in new tab | Pass |
|  | Redirect to Instagram in new tab | Click Instagram icon | Instagram page opened in new tab | Pass |
|  | Redirect to GitHub in new tab | Click GitHub icon | My GitHub profile page opened in new tab | Pass |
|  | Redirect to Pinterest in new tab | Click Pinterest icon | Pinterest page opened in new tab | Pass |
|  | Clicking T&Cs takes user to the Terms and Conditions page | Click T&Cs | Terms and conditions page opened | Pass |
|  | Clicking Privacy Policy takes user to the Terms and Conditions page | Click Privacy Policy | Privacy Policy page opened | Pass |


#### **Navigation**
    - users logged in
|  Navbar links   | Clicking Profile takes user to their profile page | Click Profile | Redirected to Profile Page | Pass |
|  | Click Log Out logs out the user | Click Log Out | User logged out and redirected to Log In | Pass |


    - user not logged in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Navbar links | Click Log In redirects to log in page | Click Log In | User redirected to Log In Page | Pass |
|  | Click Register redirects to log in page | Click Register | User redirected to Register Page | Pass |


#### **Home Page**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- |:----:|
| Floating menu | Clicking the arrow down button takes users further down the page to see shop options | Click arrow button | User redirected down the page to shopping options | Pass |
| Shopping Options | Clicking Shop Needles, Shop Wool, Shop Patterns Links lead to different parts of shop | Click Shop Needles, Shop Wool, Shop Patterns | Redirected to the relevant products in shop | Pass |
| Blog Inspiration Card | Click to be taken to the blog for inspiration | Click link | User redirected to blog  | Pass |

#### **Register Page**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Register functionality | Form validation for email requires `@` symbol |  Attempt to register without `@` in input field | Form validation requests valid email address | Pass |
| | E-mail Again value must be same as Email value | Attempt to register with incorrect email in email again input field | Form validation requests email address must match | Pass |
| | Username must be between 4 and 15 characters | Attempt to enter username with less than 4 characters | Feedback error displayed | Pass |
| | Username must be between 4 and 15 characters | Attempt to enter username with more than 15 characters | Form restricts the user from using more than 15 characters | Pass |
| | Password must be longer than 8 characters | Attempt to enter password with less than 8 characters | Form restricts the user from using less than 8 characters | Pass |
| | Register with new user and password to be logged in and redirected to Profile page | Enter email address, name, username, password and click register | New account registered and profile page shown | Pass |

#### **Log In Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-----------------| ----------|  ---------- | :----: |
| Log in functionality | Correct user/pass combination directs user to their profile page with name displayed in tab | Log in with correct username/password combination | Redirected to user profile page with name displayed in tab | Pass |
|   | Incorrect username/password combination shows error message | Attempt to log in with incorrect credentials | "The username and/or password you specified are not correct." error message appears| Pass |
| Link to Register | Redirect to Register page | Click link to register | Redirected to Register page | Pass |

#### **Profile Page**
#### **Products Pages**
#### **Products**
#### **Product Details**
#### **Add Product**
#### **Edit Product**
#### **Bag**
#### **Checkout**
#### **Blog Page**
[Back to contents](#contents)
#### **Wave**

The site was inspected for accessibility using the [Wave Browser Extension](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh) and changes made to HTML following this inspection. 




[Back to contents](#contents)