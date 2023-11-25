import json
import openai
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

openai.api_key= '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'


def lambda_handler(event, context):
    
    #body = json.loads(event['body'])
    model = int(event['model'])
    text = event['text']
    MCQ = event['MCQ']
    Single_word = event['Single_word']
    Fill_blank = event['Fill_blank']
    Descriptive = event['Descriptive']
    Difficulty = event['Difficulty']
    
    
    if model == 0:
        options = 'number of multiple choise questions = ' + str(MCQ) + ' ,number of single word answer type questions = ' +str(Single_word) + ' ,number of fill in the blank type questions = ' + str(Fill_blank) + ' ,number of descriptive type questions = ' + str(Descriptive) + ', and the difficulty level is = ' + str(Difficulty)
        input = f"""
You are asked to Generate different types of questions from the given text delimited by triple backticks.

Types of question to be generated are Multiple choice questions, Single word answer type, Fill in the blank type, and descriptive type.
In addition to the text, you will also be provided with options like below

1. Number of questions to be generated from each type.
2. Difficulty level of questions = Easy, Intermediate, Advanced.
The options are given as text delimited by triple quotes.

Provide them in four different JSON objects with keys like below:
Multiple choice questions = question number, question, option1, option2, option3, option4, right answer.
Single word answer type questions = question number, question, right answer.
Fill in the blank type questions = question number, question, right answer.
Descriptive type questions = question_number, question, right answer.

```{text}```
\"\"\"{options}\"\"\"
"""
        messages = [{"role": "user", "content": input}]
        logger.info("Calling OpenAI API")
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)
        logger.info("Completed calling")
        reply = chat.choices[0].message.content
        logger.info("response : "+ reply)
    
    
    
    elif model == 1:
        options = 'number of multiple choise questions = ' + str(MCQ) + ' ,number of single word answer type questions = ' +str(Single_word) + ' ,number of fill in the blank type questions = ' + str(Fill_blank) + ' ,number of descriptive type questions = ' + str(Descriptive) + ', and the difficulty level is = ' + str(Difficulty)
        input = f"""
You are asked to generate different types of questions from a given category of mathematics delimited by triple backticks.

Types of question to be generated are Multiple choice questions, Single word answer type, Fill in the blank type, and descriptive type.
In addition to the text, you will also be provided with options like below

1. Number of questions to be generated from each type.
2. Difficulty level of questions = Easy, Intermediate, Advanced.
The options are given as text delimited by triple quotes.

Provide them in JSON format with the following keys:
question number, question, option_1, option_2, option_3, option_4, right_answer_option_number, steps to solve.

```{text}```
\"\"\"{options}\"\"\"

"""
        messages = [{"role": "user", "content": input}]
        logger.info("Calling OpenAI API")
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)
        logger.info("Completed calling")
        reply = chat.choices[0].message.content
        logger.info("response : "+ reply)
    
    
    return {
   	 'statusCode': 200,
   	 'headers': {
   		 'Content-Type': 'application/json'
   	 },
   	 'body': json.dumps(reply) 
    }

