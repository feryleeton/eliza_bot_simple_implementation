import re
import logging

logging.basicConfig(filename='chatlog.log', encoding='utf-8', level=logging.DEBUG)


class Eliza:

    def msg_probability(self, user_msg, recognized_words, single_response=False, required_words=[]):
        msg_certainty = 0
        has_required_words = True

        for word in user_msg:
            if word in recognized_words:
                msg_certainty = msg_certainty + 1

        percentage = float(msg_certainty) / float(len(recognized_words))

        for word in required_words:
            if word not in user_msg:
                has_required_words = False
                break

        if has_required_words or single_response:
            return int(percentage * 100)
        else:
            return 0

    def check_all_msgs(self, message):
        highest_prob_list = {}

        def response(bot_response, list_of_words, single_response=False, required_words=[]):
            nonlocal highest_prob_list
            highest_prob_list[bot_response] = self.msg_probability(message, list_of_words, single_response, required_words)

        response('Hello', ['hello', 'hi', 'sup'], single_response=True)
        response('Of course I am not, how about you?', ['are', 'you', 'bot'], required_words=['you', 'bot'])
        response('How cute and i love you', ['i', 'love', 'you', 'eliza'], required_words=['love', 'you'])

        best_match = max(highest_prob_list, key=highest_prob_list.get)
        if highest_prob_list[best_match] > 0:
            logging.info(f"Input: {message} \nOutput: {best_match} \nProbability: {highest_prob_list[best_match]}\n")
            return best_match
        else:
            logging.warning(f"Input: {message} \nAnswer not found\n")
            return 'Sorry I didn not understand you'

    def get_response(self, user_input):
        words_list = re.split(r'\s+|[,;&!.-]\s*', user_input.lower())
        response = self.check_all_msgs(words_list)
        return response

    def start_dialog(self):
        while True:
            print(f"Bot: {self.get_response(input('You: '))}")