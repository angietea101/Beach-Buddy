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
![image](https://github.com/angietea101/Beach-Buddy/assets/81064737/184474fc-13fe-4c67-b34e-6a148aa34ad1)


## Getting Started

### Prerequisites

* Python 3.11+

* All dependencies within `requirements.txt`

## Installation

**Windows**:

1. Download Python and set it to **PATH** during installation.
![python](https://github.com/angietea101/Beach-Buddy/assets/81064737/782aa3f0-852e-4b98-8780-d24630331fce)
2. Clone this repository
3. Create a folder called `seasons`
4. Create a file called `config.py` in the project root folder
    * Do **NOT** create this file within the seasons folder
    * Set variable **BOT_TOKEN** to your bot's token. See next section for directions on how to set up your own Discord bot.
5. Create a `notif.txt`file
6. Download requirements using:
    ```sh
    pip install -r /path/to/requirements.txt
    ```
7. Run the `scrape_subjects.py` code to populate two CSV files holding all course information. The CSV files will be located in the seasons folder.


### Discord Bot Setup

1. Visit the [Discord Developer Portal](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications) to create your Discord Bot
2. Select the applications tab, then click on `New Application`

![new_application](https://github.com/angietea101/Beach-Buddy/assets/81064737/febac2ce-99b8-4ca2-9715-05b5ace9c266)

3.  Choose a name, agree to the terms and services (only if you agree), then select `create`.
4. Go to the `Bot` tab and select the `Reset Token` button. Copy the token and paste it into your `config.py` file.

![image](https://github.com/angietea101/Beach-Buddy/assets/81064737/33f74719-635b-422f-85cc-75d13493cd99)

5. Ensure these permissions match.

![image-1](https://github.com/angietea101/Beach-Buddy/assets/81064737/d51faa34-a728-4d8d-ae51-3960441a7292)

6. Invite the Discord Bot to your server with the `administrator` box marked:

![image-2](https://github.com/angietea101/Beach-Buddy/assets/81064737/bbaa9b37-f569-4c9a-a1d9-6f521d00a45c)

## Updating Beach Buddy
We don't provide release versions. To get the latest version, simply perform `git pull`.


## Authors


Angie Tran & Diego Cid


## License

This project is licensed under the MIT License - see the LICENSE.md file for details


## Acknowledgments

* README.md inspiration from [KOOKZ](https://github.com/KOOKIIEStudios/PalCON-Discord?tab=readme-ov-file)
