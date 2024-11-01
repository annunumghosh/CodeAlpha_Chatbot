from nltk.chat.util import Chat, reflections 

pairs =[ 
	['my name is (.*)', ['Hello ! % 1']], 
	['(hi|hello|hey|namaste|hola)', ['Hey there !', 'Hi there !', 'Hey !']], 
	['(.*) your name ?', ['My name is roasty bot']], 
	['(.*) do you do ?', ['Right now i can only answer fews ques!']], 
	['(.*) created you ?', ['Annunum Ghosh created me using python and NLTK']] 
] 

chat = Chat(pairs, reflections) 
chat.converse() 
