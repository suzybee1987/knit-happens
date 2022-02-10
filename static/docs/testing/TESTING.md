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
Automated testing of views was completed to:
- Test the calc_subtotal function works as expected
- Test the bag views work correctly
- Test the url works when loading the page
- Test the correct template loads on page load
- Test the products page is accessible by name
- Test that the view_bag view works correctly
- Test that the add to bag view works as expected
- Test that the add_to_bag function adds the item to the bag
- Test that the add_to_bag view adds the product to the bag
- Test that the add_to_bag view increases the quantity of an item if the item is already present in the shopping bag
- Test that the adjust bag view works as expected to calculate total
- Test that the add_to_bag view updates the quantity of an item if the item is already in the bag
- Test remove from bag view removes the product from the bag
- Test that the remove_from_bag view removes an item from the bag
- Test that the remove from bag view returns an error if something goes wrong


#### **Checkout**
Automated testing of views was completed to:
- Test the checkout page loads correctly
- Test that the cache_checkout_data view works as expected
- Test the url works when loading the page
- Test the correct template loads on page load
- test the products page is accessible by name
- Test get checkout view when items in the bag
- Test error msg appears when bag empty
- Test error msg appears when no stripe key
- Check if user is authenticated then autofill the form with details

Automated testing of models was completed to:
- test the order model
- test order line model string method

Automated testing of forms was completed to:
- test to see if full name field is required
- test to see if email field is required
- test to see if phone number field is required
- test to see if country field is required
- test to see if town_or_city field is required
- test to see if street_address1 field is required
- check the field only displays certain fields

[Back to contents](#contents)

#### **Profiles**
Automated testing of views was completed to:
- Test the url works when loading the page
- Test the correct template loads on page load
- Test the profile page is accessible by name
- Test the profile form works if form is valid
- Test orders displayed on login to profile page

Automated testing of models was completed to:
- Test retrieving the user profile
- Test the user profile string method returns the username

Automated testing of forms was completed to:
- Test that none of the form fields are required


#### **Products**
Automated testing of views was completed to:
- Test the url works when loading the page
- Test the correct template loads on page load
- Test the products page is accessible by name
- Test products display
- Test categories sort functionality
- Test that the sort functionality works
- Test that the search functionality works as expected
- Test that the search error message display correctly
- Test product detail page loads via url
- Test product detail page loads via name
- Test product detail page loads via template

Automated testing of models was completed to:
- Test category model string method
- Testing category models friendly name string method returns friendly name
- Test product model string method
- Test that the product name is returned
- Test that the product description is returned
- Test whether a product has sizes or not
- Test whether a product has weights or not

Automated testing of forms was completed to:
- Test to see if review title field is required
- Test to see if review field is required
- Check the field only displays certain fields
- Test to see if review title field is required


#### **Blog**
Automated testing of views was completed to:
- Test the blog page loads correctly
- Test the url works when loading the page
- Test the correct template loads on page load
- Test the blog page is accessible by name
- Test blog posts display as expected
- Test to see if the post string method returns the title as expected
- Test post detail page loads via name
- Test post detail page loads via template


#### **Home**
Automated testing of views was completed to:
- Test the url works when loading the page
- Test the correct template loads on page load
- Test the home page is accessible by name
- Test the url works when loading the page
- Test the correct template loads on page load
- Test the privacy page is accessible by name
- Test the url works when loading the page
- Test the correct template loads on page load
- Test the terms and conditions page is accessible by name

[Back to contents](#contents)

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

[Back to contents](#contents)

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

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Personal Information | Personal information is visible if previously saved | Navigate to Profile page, view personal information | The personal information is visible in Personal Information section | Pass |
| | Personal information can be updated | Navigate to Profile page, change personal information, click update information. | The personal information is updated with the new details. | Pass |
| Order History | Order History is visible if order placed while logged in | Navigate to Profile page, view Order History Section | The Order History is visible | Pass |
| | Order information can be accessed by clicking order number | Navigate to Profile page, view Order History Section, click Order Number | Order Information is visible | Pass |

[Back to contents](#contents)

#### **Products Pages**

##### **Products**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| All products visible | Products page shows all products | Open Products page and view products | Products visible and 12 to a page  | Pass |
|  | Searching by category shows products from that category | Select to search by each category | Products from each category successfully displayed | Pass |
| Pagination | When more than 12 products available only 12 displayed at a time | Open Products page, view number of products result if more than 12 | Only 12 products available per page if more than 12 products available | Pass |

##### **Product Details**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Product Details | Product description displayed for individual product | Open Product Detail page and view products | Product details visible | Pass |
| Add to bag | Clicking Add To Bag adds the product to the bag | Open Product Detail page click add to bag | Product available in bag | Pass |
|  | If product has sizes the Sizes field is required  | Open Product Detail page click add to bag without adding size | Form validation requires an item must be selected | Pass |
|  | If product has weight the Weights field is required  | Open Product Detail page click add to bag without adding weight | Form validation requires an item must be selected | Pass |
| Reviews | Reviews for individual products available | Navigate to product review section | Reviews visible or message displayed advising "There are no reviews for <product-name> yet. Why don't you add one?" | Pass |
| Reviews | Add a review form adds review to product details page | While logged in navigate to product review section, fill out form, click add review | Review visible in reviews section | Pass |
|  | User must be logged in to add review to product details page | While not logged in navigate to product review section, attempt to leave review | Message revealed "Please log in to add a review of a product." | Pass |


##### **Add Product**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Add Products | Only admin is allowed to visit add product page | Log in as non-superuser and attempt to access /products/add/ | Redirect to home page, error message displayed "Sorry, only store owners can do that." | Pass |
| Form Validation | Required fields must be completed to add the product  | Attempt to add product without filling in a required field | Error message "Please fill in this field" | Pass |


##### **Edit Product**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Edit Products | Only admin is allowed to visit edit product page | Log in as non-superuser and attempt to access /products/<item_id>/edit/ | Redirect to home page, error message displayed "Sorry, only store owners can do that." | Pass |
| Form Validation | Required fields must be completed to edit the product  | Attempt to edit product without filling in a required field | Error message "Please fill in this field" | Pass |

[Back to contents](#contents)

#### **Bag**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| View Items | Correct products are in the bag | Add product to bag and check quantity and total are in the bag | Expected products are in the bag | Pass |
| Update Items | Update the number of a product in the bag and it will reflect in bag and price | Change number of product in bag and check quantity and total has updated | Total and quantity updated | Pass |
| Remove Items | Click remove item for item to be removed from the bag | Click remove beside relevant product | Item removed from bag and notification to confirm this "Removed <item> from your bag" | Pass |

#### **Checkout**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| View Items | Correct products are in the checkout | Add products to bag, click Secure Checkout | Expected products are in the checkout product list | Pass |
| Form Validation | Required fields must be completed to complete  | Attempt to check out without filling in a required field | Error message "Please fill in this field" | Pass |


#### **Blog Page**
| ------------- |-------------| -----|  ---------- | :----:|
| All blog posts visible | Blog page shows all blog posts | Open Blog page and view posts | Posts visible | Pass |
| Add Post | Only logged in users are allowed to add posts | Log out and attempt to add blog post | User redirected to home page, error message displayed "Sorry, only store owners can do that." | Pass |


##### **Blog Post Detail**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Post Details | Post is displayed for individual slug | Open Post Detail page | Post visible | Pass |
| Comments | Add a comment form adds comment to post details page | While logged in navigate to post, fill out form, click add comment | Comment visible in post section | Pass |
|  | User must be logged in to add comment to post | While not logged in navigate to post, attempt to leave comment | Message revealed "Please log in to add a comment." | Pass |
| Edit Post | Only author of the post can edit a post | Log in as different user and attempt to edit blog post | Message displayed "You are not authorised to do this!" | Pass |
| Delete Post | Only author of the post can delete a post | Log in as different user and attempt to delete blog post | Message displayed "You are not authorised to do this!" | Pass |
| Comments | Add a comment form adds comment to post details page | While logged in navigate to post, fill out form, click add comment | Comment visible in post section | Pass |
|  | User must be logged in to add comment to post | While not logged in navigate to post, attempt to leave comment | Message revealed "Please log in to add a comment." | Pass |


[Back to contents](#contents)

### User Stories Testing

| User Story ID  | As a/an  | I want to be able to...  | So that I can... | Testing | Pass/Fail |
|-------------------|-------------------|-----------------|-------------------|-------------------|---------------|
| Viewing Products & Navigation |
| 1  | User/Shopper | view individual products | identify their qualities and compare. | View Products Page | Pass |
| 2  |   | be able to add, edit quantity and remove items from my bag | buy them if after browsing. | Add product to bag, update item quantity, remove from bag | Pass |
| 3  |   | see any special offers | take advantage of saving money on products I'd like to buy. | Navigation bar displays free shipping if shopper spends £50 or more | Pass |
| 4  |   | gain inspiration from the blog | decide what to buy and make next. | Blog Page displays knitted goods with comments linking products to the store | Pass |
| 5  |   | add posts to the blog | show other users what I have made and gain their opinions through comments. | Blog add to post function allows users to add posts to the blog | Pass |
| Registration and Accounts |
| 6  | User/Shopper | register for an account | keep track of my orders and check my personal details. | Users can register for an account and view their orders in the profile page | Pass |
| 7  |   | receive email confirmation upon signing up | verify my set up was successful. | User receives email when they register for an account | Pass |
| 8  |   | be able to reset my password in case I forget it | gain access to my account. | User can request email to reset their password | Pass |
| 9  |   | have the ability to log in to the site with my details | view my orders and personal details | Users can log in using their registered details and view their orders and personal details | Pass |
| 10  |   | update my personal details | keep them up to date. | Users can update their personal details in the profile section | Pass |
| 11 |   | purchase from the site without having to create an account | check out quickly and easily. | Users can use the checkout without registering for an account | Pass |
| 12  |   | have the ability to register to the site if I choose | easily to access my account and orders. | Users can register to create an account to see orders |
| Searching products |
| 13  | User/Shopper | search for specific products | find products I am interested in buying. | Users can search on the site for products and if no product available message to confirm this | Pass |
| 14  |   | easily understand the search results | quickly decide which product I want to buy. | Users can search for products and quickly see how many match their criteria | Pass |
| 15  |   | sort by price, name, category | view a wide range and choose which to buy. | Users can sort by price, name and category on the products page | Pass |
| Checkout  |
| 16  | Shopper | have a running total of my bag | stay within my budget. | Users can see the total in the bag icon on the navbar | Pass |
| 17  |   | view my bag contents | keep track of which products I have selected. | Users can view their bag to see which products and quantities have been added | Pass |
| 18  |   | easily select the correct size | ensure I have ordered the right size for my project. | Users use the dropdown to select the required size/weight and this is confirmed in the bag| Pass |
| 19  |   | adjust the quantity of products to buy | update the order without going back to the product page. | Users can update quantities in the shopping bag successfully | Pass |
| 20  |   | easily enter my payment details | checkout as quickly and easily as possible. | Users can navigate the checkout form payment input easily | Pass |
| 21  |   | view the full order before entering card details | check it before confirmation. | The Order can be viewed on the checkout page before entering card details | Pass |
| 22  |   | receive email notifications when I make an order | confirm my order has been placed and refer back to. | Users receive an email when they make an order | Pass |
| Admin/Management  |
| 23  | Store owner/Admin | add a product | sell new items in my store  | Super users can add a product | Pass |
| 24  |   | update a product | change descriptions, sizes, images in my store. | Super users can edit a product | Pass |
| 25  |   | delete a product | remove items no longer on sale. | Super users can delete a product | Pass |

### **Wave**

The site was inspected for accessibility using the [Wave Browser Extension](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh) and changes made to HTML following this inspection. 




[Back to contents](#contents)