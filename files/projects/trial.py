from quiz_data import capitals
import random



# 1. Create 35 differnt quizzes
for quizNum in range(35):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyfile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz:
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the state
    states = list(capitals.keys())
    random.shuffle(states)



# Loop through all 50 states, making a question for each.
for quesNum in range(50):

    # Get right and wrong answer
    correct_answer = capitals[states[quesNum]]
    wrong_answers = list(capitals.values())
    del wrong_answers[wrong_answers.index(correct_answer)]
    wrong_answers = random.sample(wrong_answers, 3)
    answer_options = wrong_answers + [correct_answer]
    random.shuffle(answer_options)

    # write the  qusetion ans the answer options to the quiz file

    quizFile.write('%s. What is the capital of %s?\n' %(quesNum + 1, states[quesNum]))
    for i in range(4):
        quizFile.write('    %s. %s\n' % ('ABCD'[i], answer_options[i]))
        quizFile.write('\n')
    
    # write the answer key to the file
    answerKeyfile.write('%s. %s\n' % (quesNum + 1, 'ABCD'[answer_options.index(correct_answer)]))

quizFile.close()
answerKeyfile.close()