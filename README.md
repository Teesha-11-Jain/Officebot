-> Following is just a prototype!
# Problem Statement
To solve the issues arising from modern-day lifestyle with remote working culture, mental wellness, and physical fitness.

# Problem identification
Striking a work-life balance is no easy feat, particularly if you work lengthy shifts. Work can seep into your personal time because to technology that allows you to stay connected all the time. The 'imbalance' of work life has become a source of worry over time. Tasks are frequently completed by one person, and there may be more effort involved than normal. 

Many employees end up overworking, which can decrease productive over time. Remote employment has been shown to result in fewer sick days, longer working hours. 

Being in an unequal or unbalanced position can lead to overworked and tight muscles in the neck, shoulders, and arms, as well as discomfort.
Staring at screens all day might disrupt sleep patterns and lead to insomnia. 


Disconnection from superiors, coworkers, and projects can lead to concerns about performance and job security.

Lack of physical exercises.

Lack of communication leads to blunders and misunderstood responsibilities. Employees' capacity to interact has been hampered, and they have been unable to communicate with their coworkers,which has had a negative impact on their mental health.

# Office Bot
Although organizations are increasingly taking steps to guarantee their employees' health, with so many employees working remotely, it's difficult for them to identify which individuals are having difficulties, which is where AI chatbots may help. Developing an AI-based chatbot to assure employees' well-being and increase productivity has been a success. 
Office bot is a chatbot powered by artificial intelligence with machine learning capabilities that is a colleague's best friend. It looks after an employee's well-being in all parts of their life, including job, relationships, and health. According to a research conducted by Workplace Intelligence, employees feel AI is better than people at delivering help.

It can be integrated into a company's work environment, whether it's in-office or remote.

Communication with bot will seems like the one with a real person.

The bot will function during office hours and assist employees with difficulties such as anxiety, physical discomfort, and so on.

It's a friend for employees who looks after their health, social life, mental health, productivity, and more.

The bot has three key features that is “Thrive Socially, Thrive Mentally and Thrive Physically”.

# Thrive Socially
Thrive socially is a component of the bot that looks after an employee's social life and awareness. People were unable to socialize, particularly during remote work, which harmed their connections with their coworkers and disrupted their mental health. The bot delivers the following functions in order to promote and sustain a person's social well-being:

Company updates: news regarding all company events and latest policies. 
Volunteer, Campaigns and fundraise : updates regarding company’s campaigns and fundraising events. 
Partnerships : updates regarding recent partnerships of the company with any organization or social workers.  
News : news on topics such as entrepreneurs, sports, weather, entertainment, protest etc. Generated from news API.
Projects: updates and conversation about projects.
Organization’s updates are provided by fetching data from a data set regularly updated by the company.

# Thrive Mentally
Depression, bipolar affective disorder, schizophrenia and other psychoses, dementia, intellectual disabilities, and developmental disorders such as autism present in a variety of ways, including altered thoughts, perceptions, emotions, behavior, and interpersonal relationships. The bot helps in identifying these symptoms and help them out.

Mental health awareness: bot provides articles related to mental health awareness using web scrapping and Wikipedia API.
Disorder Tests: Bot will ask certain questions to tests one’s level of mental disorder such as anxiety or depression etc. Later it suggests exercises or refer to a therapist if needed.
Timely break: Bot schedules timely breaks to avoid mental fatigue. Bot suggests some exercises to relieve mental pressure.
Limit to overtime: Bot shuts down the software after the office time ends, so that employee and employers can prevent overtime. 

Tests and  results are provided by inbuilt data sets. Time breaks are scheduled by Python Scheduler.

# Thrive Physically
Research has proven that long hours of desk work increase health hazards like obesity, hypertension, diabetes, raised cholesterol and osteoarthritis. The continuous sitting required with a desk job poses a constant threat of chronic back, neck and arm pain in addition to lethal conditions of congestive heart failure and stroke. The bot help the staff to keep doing physical exercises and maintain a balanced diet.

Exercise: After every hour, schedule 10-15 minutes of physical activity.
Nutrition: A daily diet chart is provided by the bot.
Musculoskeletal Health: Physical activity recommendations for any strain or muscle discomfort.
Thrive physical events: Information about any upcoming physical events in the area.
Wellbeing education: educating about wellbeing of an individual and how to stay healthy.
Timely breaks and water reminders: Bot organizes pauses and offers workouts, as well as reminds to drink water so as to stay hydrated.

Time breaks are scheduled by Python Scheduler. Exercises are provided by datasets. Diet chart is given by calculating BMR of the individual and suggests meals of the day.

# Implementation
Office bot is an AI based bot  that rely on Artificial Intelligence(AI) & Machine Learning(MI) technologies to converse with users.

Used python to develop the bot.
Nltk and Tensorflow for the construction of the model.
Rasa NLU: Handles the Natural Language Processing and train the bot
RASA Core: Handles data storing, piping, API, and basically the Assistant
Data: The context, learning, and improvement help with the files existing in the data folder.
stories.md: This file contains the conversational flow of the chatbot and the user.
News API: https://newsapi.org/
Weather information.: https://openweathermap.org/
PySimpleGUI: Chatbot GUI
Python Scheduler: to schedule tasks.
Django: for web scrapping

# Made using RASA Framework
RASA is an open-source framework used to Build contextual AI assistants and chatbots in text and voice with open source machine learning framework.

