#Driving Test Evaluator
class TestError(Exception):
    pass

class CandidateAlreadyRegisteredError(TestError):
    def __init__(self, name):
        self.name = name
        super().__init__(
            f"candidate already registered: {self.name}"
        )

class CandidateNotRegisteredError(TestError):
    def __init__(self, name):
        self.name = name
        super().__init__(
            f"candidate not registered: {self.name}")

class InvalidQuestionError(TestError):
    def __init__(self, question_num, valid_options):
        self.question_num = question_num
        self.valid_options = valid_options
        super().__init__(
            f"invalid question number {question_num}. valid questions: {valid_options}"
        )

class DrivingTestEvaluator:
    def __init__(self, answer_sheet):
        self.answer_sheet = answer_sheet
        self.submissions = {}
    
    def register_candidate(self, name):
        if name in self.submissions:
            raise CandidateAlreadyRegisteredError(name)
        self.submissions[name] = {} #{question_num: answer}
    
    def submit_answer(self, name, question_num, answer):
        try:
            candidate_answers = self.submissions[name]
        except KeyError:
            raise CandidateNotRegisteredError(name) from None
        
        if question_num not in self.answer_sheet:
            raise InvalidQuestionError(question_num,list(self.answer_sheet.keys()))
        candidate_answers[question_num] = answer
       
    def evaluate(self, name):
        try:
            candidate_answers = self.submissions[name]
        except KeyError:
            raise CandidateNotRegisteredError(name) from None
        
        if len(candidate_answers) == 0:
            return 0
        
        correct_answers = 0

        for q_num, ans in candidate_answers.items():
            if self.answer_sheet[q_num] == ans:
                correct_answers += 1
        total_questions = len(self.answer_sheet)
    
        score = int(correct_answers / total_questions * 100)
        return score
    
sheet = {1: "C", 2: "A", 3: "B", 4: "D", 5: "A"}
evaluator = DrivingTestEvaluator(sheet)

evaluator.register_candidate("Amir")
evaluator.register_candidate("Lola")

evaluator.submit_answer("Amir", 1, "C")
evaluator.submit_answer("Amir", 2, "A")
evaluator.submit_answer("Amir", 3, "B")
evaluator.submit_answer("Amir", 4, "D")
evaluator.submit_answer("Amir", 5, "A")

evaluator.submit_answer("Lola", 1, "C")
evaluator.submit_answer("Lola", 2, "B")
evaluator.submit_answer("Lola", 3, "A")

print(f"Amir: {evaluator.evaluate('Amir')}%")
print(f"Lola: {evaluator.evaluate('Lola')}%")

tests = [
    lambda: evaluator.register_candidate("Amir"),
    lambda: evaluator.submit_answer("Kamol", 1, "A"),
    lambda: evaluator.submit_answer("Lola", 9, "B"),
]

for test in tests:
    try:
        test()
    except TestError as e:
        print(e)
