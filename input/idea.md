# Advertisment

Yes we kanji - The app that helps you memorizing japanese kanjis ! 

- More than 2000 kanjis
- Prononciation support
- Translation in 10 languages
- Customize your exercises, define your objectives and track your progress


# Summary

I want ot build an app to help people learning japanese ! Unlike European languages, japanese is hard to learn because of the kanjis, where you have to memorize the kanjis visually and phonetically. Among the existing apps, I noticed that everyone has different learning methods : some learn by heart, some have to listen and repeat, some have to see, some want to write. Every learning app is generic enough to allow everyone to join and to be bad for everyone. The app yeswekanji aims at closing this gap by propposing a flexible platform where everyone can customize its exercises, objectives and pace.

# The job right now

We will build a prototype containing 1 feature : generate a list of 10 kanjis card, with lexical field similarities. User just see the kanjis drawn on top of the cards. By clicking on it, the card flips and reveals the kanji + its writing in japanese using the latin alphabet + the translation in French + it reads both french version then japanese version orally. 

## Prerequistes

### A kanji database

Connect to a kanji database containing the drawing, the spelling in latin japanese, the translation in French, the phonetical information in both french and japanese. 

Prononciation; 2 options : either phonetical data read by a robot voice, or the word already stored as an audio file. 

If translation is missing, then we can connect to a tranlator and generate it (linguee, google trad)

### A hosting platform

Limited interraction makes it easier : only user input is a click. Got to find audio output. 
1) Can this be on streamlit ?
2) What other alternative, similar to streamlit, could you recommand ?
3) Otherwise, we can host an ovh serveur and publish. How long would this take a) setup the ovh serveur b) install and run the docker c) write the html page displayed d) exposing

## Decisions to take

Remember that we are building a prototype and the metric to minimize is time to deploy. Other long-term solution can be studied and kept for later.

### Kanji database

Which database to use ?
Which synthetic voice to use ?
Can we find phonetical data ?
Can we find translation or should we use translation services ?

### Host

What's the fastest path to deploying ?
Can we stay on streamlit ?
How can we allow to use audio ?


## Outputs

Create a repo and push it to my personal github yeswekanji (this is this folder). 
Create a documentation that you own doc/ folder, where you store information that you extrapolated from this project (track records, additional documents, etc...)
Answer the architectural decisions asked for the prototype. Store them in ADR/ folder.
Using the gh-task tool (documents/gh-planner or my personnal github, gh-task), create the tasks necessary to create this prototype. Be honest about the time it takes : an agent will probably do mmost of the work, so timeline is hours, not days. 
1 page report in doc/reports/ to summarize the work of this session. You can create more documents if you deem them important, they go in doc/notes/ and the main report can reference them, as well as ADRs. 
