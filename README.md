<a id="readme-top"></a>

<h1 align='center'>Whispered Wishes :sparkles:</h1> 

<div align='center'>

<img src='\images\Twilio_Text_Reminder.PNG' alt='Picture of the Whispered Wishes event reminder application sending a personalized text reminders for birthdays, anniversaries, and other special events using Twilio.'>

<p align='center'>Whispered Wishes is a Python-based event reminder application that sends personalized SMS reminders for birthdays, anniversaries, and other special events using Twilio. The goal is to help you stay connected to your loved ones by sending you reminders to celebrate their special moments.<br/>

<a href='https://github.com/AmberForrester/Whispered_Wishes'><strong>Source Code »</strong></a>
<br />
<br />
<a href='https://github.com/AmberForrester/Whispered_Wishes/issues/new?assignees=&labels=bug&projects=&template=bug-report-%F0%9F%90%9E.md'>Report Bug</a>
.
<a href='https://github.com/AmberForrester/Whispered_Wishes/issues/new?assignees=&labels=enhancement&projects=&template=feature-request-%F0%9F%9A%80.md'>Request Feature</a>
</p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-this-project">About This Project</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#running-the-game">Running The Game</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
<br />



## About This Project
<p align='center'>Whispered Wishes is more than just a reminder app — it's your personal memory whisperer, designed to make sure you never miss a chance to celebrate the people who matter most. Powered by the magic of Twilio, Whispered Wishes sends you gentle nudges to connect with your loved ones on their special days, like birthdays, anniversaries, or any moment worth celebrating. But it doesn't stop there! This app goes beyond the basics, prompting you with heartwarming memories and inside jokes to make each message you send even more meaningful.</p>

<p align='center'>No more scrambling to remember dates or last-minute generic texts Whispered Wishes has got you covered. Whether it's a spontaneous note to a friend or a heartfelt message to a family member, this project helps you make those connections truly unforgettable. With effortless setup and seamless automation, you're just a few clicks away from becoming the friend or family member who never forgets. Ready to turn everyday moments into cherished memories? Let Whispered Wishes do the whispering, while you enjoy the smiles!</p>
<br />
A good understanding of Python and Pygame would be beneficial to helping you create this project. However, it is always good practice to refer to the Documentation available when developing ***any*** project. 

_Please refer to the [Python Documentation](https://docs.python.org/3/) for your reference._

_The standard shell of Python, or REPL (Read-Eval-Print Loop) allows you to run Python code interactively as you work on a project or are in the process of learning this programming language. You may find it useful to vist the [Getting the Most Out of the Python Standard REPL website](https://realpython.com/python-repl/) to further your understanding and produce better results._

<p align="right">(<a href="#readme-top">top of page</a>)</p>


## Features
- Automated SMS reminders for special events like birthdays and anniversaries.
- Seamless integration with Twilio for sending text messages.
- Easy-to-manage contact list with personalized memories.
- Graceful error handling for incomplete or incorrectly formatted data.
<br/>


## Installation

### Prerequisites
- Python >= 3.8
- Twilio Account to send SMS (Free Trial Available)
- Virtual Environment (Optional but recommended.)



### Step-by-Step Instructions

1. **Clone the Repository**
  ```bash
  git clone https://github.com/yourusername/Whispered_Wishes.git
  cd Whispered_Wishes
  ```

2. **Set up a Virtual Environment** (Optional but recommended.)
  ```bash
  python -m venv venv
  .\venv\Scripts\Activate
  ```

3. **Install Required Dependencies after activating the Virtual Environment** 

Navigate to the project directory and install the dependencies:
  ```bash
  pip install -r requirements.txt
  ```

<p align="right">(<a href="#readme-top">top of page</a>)</p>



### Project Structure

![Project Structure](/images/WW_Structure.png)

<p align="right">(<a href="#readme-top">top of page</a>)</p>



### Set Up Twilio

1. **Create a Twilio Account**
  - Sign up for free at [Twilio](https://www.twilio.com/en-us) and log in.
  - Get your **Account SID, Auth Token,** and a **Twilio Phone Number.**

2. **Create the `.env` file**
  - In the project's root directory, create a new file named `.env`.
  - Add the following lines to the `.env` file with your Twilio credentials:
  ```env
  TWILIO_ACCOUNT_SID=your_account_sid_here
  TWILIO_AUTH_TOKEN=your_auth_token_here
  TWILIO_PHONE_NUMBER=your_twilio_number_here
  MY_PHONE_NUMBER=your_personal_phone_number_here
  ```

3. **Add `.env` to `.gitignore`**

To ensure your sensitive information does not get committed to version control:
  - Open (or create) the `.gitignore` file in the root directory.
  - Add the following line to the file:
```
.env
venv/
```
> [!CAUTION]
> This step will prevent the `.env` file from being tracked by Git and keep your sensitive credentials secure.

<p align="right">(<a href="#readme-top">top of page</a>)</p>








### Contributing

I have learned that contributions are the heart of what makes the open source community such an amazing place! We are constantly able to learn, grow, inspire eachother, and create incredible things. Any contributions you make are **greatly appreciated**, we are so lucky to be here together.

If you have a suggestion that would make this project better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please, don't forget to give the project a :star:! 

I appreciate you!

<p align="right">(<a href="#readme-top">top of page</a>)</p>



### License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">top of page</a>)</p>



### Acknowledgments

Please take some time to check out the links below! I found value in each and every one of them while creating this project, so my hope is that you will to!

* [Creating Tetris in Python with pygame](https://youtu.be/nF_crEtmpBo?si=SvdgSXpcOYEvCOl0) - Special thank you to _Programming With Nick_ for the tutorial!
* [More Music by Spyros](https://assetstore.unity.com/) - Game Sounds 
* [Best README Template](https://github.com/othneildrew/Best-README-Template)
* [Basic Syntax: Markdown Guide](https://www.markdownguide.org/basic-syntax/#reference-style-links)
* [Formatting Syntax: GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#animal-bug)

<p align="right">(<a href="#readme-top">top of page</a>)</p>