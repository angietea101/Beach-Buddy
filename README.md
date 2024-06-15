# Beach Buddy

Python Discord bot that displays CSULB course information. Get notifications when seats & sections open.

The data displayed by the bot updates every morning at 5:03 AM - 5:04 AM. This is when the CSULB schedule of classes updates. Currently, real time updates are only available to admins.

See Gallery below to see examples of bot usage.


## Gallery

**/search command:**
![image](https://github.com/angietea101/Beach-Buddy/assets/81064737/cde753b6-e292-42c6-b041-55db79e4662d)

**/search of CECS 329 in Fall 2024 with opened_only set to False**
![image](https://github.com/angietea101/Beach-Buddy/assets/81064737/4f3dc24e-0e1f-4853-9c69-05c8e0d836b6)

**Set channel to where notifications are sent:**
![image](https://github.com/angietea101/Beach-Buddy/assets/81064737/40a482f3-f1f3-4f49-920e-93ef03017cd7)

**Beach Buddy updating its' data on courses every morning:**
![alt text](image-3.png)


## Getting Started

### Prerequisites

* Python 3.11+

* All dependencies within `requirements.txt`

## Installation

**Windows**:

1. Download Python and set it to **PATH** during installation.
![alt text](python.png)
2. Clone this repository
3. Create a folder called `seasons`
4. Create a file called config.py in the project root folder
    * Do **NOT** create this file within the seasons folder
    * Set variable **BOT_TOKEN** to your bot's secret. See next section for directions on how to set up your own Discord bot
5. Create a `notif.txt`file
6. Download requirements using:
    ```sh
    pip install -r /path/to/requirements.txt
    ```
7. Run the `scrape_subjects.py` code to populate two csv files holding all course information inside of the seasons folder


### Discord Bot Setup

1. Visit the [Discord Developer Portal](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications) to create your Discord Bot
2. Select the applications tab, then click on `New Application`

![alt text](new_application.png)

3.  Choose a name, agree to the terms and services, then select `create`.
4. Go to the `Bot`tab and select the `Reset Token`button. Copy the token and paste it into your `config.py`file.

![alt text](image.png)

5. Ensure these permissions match.

![alt text](image-1.png)

6. Invite the Discord Bot to your server with the `administrator` box marked:

![alt text](image-2.png)


## Updating Beach Buddy
We don't provide release versions. To get the latest version, simply perform `git pull`.


## Authors


Angie Tran & Diego Cid


## License

This project is licensed under the MIT License - see the LICENSE.md file for details


## Acknowledgments

* README.md inspiration from [KOOKZ](https://github.com/KOOKIIEStudios/PalCON-Discord?tab=readme-ov-file)
