
# Joshi Collector

![Logo](https://i.imgur.com/I0IYZd2.png)

The concept is a card collecting app for fans of Joshi Puroresu / Women's Wrestling.

Users will be able to sign up, collect their favourite joshis, and add bookings to keep them happy.


# Icebox and Lessons Learned

https://joshicollector.herokuapp.com/

Full disclosure - this is actually a full-CRUD app built using Python3, PostgreSQL, and Django that is being dressed up as a card collector game.

This app was created purely for educational purposes as I learn this tech stack.

Realistically, there are many things that would need to be done to gamify the app. 

There will need to be some changes made to the data structure to allow users to collect and manage each card individually.

I intend to add this functionality in the future, and deploy a full working app with a seeded database containing cards to demonstrate the concept as a portfolio piece.

Nevertheless, this was a super fun way to implement CRUD on a new-to-me tech stack.




## Tech Stack

**Languages Used:** Python3 w/ traces of JavaScript and HTML

**CSS:** Materialize CSS + custom CSS

**Framework:** Django

**Database:** PostgreSQL


## Screenshots from Development and Feature Descriptions

![](https://i.imgur.com/KysOPmq.png)
Home Page - navigate through the dropdown menu.

![](https://i.imgur.com/Hl26ZRd.png)
Add a Joshi - enter a Joshi's details including ratings for skill attributes.

![](https://i.imgur.com/siBP235.png)
Joshi Detail Page - once created, a photo can be uploaded to the detail page. A single photo is allowed per page. Skill ratings will also be averaged to provide an overall rating. Congratulations, you've added a top talent to your collection. Don't leave them hanging, or they might start questioning how they are being utilized.

![](https://i.imgur.com/iHDtuV1.png)
Joshi Detail Page - available bookings include Dojo Training, match types including Singles, Tag, Unit and Gimmick Matches, Media Appearances, and In-Ring Promos.

![](https://i.imgur.com/D0MkuBG.png)
Joshi Detail Page - once a Joshi has been booked at least 3 times in a day, they will be satisfied with their role. Still paying attention? You might have noticed the age for this Joshi is unknown. The time honoured tradition of a Joshi's age no longer being mentioned after reaching 30 is adhered to on Joshi Collector.

![](https://i.imgur.com/vAnkcnx.png)
Item List View - users can also add items to be collected by Joshis. This can range from weapons, to title belts, to costumes. There is no limit to the creativity allowed. In a deployed product, there  would be seeded items available with the future intent of including photos and adding functionality for the items to increase various attribute ratings.

![](https://i.imgur.com/Wk8lRVN.png)
Items on Joshi Detail Page - once items are added, they will be available to be added or removed from individual Joshis as needed.




## Usage/Examples

Models.py
![App Screenshot](https://i.imgur.com/6aE4YC5.png)


## Authors

- [Anthony Vanoni](https://www.linkedin.com/in/anthony-vanoni/)


## Acknowledgements

 My instructor at General Assembly made the joke when assigning this lab that I would probably do a wrestler collector app. 

 That set the wheels in motion, and I put together the concept for this Joshi Collector card app.

 That being said, I do not own the rights for any of the performers in the development samples and have used this purely for educational purposes.

 Please support the talent via their social and YouTube content, and consider subscribing to [Stardom World](https://www.stardom-world.com) for the best in Joshi Puroresu.


## Feedback

If you have any feedback, please reach out at tony.vanoni@outlook.com


## 🚀 About Me
I've been somewhere in the middle of creative and technical my whole life. Full-stack development has proven to be the outlet for both that I was always looking for. I have recently graduated from a remote flex immersive through General Assembly, where I gained skills and experience in developing full-stack applications. Some of my favourite technologies include Node.js, Express.js, Django, and MongoDB.

