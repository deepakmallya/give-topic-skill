from mycroft import MycroftSkill, intent_file_handler


class GiveTopic(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('topic.give.intent')
    def handle_topic_give(self, message):
        self.speak_dialog('topic.give')


def create_skill():
    return GiveTopic()

