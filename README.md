# Markov-chains-messanger
# Requirements
## Getting the data
Firstly you need to download your facebook conversations 
In order to do this on your facebok account go to:
`setting > Your Facebook Inormation > Download Your Information`
You only need to check the **messages** checkbox, other data is irrelevant
## Installing fbchat-archive-parser
This program uses extarnal module called fbchat-archive-parserto gather the data from messages
You can simply install it using pip
```
pip install fbchat-archive-parser

```
then you can also upgrade it
```
pip install fbchat-archive-parser
```
# Usage
Firstly you need to place the **learn.py** file in the **html** folder of the files that you downloaded
![](https://i.imgur.com/OIaT2wg.png)
then you run the program by typing
```
python learn.py <Name> <Surname>

```
There you enter the name and surname of the person from whose messages you fish the programm to learn

This by dafault should generate two fils
```
<name>.txt 

```
Where all the convesations from people with given name are stored,and
```
<name>_<surname>.json
```
Where the actual learned information are storred.
Next you have to make sure the json **file** is in the same direectory as the **generate.py** file
Then you can use the **generate.py** file like that:
```
python generate.py <length of message> <dictionary name>
```
Where dictionary name will be the json file generated by previous program
