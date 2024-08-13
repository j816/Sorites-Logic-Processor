import sys

class LogicProcessor:
    def __init__(self):
        self.connectors = {'and', 'or', 'implies', 'not'}

    def clean_tokens(self, tokens):
        return [token for token in tokens if token not in ['of', 'the', 'a', 'an']]

    def tokenize(self, statement):
        tokens = statement.lower().split()
        tokens = self.clean_tokens(tokens)
        return tokens

    def parse_statement(self, tokens):
        if 'and' in tokens or 'or' in tokens:
            connector = 'and' if 'and' in tokens else 'or'
            split_index = tokens.index(connector)
            left_tokens = tokens[:split_index]
            right_tokens = tokens[split_index + 1:]
            return (connector, self.parse_statement(left_tokens), self.parse_statement(right_tokens))
        elif 'implies' in tokens:
            split_index = tokens.index('implies')
            left_tokens = tokens[:split_index]
            right_tokens = tokens[split_index + 1:]
            return ('implies', self.parse_statement(left_tokens), self.parse_statement(right_tokens))
        else:
            # Base case: simple statement
            if len(tokens) == 3:  # Example: "dogs are mammals"
                subject, verb, predicate = tokens
                return (subject, verb, predicate)
            elif len(tokens) == 4 and tokens[1] == 'are':  # Example: "dogs and cats are mammals"
                subject1, _, subject2, predicate = tokens
                return ('and', (subject1, 'is', predicate), (subject2, 'is', predicate))
            return tuple(tokens)

    def evaluate_tree(self, tree):
        if isinstance(tree, tuple) and len(tree) == 3:
            operator, left, right = tree
            if operator == 'and':
                return f"({self.evaluate_tree(left)}) and ({self.evaluate_tree(right)})"
            elif operator == 'or':
                return f"({self.evaluate_tree(left)}) or ({self.evaluate_tree(right)})"
            elif operator == 'implies':
                return f"(implies {self.evaluate_tree(left)} {self.evaluate_tree(right)})"
            else:
                return f"({operator} {left} {right})"
        elif isinstance(tree, tuple) and len(tree) == 2:
            subject, predicate = tree
            return f"{subject} is {predicate}"
        else:
            return " ".join(tree)

    def validate_premise(self, premise):
        tokens = self.tokenize(premise)
        tree = self.parse_statement(tokens)
        logic = self.evaluate_tree(tree)
        if logic:
            print(f"[INFO] Validated premise: '{premise}' -> {logic}")
            return logic
        else:
            print(f"[ERROR] Invalid premise: '{premise}' - Failed to parse.")
            return None

    def validate_argument(self, premises, conclusion=None):
        print(f"Validating premises and conclusion:")
        for idx, premise in enumerate(premises):
            print(f"Validating premise {idx + 1}: {premise}")
            valid_premise = self.validate_premise(premise)
            if valid_premise is None:
                print(f"[ERROR] Failed to validate premise {idx + 1}: '{premise}'")
                return f"Error in premises parsing at premise {idx + 1}: '{premise}'"

        if conclusion:
            print(f"Validating conclusion: {conclusion}")
            valid_conclusion = self.validate_premise(conclusion)
            if valid_conclusion:
                return f"Conclusion is valid: {conclusion}"
            else:
                return f"Invalid conclusion: {conclusion}"
        return "All premises are valid."

    def load_sorites_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file.readlines() if line.strip()]
            return lines
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Lpremise.py <sorites_file.txt>")
        sys.exit(1)

    file_path = sys.argv[1]
    processor = LogicProcessor()
    premises = processor.load_sorites_from_file(file_path)

    if premises:
        result = processor.validate_argument(premises)
        print(result)
