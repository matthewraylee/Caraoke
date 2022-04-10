# Caraoke
## Inspiration
Our team loves going on road trips, but we always felt something was missing during our journey. As we watch the scenery go by, we wanted to be singing along to our favorite tunes, but there are times when some of us are not familiar with the lyrics. This set of obstacles is what inspired us to use the power of Engineering and solve something that has bothered not just us, but some of you as well.

So we thought of Caraoke, a little Arduino machine that fits right into the air vents of our cars and lets us know the lyrics to any song that's playing on our Spotify application. In this way, everyone in the car gets to sing along to the same set of lyrics, as if we are in a karaoke bar. No phones, no-frills.


## What it does
Play a song on your Spotify and enjoy karaoke sessions in the car. 

Within a click of a button, the lyrics to that song will start appearing on our 16x2 LCD display. You can attach this display on the air vents of your car and enjoy an accessible view of the currently playing song lyrics. With more songs queued, Caraoke will be ready to display the next set of lyrics automatically as one song progresses to the next. 


## How we built it
###Software
The core software was built using Python, utilizing Spotify's powerful API to get information on the song currently played by the user. Using this data, we would retrieve the lyrics using [Textyl.co](https://api.textyl.co/api/lyrics?q=query)'s API generator. The syncing is accomplished using an internal custom-built stopwatch that lets us predict the user's current timestamp. The rest is fulfilled by our hardware.

###Hardware
We used an Arduino Genuino 101 to power and communicate with our 16x2 Grove LCD-RGB Backlight display. Using Python's `Serial` package, we managed to transmit the required information through our computer ports, binding together the power of two programming languages.


## Challenges we ran into
From our research, we discovered that Spotify is the most-used streaming app in the world. This is where we decided to dive into what their API offers.
- Our first challenge was figuring out how to generate the lyrics of the currently played song, since Spotify does not provide this information. Using the same API they used would not be a cost-effective decision, but thankfully, we managed to find another API that accomplished exactly what we wanted it to do. 
- Another difficulty was trying to sync the lyrics per the current timestamp of the song, which was the core feature of our application. Since it was unrealistic to keep asking Spotify for the current song player's timestamp, we had to implement and maintain our own Timer in our program.

Our biggest challenge, however, was the hardware. None of us had prior experience in working with Arduino.
- The LCD screen we used to output the lyrics had some limitations. As it was a 16x2 display, we could only print out a maximum of 32 characters onto a screen, which made it difficult to present the lyrics seamlessly
- The Grove LCD's documentation had shown us that the I2C memory addresses were constant variables, which means that we could not associate the LCD screen to a certain address. This prohibits us from using two separate LCDs unless we were using two Arduino boards, which was not an optimal solution.


## Accomplishments that we're proud of
Our team was proud to have completed our project the way we desired it to be and the way we visualized it in our thought process. We managed to learn a lot of various packages within Python and figured out a way to communicate our software with Arduino code. 

But despite our accomplishments, there is still a lot of room for improvement.


## What we learned
We got a lot more understanding of the concept of APIs and how to efficiently read the documentation to maximize the functions of our application. And we learned about Arduino, a lot about it, from scratch.


## What's next for Caraoke - Lyrics on the Go!
Currently, Caraoke cannot function independently without a wired connection to a computer that holds our code. In the future, we hope to implement an infrastructure to support Bluetooth connection such that the Arduino platform can function as a standalone. Furthermore, we plan to create an interface where users can personalize the digital display, such as accessibility features, to make it an even more powerful Karaoke platform. 
