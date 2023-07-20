# The Woodshed Custom API

Welcome to the readme for <em><strong>['The Woodshed'](https://the-woodshed.herokuapp.com/)</strong></em> project. This repo is the back-end custom API for the REACT front-end.

<hr>
<image src="readme-files/amiresponsive.png">
<hr><br/>

The documentation for the REACT front-end side of this project can be found here:<br/>
<em><strong>--> [REACT Front-end repository and readme](https://github.com/NickWaldock/the-woodshed)</strong></em>

[Click here to view the live site](https://the-woodshed.herokuapp.com/)
<hr><br>

# Table of Contents

1. [Introduction](#introduction)

<br>

2. [Project Development](#project-development)
    - 2.1 [Repositories & Project Boards](#repos--project-links)
    - 2.2 [Aims](#aims)
    - 2.3 [Milestones](#milestones)
    - 2.4 [User Stories](#user-stories)
    
<br>

3. [Database](#database)
    - 3.1 [Database Schema](#database-schema)
    - 3.2 [CRUD Functionality](#crud-functionality)
    - 3.3 [Technologies](#technologies)

<br>

4. [Models](#models)
    - 4.1 [User Model](#user-model)
    - 4.2 [Profile Model](#profile-model)
    - 4.3 [Post Model](#post-model)
    - 4.4 [Comment Model](#comment-model)
    - 4.5 [Like Model](#like-model)
    - 4.6 [Follower Model](#follower-model)

<br>

5. [Testing](#testing)
    - 5.1 [Pep8 Validation](#pep8-validation)
    - 5.2 [Manual Testing](#manual-testing)

<br>

6. [Deployment](#deployment)
    - 6.1 [Cloudinary](#cloudinary-1)
    - 6.2 [PostgreSQL](#postgresql)
    - 6.3 [Heroku](#heroku)
    - 6.4 [Forking](#forking)
    - 6.5 [Cloning](#cloning)

<br>

7. [References & Acknowledgements](#references--acknowledgements)
    - 7.1 [References](#references)
    - 7.2 [Acknowledgements](#acknowledgements)

<hr><br>

# Introduction

The Woodshed API is a custom Application Programming Interface that facilitates a multi-user file sharing  platform designed to allow musicians to share, like, and comment on PDF files relating to musical practice. 

This project supports a React front-end application called [The Woodshed](https://the-woodshed.herokuapp.com/) but is also available as a custom API for related projects by 3rd parties.

The name of the site refers to the colloquial term _'woodshedding'_ which is often used by musicians to mean spending time in the practice room. This originates in old jazz vernacular meaning the musician should go to the woodshed, a solitary place where no-one can hear you continually get it wrong for your sake and theirs(!), until they can play the passage correctly and are ready to return. In modern times the term is now used commonly to deonte spending time practicing.

In the digital age PDFs are common as resources amongst musicians and music teachers alike. And with the large demand for online music lessons increasing during the 2020 pandemic the demand to share resources online increase.

The Woodshed API attempts to act as a starting point for anyone attempting to create their own music-based file sharing platform and is able to be easily built upon for scaling and further development purposes.

This API allows users to create an account, profile, and share PDF files as well as interact in the environment through likes, comments, and following users.

The Woodshed API has been created as part of the 5th portfolio project for the [Code Institue](https://codeinstitute.net) Full Stack Software Development Diploma and has no intended commerical purpose.
<br><hr>

# Project Development

## Repos & Project Links
- [The Woodshed REACT Front-end Repository](https://github.com/NickWaldock/the-woodshed)
- [The Woodshed LIVE Site](https://the-woodshed.herokuapp.com/)
- [Front-end Project Board](https://github.com/users/NickWaldock/projects/7)<br><br>
- [Back-end Project Board](https://github.com/users/NickWaldock/projects/6)<br><br>
- [Github Profile](https://github.com/NickWaldock)
<br><br><hr>

## Aims

- Build a Back-End for a Full-Stack web application that allows users to store and manipulate data records about a particular domain

- Design a database structure to handle the requirement of the front-end

- Records in the API must have full CRUD functionality

- Users need to have relevant access permissions and not have access to restricted data

- Be a reusable, scalable, and customisable API
<br /><br /><hr /><br>


## Milestones
The [Milestones](https://github.com/NickWaldock/the-woodshed-api/milestones) for the back-end development were managed seperately but were similar in scope to the front-end.
- <strong>Authentication & Profiles</strong>
	- Relating to creation of user accounts and profile and thier authentication<br><br>

- <strong>CRUD Functionality</strong>
	- Relating to the ability to Create, Read, Update, or Delete database instances<br><br>

- <strong>User Interactivity</strong>
	- Relating to a single user instance interacting with the property of a different user instance<br><br>

- <strong>Forms</strong>
	- Relating to front-end submittable forms that parse data to the API<br><br>

- <strong>Deployment</strong>
	- Relating to deploying the API after development<br><br>

- <strong>Bugs</strong>
	- Documentation of Bugs and Issues<br><br>

- <strong>Documentation</strong>
	- Documentation tasks
<br><br><hr>


## User Stories
User stories were mapped to [milestones](#milestones) in the [project Kanban Board](https://github.com/users/NickWaldock/projects/6/views/2)

<strong>Authenticatin & Profiles</strong>

- As a user, I should only be able to edit or delete my own posts, comments, and profile
- As a user, I want to be able to create a profile
- As a user, I want to be able to edit my profile
- As a user, I want to be able to see the details and data of individual profiles
- As a user, I want to be able to log in and out
- As a user, I want to be able to view user profiles
- As a user, I want to be able to add picture to my profile
- As a site owner, I want the API to be configured to allow a user to stay logged in


<strong>CRUD Functionality</strong>
- As a user, I want to be able to view posts
- As a user, I want to be able to edit or delete my posts
- As a user, I want to be able to search posts using a search bar


<strong>User Interactivity</strong>
- As a user, I want to be able to add comments to a post
- As a user, I want to be able to read comments on a post
As a user, I want to be able to follow and unfollow other users
- As a user, I want to be able to like and unlike posts
- As a user, I want to be able to see how many likes and comments a post has
- As a user, I want to be able to see how many followers a profile has, how many posts, and how many users that profile is following

<strong>Deployment</strong>
- As a site owner, I need the API to be deployed to an external server
<br><hr>

# Database
[Django REST Framework](https://www.django-rest-framework.org/) was utilised for building this custom API
<br>
[ElephantSQL](https://www.elephantsql.com/) was used to host and manage the PostgreSQL database. The database works in tandem with a [REACT front-end application](https://github.com/NickWaldock/the-woodshed) to manage and store data delivered via the API
<br/><br>

## Database Schema
The following database design was decided upon during development to facilitate reaching the project's purpose and [aims](#aims)

<br>
<image src="readme-files/database.png" width=70%><br>

<em>*Database schema created using [LucidChart](https://www.lucidchart.come)</em><br><br>

## CRUD Functionality

This project incorporates CRUD (Create, Read, Update, Delete) functionality as a key feature. Users will need to be able to create, edit and update existing elements, and finally delete any created content. All content stored in the back-end is to be kept updated in the front-end rendering so changes remain apparent to the user.
<br/><hr>

## Technologies

Built using: [React](https://react.dev/), [Django Rest Framework](https://www.django-rest-framework.org/), [React Bootstrap](https://react-bootstrap.netlify.app/), [CSS](https://www.w3.org/Style/CSS/Overview.en.html#:~:text=Cascading%20Style%20Sheets%20(CSS)%20is,CSS%20and%20on%20available%20software.), and [HTML(JSX)](https://www.w3schools.com/react/react_jsx.asp), as well as [Cloudinary](https://cloudinary.com/) for image and file storage, [ElephantSQL](https://www.elephantsql.com/) for database management, and [Heroku](https://www.heroku.com/) for deployment hosting.
<br><br><hr>

## [Django Rest Framework](https://www.django-rest-framework.org/)
The custom API was constructed using DRF, a [Django](https://www.djangoproject.com/) framework built using the [Python](https://www.python.org/) programming language. DRF is a popular framework for developing web application APIs and includes features such as [serialization](https://www.django-rest-framework.org/api-guide/serializers/) which <em>"allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types after first validating the incoming data."</em>

### [Django Rest Auth](https://django-rest-auth.readthedocs.io/en/latest/)
Creates DRF API endpoints for handling user registration, essentially givig a user site credentials to that can be validated by Django Allauth (below)

### [Django All Auth](https://django-rest-auth.readthedocs.io/en/latest/index.html)
A [DRF](https://www.django-rest-framework.org/) library that handles user registration and authentication tasks and additional user management requirements

### [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) 
A [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token) authentication plugin for [DRF](https://www.django-rest-framework.org/). It provides user authentication communication between the client in the front-end and server in the back-end so the user can be validated to access the features of the application
<br><br>

## Cloudinary
[Cloudinary](https://cloudinary.com/) is a cloud-based image and file hosting site. In this project all profile images and PDF files are stored on this platform. URLs for files are saved to the relevant database instances 

For steps on using Cloudinary for your version of this project click [here](#deployment)
<br><br><hr>

# Models
In order to fulfil the requirements of the project, database [models](https://docs.djangoproject.com/en/4.2/topics/db/models/) would be required to store data. The following are the models created and used by the API to allow the users to interact with and manipulate data on the site.<br><br>

## <ins>***User Model***
[Django Auth](https://docs.djangoproject.com/en/4.2/topics/auth/) is a built in Django library that automatically manages all user creation, authorisation and authentication. This was utilised to handle the heavy lifting of user management. Features include password checking, permissions, and user management through the admin panel.<br><br>


## <ins>***Profile Model***
<image src="readme-files/models/profile-model.png" width=70%><br>

- The Profile model relates to the <a href="#user">User</a> django auth package via the <strong><em>`owner`</em></strong> model attribute in a one-to-one relationship. Meaning a user can only have a single profile linked to its instance within the application<br><br>
- <strong><em>'created_at'</em></strong>
([Date Time Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#datetimefield)) timestamps that will be automatically added to the creation of the user. This data is not currently being viewed in the front-end but is available to view in the back-end admin panel (this feature has been noted as a <a href="#future-developments">future development</a>). The `auto_now_add=True` setting gets the current date and time, setting the intital date time value for the instance<br><br>
- <strong><em>'updated_at'</em></strong>
([Date Time Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#datetimefield)) timestamps that will be automatically added to the updating of the profile. This data is not currently being viewed in the front-end but is available to view in the back-end admin panel (this feature has been noted as a <a href="#future-developments">future development</a>). The `auto_now=True` setting gets the current time.<br><br>
- <strong><em>'name'</em></strong>
([Character Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#charfield)) is the attribute for the user to add optionally in the front-end. One of the remits for the site is that users will eventually be able to use it to find new contacts/students. This field has been added to allow the user to add their real name to the site if they so choose. This will be an optional field with the form permissions handled in the front-end<br><br>
- <strong><em>'description'</em></strong>
([Text Field](https://docs.djangoproject.com/en/4.2/ref/models/fields/#textfield)) Biographical info can be added here to give context for other users as to who this profile is for, why they are there, and what their experience is and what they are likey to be posting about<br><br>
- <strong><em>'headline'</em></strong> is a short (maximum of 80 characters, 
[Character Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#charfield)) text string which aims to be an attention-grabber for when a user views a profile. Inspiration for this comes from the popular social media site [Twitter](https://twitter.com)<br><br>
- <strong><em>'instrument'</em></strong>
([Character Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#charfield)) means the user can add thier instrumental specialisms to their profile, giving context to the content they are likely to share. [Future developments](#future-developments) will offer dedicated pages for searching instrument specific content or users<br><br>
- <strong><em>'location'</em></strong>
([Character Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#charfield)) Allows users to input their location. This is only intended as a general location and not a specific location, e.g. 'New York', or 'Manchester'. This is biograpical data that may in [future developments](#future-developments) utilise a google maps feature, or feature where users can search for profiles based on general geo-location<br><br>
- <strong><em>'email'</em></strong>
([Email Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#emailfield)) Caputures a valid email with Django's automatic [email validator](https://docs.djangoproject.com/en/4.2/ref/validators/#django.core.validators.EmailValidator) and displays an error if the user input doesn't conform to this. Like the name attribute this will be an optional field with this permission handled in the front-end<br><br>
- <strong><em>'image'</em></strong>
([Image Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#imagefield)) This allows the user to upload a profile image which becomes the user's '[Avatar](#)' in the front-end. Images are stored on the cloud file storage service [Cloudinary](https://cloudinary.com). When a user first creates an account they are designated a temporary profile image until they upload their own. Django's image form field uses [Pillow](https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html), a [file extension validator](https://docs.djangoproject.com/en/4.2/ref/validators/#django.core.validators.FileExtensionValidator) to determine valid image files
<br><br>

## <ins>***Post Model***
<image src="readme-files/models/post-model.png" width=70%><br>

- <strong><em>'owner'</em></strong>
([Foreign Key](https://docs.djangoproject.com/en/4.2/ref/models/fields/#foreignkey)) is a Many to One relationship with the `User` model. A single use can own and have multiple post instances related to it. Also links to the `owner` attribute in the [profile model](#profile-model). The `on_delete=models.CASCADE` setting means all posts related to this profile will be deleted if the user is deleted. <em>*Note: If the `profile` instance is seperate from the user model, if the profile instance is deleted and not the <em>user</em> instance then the post data will continue to exist</em><br>

- <strong><em>'created_at'</em></strong> 
([Date Time Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#datetimefield)) logs the time the post instance was created and uploaded to the database. This data will be used in the front-end to display a date of creation on the post component. This attribute will be the date shown unless the post is later updated, in which case the updated date will display. The `auto_now_add=True` setting gets the current date and time, setting the intital date time value for the instance<br>

- <strong><em>'updated_at'</em></strong>
 ([Date Time Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#datetimefield)) logs the time the post instance was updated by the user and uploaded to the database. This value will display and be the dominant data timestamp for the post instance instead of the above `created_at` field. This is so in the front-end posts can be filtered by the most recently updated<br>

- <strong><em>'title'</em></strong> 
([Character Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#charfield)) is the main title of a post. This field is searchable by the user in the [Search Bar]() component<br>

- <strong><em>'subtitle'</em></strong> 
([Character Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#charfield)) this is the subtitle of a post, for the user to expand on the main post title with engaging but brief informational context to encourage a user to view the rest of the content, similar to purpose of the [Headline](#profile-model). This is a searchable field in the [Search Bar]() component<br>

- <strong><em>'description'</em></strong> 
as a ([Text Field](https://docs.djangoproject.com/en/4.2/ref/models/fields/#textfield)) alllows the user to add more detailed information and allows for more data input than a `CharField`. This is where the bulk of information relating to the post will reside. Users can add specific and detailed instructions to posts and further context in th epurpose of the post and using the PDF file. Including: notes, how-to-use, suggestions, etc<br>

- <strong><em>'instrument'</em></strong> 
([Character Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#charfield)) allows the user to add a list of instruments that the post is designed to be used for in practice. This is a searchable field in the [Search Bar]() component<br>

- <strong><em>'tags'</em></strong> 
([Character Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#charfield)) allows the user to add a list of key word tags to the post. This is a searchable field in the [Search Bar]() component<br>

- <strong><em>'file'</em></strong> 
([File Field](https://docs.djangoproject.com/en/4.2/ref/models/fields/#filefield)) is the primary purpose of the site, to upload and share PDFs documents. Here the user can upload only a PDF file, as the vast majority of musical performance, practice, and education digital content is shared as PDF files, it prudent for the early stages of this project to keep file formats singularly to PDFs to help with site formating and previewing. Files are stored in the [Cloudinary](https://cloudinary.com) cloud file storage service via the `upload_to` attribute.

  `validators=[FileExtensionValidator(allowed_extensions=['pdf'])]`
  This snippet of code in the model handles the post upload authentication for file types by only accepting files with a suffix of .pdf. This will need to be further addressed as a [future development](#future-developments) as this kind of file validation will not discourage users from attempting to circumvent the validation by uploading files where the file suffix has been manually changed to ".pdf" when the file is <em>not</em> actually in a PDF format. This behaviour would likely cause rendering errors. Additional file types would need to be included as valid filetypes in teh project, or more robust file validation
<br>
- <strong><em>Ordering</em></strong>: Posts display with the most recent date stamp first with the following code:
```python
class Meta:
   ordering = ['-created_at']
```
<br>

## <ins>***Comment Model***
<image src="readme-files/models/comment-model.png" width=70%><br>

- <strong><em>'owner'</em></strong> 
([Foreign Key](https://docs.djangoproject.com/en/4.2/ref/models/fields/#foreignkey)) links a single comment to a single `User` via a `Foreign Key`. A user can own multiple comments on any post instance. `User, on_delete=CASCADE` means if a `User` instance is deleted, all comments owned by that user will also be deleted<br>

- <strong><em>'post'</em></strong> 
([Foreign Key](https://docs.djangoproject.com/en/4.2/ref/models/fields/#foreignkey)) links a comment instance to a `Post` instance creating a relationship for the comment to exist only with a certain post, this is done similarily via the `Foregin Key` relationship. `Post, on_delete=CASCADE` means that if a post is deleted, all comments directly related to that post will be deleted<br>

- <strong><em>'created_at'</em></strong> 
([Date Time Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#datetimefield)) time stamps the creation of the comment with the current time. Similarly to the same action in the [Post Model](#post-model). This time stamp will displayed as 'time elapsed since posting' in the comment component so users can see how long ago comment was created<br>

- <strong><em>'updated_at'</em></strong> 
([Date Time Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#datetimefield)) time stamps the current time the comment was updated. Similarly to the same attribute in the [Post Model](#post-model).  This time stamp will displayed as 'time elapsed since posting' in the comment component so users can see how long ago comment was created and will override the `created_at` time stamp<br>

- <strong><em>'content'</em></strong> 
([Text Field](https://docs.djangoproject.com/en/4.2/ref/models/fields/#textfield)) is where the main text content of the comment is stored<br>

- <strong><em>Ordering</em></strong>: Posts display with the most recent date stamp first with the following code:
```python
class Meta:
   ordering = ['-created_at']
```
<br>

## <ins>***Like Model***
<image src="readme-files/models/like-model.png" width=70%><br>

- <strong><em>'owner'</em></strong> 
([Foreign Key](https://docs.djangoproject.com/en/4.2/ref/models/fields/#foreignkey)) links a like instance to a single `User` via a `Foreign Key`. A user can 'like' multiple `Post` instances. `User, on_delete=CASCADE` means if a `User` instance is deleted, all 'likes' owned by that user on any post in the database will also be deleted. With this, it can be possible to view all posts that a user has 'liked'.<br>

- <strong><em>'post'</em></strong> 
([Foreign Key](https://docs.djangoproject.com/en/4.2/ref/models/fields/#foreignkey)) links a 'like' instance to a `Post` instance creating a relationship for the 'like' to exist only with a certain post, this is done similarily via the `Foregin Key` relationship. `Post, on_delete=CASCADE` means that if a post is deleted, all 'likes' directly related to that post will be deleted for any relevant `Users`<br>

- <strong><em>'created_at'</em></strong> 
([Date Time Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#datetimefield)) creates a current time stamp for when a `User` has 'liked' a post. <em>*Note: This field does not require an `updated_at` model attribute. This is because a 'like' instance will either exist or not. If a user is to 'unlike' a post, the 'like' instance is removed completely and not updated. A repeated 'like' action will create a new 'like' instance</em><br><br>

### <ins>***Follower Model***
<image src="readme-files/models/follower-model.png" width=70%><br>

- <strong><em>'owner'</em></strong> 
([Foreign Key](https://docs.djangoproject.com/en/4.2/ref/models/fields/#foreignkey)) links a follower instance to a single `User` via a `Foreign Key`. A `related_name='following` means that this relationship can be accessed in the front-end for data display to show which profiles this singular profile has chosen to link to or 'follow'. A user can 'follow' multiple profiles (or `owners`). `User, on_delete=CASCADE` means if a `User` instance is deleted, all 'follow' relationships creted by that user will also be deleted. This function allows us to filter posts from only profiles the current user is 'following'<br>

- <strong><em>'followed'</em></strong> 
([Foreign Key](https://docs.djangoproject.com/en/4.2/ref/models/fields/#foreignkey)) works similarly to the above attribute in that a relationship is created between a `User` who is being 'followed' by other profiles. The `related_name='followed'` means we can view how many other profiles have chosen to 'follow' <em>this</em> profile.

- <strong><em>'created_at'</em></strong> 
([Date Time Field](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#datetimefield)) provides a current time stamp when the relationship was established. <br><em>*Note: This field does not require an `updated_at` model attribute. This is because a 'like' instance will either exist or not. If a user is to 'unlike' a post, the 'like' instance is removed completely and not updated. A repeated 'like' action will create a new 'like' instance</em>
<br><br><hr>


# Testing

## PEP8 Validation
[PyCodeStyle](https://pycodestyle.pycqa.org/en/latest/intro.html) was used for python code validation, previously PEP8.

All custom Python passes validation.

## Manual Testing

Documented below are all the manual tests for the API endpoint that were undertaken and their results

<details>
<summary>Testing Endpoints</summary>
<br>

### Profiles
<table>
	<tr>
		<th>Test</th>
		<th>URL</th>
		<th>Procedure</th>
		<th>Result</th>
		<th>Data</th>
	</tr>
	<tr>
		<td>Create a new Profile/User</td>
		<td>/profiles/</td>
		<td>A POST request to this endpoint with the username data 'test123' should result in creation of new user of the same name. A new profile linked to the user is created and available for view. The image field contains the default image, the date of creation is stated, and all other fields are empty</td>
		<td>PASS</td>
        <td><image src="readme-files/testing/new-user.png"></image></td>
	</tr>
<tr>
		<td>Update a new Profile/User Instance</td>
		<td>/profiles/23</td>
		<td>When authenticatd, A PUT request to this endpoint with additional profile data should update the profile instance</td>
		<td>PASS</td>
        <td><image src="readme-files/testing/update-user.png"></image></td>
	</tr>
</table>

### Posts
<table>
	<tr>
		<td>Creating a New Post Instance</td>
		<td>/posts/create</td>
		<td>When authenticated, making a POST request to this endpoint will result in a new post instance being created with the inputted form data, the file is saved to the hosting platform</td>
		<td>PASS</td>
		<td><image src="readme-files/testing/new-post.png"></image></td>
	</tr>
	<tr>
		<td>Updating a Post Instance</td>
		<td>/posts/72/edit</td>
		<td>When authenticated, making a PUT request to this endpoint with the post id will update the post instance with the inputted form data</td>
		<td>PASS</td>
		<td><image src="readme-files/testing/update-post.png"></image></td>
	</tr>
	<tr>
		<td>Deleting a Post Instance</td>
		<td>/posts/72</td>
		<td>When authenticated, making a DELETE request to this endpoint will remove the post instance form the database</td>
		<td>PASS</td>
		<td><image src="readme-files/testing/delete-post.png"></image></td>
	</tr>
	<tr>
		<td>Listing Post Instances</td>
		<td>/posts/</td>
		<td>When authenticated, sending a GET request to this endpoint will retireve all existing post instances</td>
		<td>PASS</td>
		<td><image src="readme-files/testing/posts-list.png"></image></td>
	</tr>	
	<tr>
		<td>Post Like Relationship</td>
		<td>/posts/72</td>
		<td>When authenticated, 'liking' a post sends a PUT request to that post's instance, incrementing the "like_count" field by 1</td>
		<td>PASS</td>
		<td><image src="readme-files/testing/post-relationship.png"></image></td>
	</tr>	
	<tr>
		<td>Post Comment Relationship</td>
		<td>/posts/72</td>
		<td>When authenticated, commenting on a post sends a PUT request to that post's instance, incrementing the "comments_count" by 1</td>
		<td>PASS</td>
		<td><image src="readme-files/testing/post-relationship.png"></image></td>
	</tr>	
</table>

### Likes
<table>
<tr>
		<td>Liking a Post Instance</td>
		<td>/likes/61</td>
		<td>When authenticated, 'liking' a post sends a POST request to this endpoint adding the relationship between the authenticated user's 'owner' field and the post id with the likes own unique id. An authenticated owner id that is the same as the post owner id cannot make this action (a user can't like their own post)</td>
		<td>PASS</td>
		<td><image src="readme-files/testing/like.png"></image></td>
	</tr>
<tr>
		<td>Unliking a Post Instance</td>
		<td>/likes/61</td>
		<td>When authenticated, 'liking' a post that already contains a like instance relationship sends a DELETE request to this endpoint, removing the relationship between the authenticated user id and the post id</td>
		<td>PASS</td>
		<td><image src="readme-files/testing/unlike.png"></image></td>
	</tr>
	<tr>
		<td>Like Relationships</td>
		<td>/likes/</td>
		<td>When authenticated, making a GET request to this endpoint will retrieve a list of all like relationships instnces</td>
		<td>PASS</td>
		<td><image src="readme-files/testing/likes.png"></image></td>
	</tr>
</table>

### Commenting
<table>
<tr>
		<td>Creating a Comment Instance</td>
		<td>/comments/27</td>
		<td>When authenticated, sending a POST request to this endpoint will result in a comment instance being created with its own unique id</td>
		<td>PASS</td>
		<td><image src="readme-files/testing/comment.png"></image></td>
	</tr>
	<tr>
		<td>Updating a Comment Instance</td>
		<td>/comments/72</td>
		<td>When authenticated, sending a PUT request to this endpoint will result in a comment instance with the same id being updated</td>
		<td>PASS</td>
		<td><image src="readme-files/testing/comment-update.png"></image></td>
	</tr>
<tr>
		<td>Deleting a Comment Instance</td>
		<td>/comments/72</td>
		<td>When authticated, sending a DELETE request to this endpoint will result in a comment with the related id being deleted</td>
		<td>PASS</td>
		<td><image src="readme-files/testing/delete-comment.png"></image></td>
	</tr>
</table>

### Following 
<table>
	<tr>
		<td>Following a Profile Relationship</td>
		<td>/followers/74</td>
		<td>When authenticated, following another profile will send a POST request to this endpoint creating a follower instance id</td>
		<td>PASS</td>
		<td><image src="readme-files/testing/follow-user.png"></image></td>
	</tr>
	<tr>
		<td>Reverting a Profile Follow Relationship</td>
		<td>/followers/74</td>
		<td>When authenticated, unfollowing another profile will send a DELETE request to this endpoint, removing the follower instance by id</td>
		<td>PASS</td>
		<td><image src="readme-files/testing/unfollow.png"></image></td>
	</tr>
<tr>
		<td>Being Followed by a Profile Relationship</td>
		<td>/profiles/23</td>
		<td>When authenticated, if another user has 'followed' the authenticated user's profile, the relationship is reflected in that profile's instance "followers_count" </td>
		<td>PASS</td>
		<td><image src="readme-files/testing/being-followed.png"></image></td>
	</tr>
</table>
</details>

<br><br><hr>

# Deployment

[The live site can be accessed here](https://the-woodshed.herokuapp.com/)
<br/><br/>
To create and deploy your own version of this application please follow the steps below.

## <ins>Cloudinary

1. Navigate to the [Cloudinary website](https://cloudinary.com/)
2. Log in or create and account
3. On the main console page click "Dashboard"
4. Here you will find all the information for the next steps

## <ins>PostgreSQL

1. Navigate to [ElephantSQL](https://www.elephantsql.com/) or another PostgresSQL database provider
2. Log in or create an account
3. Click "Create New Instance"
4. Add a name for your database, tags and a plan (Tiny Turtle is Free)
5. Click "Select Region"
6. Select your cloest region
7. Click Review
8. On the confirm page click "Create Instance"
9. Your database is now set up. Click on the name of your database in the dashboard to view all information for the next steps


## <ins>Heroku
To deploy the API to Heroku:
1. Log in to [Heroku](https://www.heroku.com/) (create an account if necessary)
2. From the dashboard, click on the "New" button and select "Create new app"
3. Choose an appropriate name for your app and select the region closest to your location
4. Access the "Settings" tab
5. Click on "Reveal Config Vars"
6. Add all necessary key-value pairs:<br>
<image src="readme-files/heroku-vars-backend.png">
<br/>
Required config vars:
- <strong>ALLOWED_HOST</strong> --> The URL of the back-end application
- <strong>CLIENT_ORIGIN</strong> --> The URL of the front-end application
- <strong>CLOUNDINARY_URL</strong> --> Available from Cloudinary (for image, file storage)
- <strong>DATASABE_URL</strong> --> Available from your SQL provider
- <strong>DISABLE_COLLECTSTATIC</strong> - "1"
- <strong>SECRET_KEY</strong> --> Django secret key, found in env.py file. Should be unique!

7. Access the "Deploy" tab
8. Select "GitHub - Connect to GitHub" from the deployment methods and click on "Connect to GitHub"
10. Search for the relevant GitHub repository and click it
11. Choose automatic deploys to allow the deployed site to be updated each time code is pushed to GiHub
12. Click "View" to view the deployed site. The back-end is now deployed!
<br><br>

## <ins>Forking
To fork this repository on [Github](https://github.com/NickWaldock/the-woodshed-api) proceed with the following steps:
1. Log it to GitHub (create an account if necessary)
2. Locate the [GitHub Respository](https://github.com/NickWaldock/the-woodshed-api)
3. On the repository page, find the 'Fork' menu in the top right, click on the small down arrow
4. Select '+ Create a new fork'
5. Remane repository as required
6. Click 'Create Fork'
7. You now have your forked version of this repository

<em>* Note * You can find the front-end repo for this project [here](https://github.com/NickWaldock/the-woodshed)</em>
<br />
<br />

## <ins>Cloning
To clone the repository procees with the following steps:
1. Log in to GitHub (create an account if necessary)
2. Locate the [GitHub Respository](https://github.com/NickWaldock/the-woodshed-api)
3. On the repository page, find and click on the 'Code' menu in the mid-top right of the page
4. Choose to either download or open in GitHub Desktop,
  - or;
    5. Choose the HTTPS option and copy the URL to your clipboard
    6. - To clone the repository using HTTPS, under "HTTPS", copy the url
       - To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then copy the url
       - To clone a repository using GitHub CLI, click GitHub CLI, then copy url
    7. Open Terminal and change the current directory to where you want the cloned directory
    8. Type git clone, and paste the url, press Enter to create your local clone
<br/><br/>

<em>* NOTE * You can find the front-end repo for this project [here](https://github.com/NickWaldock/the-woodshed)</em>
<hr><br /><br />

# References & Acknowledgements
## References

- [Moments (Code Institute Project)](https://codeinstitute.net/): this demo project was consulted in the creation of this project and expanded upon in the models

- [Using validators for file type (PDF)](https://stackoverflow.com/questions/69054680/safe-way-to-validate-file-extension-in-serializer-django): this page was consulted to help create the file validation


## Acknowledgements

I would like to thank my Code Institute Mentor Jubril Akolade for his time and expertise in guiding me through this project; the Code Institute tutors for thier continued support; and [Code Institute](https://codeinstitute.net/) for the Full Stack Software Developement Program that has taught me an inordinate amount about the world of software from scratch. I hope this project has been interesting and fun to engage with, if you would like to get in touch for collaborations you can reach me through my website [www.nicholasjameswaldock.uk](https://www.nicholasjameswaldock.uk) or through my [LinkedIn profile](https://www.linkedin.com/in/nicholas-waldock-05237071/). <br><br>Thanks for stopping by!