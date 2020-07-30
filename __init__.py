from mycroft import MycroftSkill
from mycroft.skills import skill_api_method


class SkillApiSource(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.__name__ = 'skill-api-source-skill'
    
    def initialize(self):
        self.log.info('~~~~~~~~ loaded')
        self.log.info(skill_api_method)

    @skill_api_method
    def speak_from_other_skill(self, message):
        self.speak_dialog('source.api.skill')


def create_skill():
    return SkillApiSource()

