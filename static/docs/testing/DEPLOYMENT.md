# Deployment Steps

## **Contents**

- [**GitPod IDE**](#gitpod-ide)
- [**Heroku Deployment**](#heroku-deployment)
  - [**Connecting to Heroku**](#connecting-to-heroku)
  - [**Config Vars**](#config-vars)
  - [**Where to find Config Var Key-value Pairs**](#where-to-find-config-var-key-value-pairs)
- [**Design Choices**](#design-choices)
  - [**Fonts**](#fonts)
  - [**Colours**](#colours)
  - [**Imagery**](#imagery)
  - [**Wireframes**](#wireframes)


### **Gitpod IDE**


### **Heroku Deployment**

#### **Connecting to Heroku**

The project was developed using [GitPod](https://gitpod.io/) and pushed to [GitHub](https://github.com/) then deployed on Heroku using these instructions:

1. Log in to Heroku and create a new app by clicking "New" and "Create New App" and giving it an original name and setting the region to closest to your location.
2. Navigate to Heroku Resources and add Postgres using the free plan.
3. Create a requirements.txt file using command *pip3 freeze > requirements.txt*
4. Create a Procfile with the terminal command *web: gunicorn knit_happens.wsgi:application* and at this point checking the Procfile to make sure there is no extra blank line as this can cause issues when deploying to Heroku.
5. Use the loaddata command to load the fixtures for both json files: *python3 manage.py loaddata categories.json* and *python3 manage.py loaddata products.json*
6. If it returns error message: *django.db.utils.OperationalError: FATAL: role <somerandomletters> does not exist* run *unset PGHOSTADDR* in your terminal and run the commands in step 11 again.
7. From the CLI log in to Heroku using command *heroku login -i*.
8. Temporarily disable Collectstatic by running: *heroku:config:set DISABLE_COLLECTSTATIC=1 --app <heroku-app-name>* So that Heroku won't try to collect static files when we deploy.
9. Add Heroku app name to ALLOWED_HOSTS in settings.py.
10. Commit changes to GitHub using *git add .*, *git commit -m <commit message>*, *git push*.
11. Then deploy to Heroku using *git push heroku main*
If the git remote isn't initialised you may have to do that first by running *heroku git:remote -a <heroku-app-name>
12. Create a superuser using command: *heroku run python3 manage.py createsuperuser* so that you can log in to admin as required.
13. From Heroku dashboard click "Deploy" -> "Deployment Method" and select "GitHub"
14. Search for your GitHub repo and connect then Enable Automatic Deploys.
15. Generate secret key. Strong secret keys can be obtained from [MiniWebTool](https://miniwebtool.com/django-secret-key-generator/). This automatically generates a secret key 50 characters long with alphanumeric characters and symbols. 
16. Add secret key to GitPod variables and Heroku config vars.
17. Set up Amazon AWS S3 bucket using instructions [below](#amazon-aws)
18. In the dashboard click "Settings" -> "Reveal Config Vars"
19. Set [config vars](#config-vars) using advice below.


#### **Amazon AWS**

1. Create Amazon AWS account and create a new bucket in the S3 services and choose your closest region.
2. Uncheck block all public access and create bucket. 
3. From Properties tab turn on static website hosting using default values of index.html and errors.html.
4. On permissions tab include CORS configuration:
```python
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
5. Create security policy: S3 Bucket Policy, allow all principles by adding a * and Amazon S3 services and selecting Get Object action. Paste ARN from Bucket Policy, add statement, generate policy and copy and paste into Bucket Policy. Also add /* at end of resource key to allow use of all pages. 
6. Under public access select access to all List Objects. 

7. Create Group for the bucket through IAM. Create policy by importing AWS S3 Full Access policy and add ARN from bucket to the policy resources. Attach policy to group. 
8. Create user, give programmatic access and add user to the group. Download CSV file when prompted to save access key ID an secret access key to save to environment and config [variables](#config-vars).
9. Add AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME = 'eu-west-2' to settings.py.
10. Add, commit and push to GitHub then navigate to Heroku to confirm static files collected successfully on the Build Log.

#### **Email Client**


#### **Config Vars**

Table:

| Key                    | Value                      |
| ---------------------- |--------------------------- |
| PORT                   | 8000                      |
| IP                     | 0.0.0.0                   |
| SECRET_KEY             | YOUR_SECRET_KEY            |
| STRIPE_PUBLIC_KEY      | STRIPE_PUBLIC_KEY          |
| STRIPE_SECRET_KEY      | YOUR_STRIPE_SECRET_KEY     |
| STRIPE_WH_SECRET       | STRIPE_WEBHOOKS_KEY        |
| DATABASE_URL           | YOUR_POSTGRES_URL          |
| AWS_ACCESS_KEY_ID      | YOUR_AWS_ACCESS_KEY_ID     |
| AWS_SECRET_ACCESS_KEY  | YOUR_AWS_SECRET_ACCESS_KEY |   
| USE_AWS                | True                       |
| EMAIL_HOST_PASS        | YOUR_EMAIL_HOST_PASSCODE   |
| EMAIL_HOST_USER        | YOUR_EMAIL_HOST_USERNAME   |


#### Where to find Config Var Key-value Pairs 

To find the values of each key:

- SECRET_KEY: This is a random string provided when creating the Django project and can easily be changed to ensure extra security. 
- DATABASE_URL: This is temporary.
- STRIPE_PUBLIC_KEY: Retrived from Stripe Dashboard in the Developer's API section (Publishable key).
- STRIPE_SECRET_KEY: Retrived from Stripe Dashboard in the Developer's API section (Secret key)
- STRIPE_WH_SECRET: Retrived from Stripe Dashboard in the Developer's after creating an endpoint for your webhook (Signing secret).
- EMAIL_HOST_USER: Your email address or username. [See below for instructions](#smtp-setup).
- EMAIL_HOST_PASS: Your passcode from your email client. [See below for instructions](#smtp-setup).
- AWS_SECRET_ACCESS_KEY: From the CSV file that you download having created a User in Amazon AWS S3. [See below for instructions](#amazon-aws).
- AWS_ACCESS_KEY_ID: From the CSV file that you download having created a User in Amazon AWS S3. [See below for instructions](#amazon-aws).





### How to contribute to the site

1. Navigate to [GitHub](https://github.com/) and log in
2. Locate my [repo](https://github.com/suzybee1987/knit-happens)
3. On the right side of the screen click Fork
4. This creates a copy in your own repository to make changes in [GitPod](https://gitpod.io/)
5. Once finished with changes add, commit and push to your own [GitHub](https://github.com/)
6. Click Pull Requests and select "New Pull Request" button.


### How to run the project locally

To clone this project from GitHub follow the instructions taken from [GitHub Docs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) explained here:
1. Navigate to the [GitHub Repository](https://github.com/suzybee1987/knit-happens)
3. To clone using HTTPS click the clipboard symbol under "Clone with HTTPS". To clone using SSH key click Use SSH then click the clipboard symbol. To clone using GitHub CLI select Use GitHub CLI and click the clipboard symbol. 
4. Open Git Bash
5. Change the working directory to the location you want the cloned directory to be.
6. Type 'git clone' and paste the url copied from step 3. 
7. Press 'enter' to create your clone.

[Back to contents](#contents)