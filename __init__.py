from mycroft import MycroftSkill, intent_file_handler


class SkillApiSource(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('source.api.skill.intent')
    def handle_source_api_skill(self, message):
        self.speak_dialog('source.api.skill')


def create_skill():
    return SkillApiSource()

