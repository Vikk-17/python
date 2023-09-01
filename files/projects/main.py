from quiz_data import capitals
import random

# 1. Create the quiz and ans key files

for quizNumber in range(35):
    quiz_file = open(f'capitalsquiz{quizNumber + 1}.txt', 'w')
    answer_file = open(f'capitalsanswer{quizNumber + 1}.txt', 'w')

    # write the header for the files
    quiz_file.write(
        'Name:\n\n'
        'Date:\n\n'
        'Period:\n\n'
    )
    quiz_file.write(
        (' ' * 20) + f'State Capital Quiz (Form{quizNumber + 1})'
    )
    quiz_file.write('\n\n')

    # Shuffle the order of the state
    states = list(capitals.keys())
    random.shuffle(states)


# Loop through all 50 states, making a question for each

for question_number in range(50):

    # Get the right and wrong answers
    correct_answer = capitals[states[question_number]]
    wrong_answer = list(capitals.values())
    del wrong_answer[wrong_answer.index(correct_answer)]
    wrong_answer = random.sample(wrong_answer, 3)
    answer_options = wrong_answer + [correct_answer]
    random.shuffle(answer_options)

    # Write the question and answer options to the quiz file
    quiz_file.write(f'{question_number + 1}. what is the capital of {states[question_number]}')
    for i in range(4):
        quiz_file.write('    %s. %s\n' % ('ABCD'[i], answer_options[i]))
    quiz_file.write('\n')

    # Write the answer key to the file
    answer_file.write('%s. %s\n' % (question_number + 1, 'ABCD'[answer_options.index(correct_answer)]))

quiz_file.close()
answer_file.close()