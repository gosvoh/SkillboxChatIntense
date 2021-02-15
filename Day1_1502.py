#!/usr/bin/env python
# coding: utf-8

# In[154]:


import random
import nltk


# In[93]:


BOT_CONFIG = {
    'intents': {

        'hello': {
            'examples': ['Привет', 'Добрый день', 'Шалом', 'Привет, бот'],
            'responses': ['Привет, человек!', 'И вам здравствуйте :)', 'Доброго времени суток']
        },
        'bye': {
            'examples': ['Пока', 'Досвидания', 'До свидания', 'До скорой встречи'],
            'responses': ['Еще увидимся', 'Если что, я всегда тут']
        },
        'name': {
            'examples': ['Как тебя зовут?', 'Скажи свое имя', 'Представься'],
            'responses': ['Меня зовут Саша']
        },

    },

    'failure_phrases': [
        'Непонятно. Перефразируйте, пожалуйста.',
        'Я еще только учусь. Спросите что-нибудь другое',
        'Слишком сложный вопрос для меня.',
    ]
}


# In[143]:


def clear_phrase(phrase):
    phrase = phrase.lower()

    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя- '
    result = ''.join(symbol for symbol in phrase if symbol in alphabet)

#     result = ''
#     for symbol in phrase:
#         if symbol in alphabet:
#             result += symbol

    return result


# In[165]:


def classify_intent(replica):
    # TODO use ML!
    
    replica = clear_phrase(replica)

    for intent, intent_data in BOT_CONFIG['intents'].items():
        for example in intent_data['examples']:
            example = clear_phrase(example)

            distance = nltk.edit_distance(replica, example)
            if distance / len(example) < 0.4:
                return intent


# In[122]:


def get_answer_by_intent(intent):
    if intent in BOT_CONFIG['intents']:
        responses = BOT_CONFIG['intents'][intent]['responses']
        return random.choice(responses)


# In[123]:


def generate_answer(replica):
    # TODO на 3й день
    return


# In[124]:


def get_failure_phrase():
    failure_phrases = BOT_CONFIG['failure_phrases']
    return random.choice(failure_phrases)


# In[125]:


def bot(replica):
    # NLU
    intent = classify_intent(replica)

    # Answer generation
    
    # выбор заготовленной реплики
    if intent:
        answer = get_answer_by_intent(intent)
        if answer:
            return answer

    # вызов генеративной модели
    answer = generate_answer(replica)
    if answer:
        return answer
    
    # берем заглушку
    return get_failure_phrase()


# In[164]:


print(bot('добрый вечер'))


# In[ ]:





# In[ ]:




