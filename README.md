# COSC310 Ryder Van Oerle Chatbot
## Project Description
The purpose of this project is to create a customer service chat bot agent which will communicate with basic canned sentences. The chat bot will offer the opportunity for users to leave reviews or return specific products from its online store. This conversation between the user and chat bot is “smooth,” and provides the user with a realistic customer service conversation which can undergo 30 or more turns of dialogue. I have also implemented the Google Places and Geocoding API to display 5 electronic stores near the users address.

To develop this software, our team decided to work with the Agile Scrum SDLC. The rationale behind choosing Scrum is because we wanted to follow a model that allows the flexibility to monitor the software development as the project is being developed throughout the term. Utilizing Scrum will allow the team to provide feedback throughout any stage of the project and iterate accordingly.

## Installation and Running the Chat Bot
Either download this repository or clone it to your desired directory with 
```git clone https://github.com/rvanoerle/chatbot_finalproj``` 
in the command line

### Create Virtual Environment (A3)
```
cd chatbot_team1_chatbot
python -m env chat_env
```
### Activate Virtual Environment (A3)
```
chat_env\Scripts\activate
```
![image](https://user-imag
es.githubusercontent.com/61817636/158919972-9e390d45-5a4e-44e0-af77-280f602a2482.png)

### Install PyTorch NLTK and GoogleMaps (A4)
For PyTorch Installation, follow this [link](https://pytorch.org/get-started/locally/)
![image](https://user-images.githubusercontent.com/61817636/158920135-d7c2b190-74a5-49c8-a346-c43ca8e1eae4.png)

For NLTK, run the following commands in your CLI:
```pip install googlemaps ```

For NLTK, run the following commands in your CLI:
```pip install nltk```

If you get an error trying to run the program, run the following:
```$ python
>>> import nltk
>>> import nltk.download('all')
```
![image](https://user-images.githubusercontent.com/61817636/158920100-f462feea-6512-4bf1-a4b5-47d7d22e4503.png)

### Running Bot
First, run:
```python train.py```

Then, run app.py to start the chat bot:
```python app.py```

## Conversation Flow (A3)
![image](https://user-images.githubusercontent.com/61817636/158088234-0a9e4185-52a1-454f-b4da-4a337ee09f65.png)

## Example (A4)
![image](https://user-images.githubusercontent.com/75710067/162855888-f5eed1d3-d5ea-467f-804a-f93c0fa8e591.PNG)

### Demo (A4)
https://user-images.githubusercontent.com/75710067/162860687-634bb4b9-e03d-43c5-9328-f239bd1b154f.mp4

## Coversation Structure

```
"tag": "service_review_received",
"patterns": [
          All of the user inputs which can be classified under the tag
        ],
        "responses": [
          All the responses which the bot can choose from
          ]
      }
```
### Opening and API Conversation
```
"Hello, please enter your address to view nearby stores to purchase one of our products."
 Customer inputted address
 Display list of stores
 "Would you like to discuss a product or a service?"

### Product Conversation
```
"tag": "product_initial",
"patterns": [
          "product"
          "Discuss a product please",
          "I'd like to discuss a Product",
          "I would like to discuss a product",
          "Can we discuss a Product",
          "Discuss"
        ],
        "responses": [
          "Sounds good! Would you like to leave a review or receive a refund on your most recently purchased product?",
          "Okay. Would you like to leave a review or receive a refund for the last product you purchased?"
        ]
```
### Product Review
```
"tag": "product_review",
"patterns": [
          "review"
          "I would like to leave a Product review please",
          "Product review",
          "Can I leave a product review",
          "Can I review a product"
        ],
        "responses": [
          "Sounds good. Please begin your review with 'Product Review _', where the underline signifies a rating from 1 - 5 stars",
          "Okay. Please begin your review with 'Product Review _', where the underline signifies a rating from 1 - 5 stars",
          "Will do. Please begin your review with 'Product Review _', where the underline signifies a rating from 1 - 5 stars"
        ]
```
### Product Received
```
"tag": "product_review_received",
"patterns": [
          "Product Review 0",
          "Product Review 1",
          "Product Review 2",
          "Product Review 3",
          "Product Review 4",
          "Product Review 5",
          "Product Review"
        ],
        "responses": [
          "Thank you for your review! Would you like to discuss another product or service? Remember to type 'quit' to leave at any time",
          "Your review has been saved! Would you like to discuss another product or service? Remember to type 'quit' to leave at any time",
          "We have received your review! Would you like to discuss another product or service? Remember to type 'quit' to leave at any time"
        ]
```
## Product Refund
```
"tag": "product_refund",
"patterns": [
          "I would like to a refund please",
          "Can I get a refund",
          "refund"
        ],
        "responses": [
          "Sounds good. Alright, we will send you an email with the next steps. Would you like to discuss another product or service? Remember to type 'quit' to leave at any time?",
          "Okay. Alright, we will send you an email with the next steps. Would you like to discuss another product or service? Remember to type 'quit' to leave at any time?",
          "Will do. Alright, we will send you an email with the next steps. Would you like to discuss another product or service? Remember to type 'quit' to leave at any time?"
        ]
```
## Service Conversation
```
"tag": "service_initial",
"patterns": [
          "Service please",
          "I'd like to review a service",
          "Can I review a service",
          "Service review"
        ],
        "responses": [
          "Sounds good! Which of the following services would you like to review? \n - Massage \n - Haircuts \n - Pedicures",
          "Okay! Which of the following services would you like to review? \n - Massage \n - Haircuts \n - Pedicures",
          "Will do! Which of the following services would you like to review? \n - Massage \n - Haircuts \n - Pedicures"
        ]
```
## Service Review
```
"tag": "service_review",
"patterns": [
          "I would like to leave a review for the massage please",
          "I would like to leave a review for the haircut please",
          "I would like to leave a review for the pedicure please",
          "Massage",
          "Haircuts",
          "Pedicures",
          "Can I leave a massage review",
          "Can I leave a haircut review",
          "Can I leave a pedicure review"
        ],
        "responses": [
          "Sounds good. Please begin your review with 'Service Review _', where the underline signifies a rating from 1 - 5 stars",
          "Okay. Please begin your review with 'Service Review _', where the underline signifies a rating from 1 - 5 stars",
          "Will do. Please begin your review with 'Service Review _', where the underline signifies a rating from 1 - 5 stars"
        ]
```
## Service Review Received
```
"tag": "service_review_received",
"patterns": [
          "Service Review 0",
          "Service Review 1",
          "Service Review 2",
          "Service Review 3",
          "Service Review 4",
          "Service Review 5",
          "Service Review"
        ],
        "responses": [
          "Thank you for your review! If you liked their service, you can specify you want Mary for your next visit. Would you like to discuss another product or service? Remember to type 'quit' to leave at any time?",
          "Your review has been saved! If you liked their service, you can specify you want James for your next visit. Would you like to discuss another product or service? Remember to type 'quit' to leave at any time?",
          "We have received your review! If you liked their service, you can specify you want John for your next visit. Would you like to discuss another product or service? Remember to type 'quit' to leave at any time?"
        ]
      }
```
## New Features (A4)
- Google Geocoding API:
  * This was implemented for when a user enters there general address, we are able to use the API to get and return the relative coordinates.
- Google Places API:
  * This was implemented to produce a list of 5 close electronic stores that the user may purchase an item at. Because this API requires coordinates, they are taken from the Geocoding API.
 
### Sample output with user typos
![image](https://user-images.githubusercontent.com/61817636/158089817-452c73b5-2784-42f7-bb00-f37168f8d502.png)

## References (A4)
To implement the Google API's, the following resources were used:
- [Places API - Google Developers Documenation](https://developers.google.com/maps/documentation/places/web-service)
- [How to Use Google Places API In Python - YouTube](https://www.youtube.com/watch?v=qkSmuquMueA)
- [Geocoding API - Google Developers Documentation](https://developers.google.com/maps/documentation/geocoding)
- [Getting Started with Google Geocoding API - YouTube](https://www.youtube.com/watch?v=d1QGLwie9YU)
