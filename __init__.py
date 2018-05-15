from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from random import randint
import re
__author__ = "HellCatVN"

class RandomSkill(MycroftSkill):
    def __init__(self):
        super(RandomSkill, self).__init__(name="RandomSkill")
    @intent_handler(IntentBuilder("").require("RandomKeyword"))
    def handle_random_intent(self, message):
        utterance=message.data.get('utterance')
        keyword_search = re.search('random ?([0-9]*) from (?P<From>[0-9]*) to (?P<To>[0-9]*)', utterance, re.IGNORECASE)
        random_array = []
        if(keyword_search.group(1) != ''):
            while (len(random_array)< int(keyword_search.group(1))):
                random_array.append(randint(int(keyword_search.group(2)),int(keyword_search.group(3))))
                print(random_array)
                random_array = list(set(random_array))
                print(random_array)
            random_string = ''
            self.speak_dialog("multi.random.res", data={"time": keyword_search.group(1)})
            for i in random_array:
                self.speak(str(i))
        else:
            random_number=randint(int(keyword_search.group(2)),int(keyword_search.group(3)))
            self.speak_dialog("single.random.res", data={"number": random_number})
def create_skill():
    return RandomSkill()
