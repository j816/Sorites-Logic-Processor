# Sorites-Logic-Processor

## Overview

`LogicProcessor` is a powerful Python application designed to process, parse, and validate complex logical statements (sorites). The program reads a text file containing logical premises, constructs logical trees for each premise, and validates the logical consistency of the statements. It supports compound subjects, nested logical structures, and mixed logical connectors, making it a versatile tool for logical reasoning tasks.

## Features

- **Flexible Input Handling**: Process logical premises from a text file, handling complex sentence structures, compound subjects, and nested logic.
- **Dynamic Logical Parsing**: Construct logical trees dynamically, allowing for the evaluation of varied logical forms without the need for preset logical templates.
- **Comprehensive Validation**: Validate the logical consistency of a series of premises, with detailed output on each step of the validation process.
- **Error Handling**: Gracefully handles errors in logical structures, providing clear feedback and suggestions for potential corrections.

## Installation

### Prerequisites

- Python 3.x
- Recommended: A virtual environment to manage dependencies

### Steps

1. **Clone the Repository** 

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv lo-env
   source lo-env/bin/activate  # On Windows, use `lo-env\Scripts\activate`
   ```

3. **Install Dependencies**:
   The `LogicProcessor` script is self-contained and does not require external dependencies beyond Python's standard library. Simply ensure you're running Python 3.x.

## Usage

### Command Line Usage

The `LogicProcessor` is designed to be used from the command line, where you can pass a text file containing your logical premises as an argument.

**Basic Usage**:
```bash
python Lpremise.py <sorites_file.txt>
```

**Example**:
```bash
python Lpremise.py complex_sorites.txt
```

### Input File Structure

- **Plain Text**: Each line in the text file should contain a single logical premise.
- **No Special Formatting**: Avoid numbering, bullet points, or special characters that aren't part of the logical statement.
- **Compound and Complex Statements**: The processor can handle complex statements, including compound subjects and nested logical operations, as long as they are formatted correctly.

**Example Input File**:
```plaintext
All artists and poets are creators.
Some creators are dreamers.
None of the dreamers are realists.
All realists and scientists are logical.
Some logical individuals are skeptics.
None of the skeptics are believers.
```

### Detailed Output

The program provides detailed output for each premise, including:
- **Validation Status**: Whether the premise was successfully parsed and validated.
- **Logical Tree Evaluation**: The evaluated logical expression for each premise.
- **Error Messages**: Clear and descriptive error messages if the premise fails to parse or validate.

### Example Output

```plaintext
Validating premises and conclusion:
Validating premise 1: All artists and poets are creators.
[INFO] Validated premise: 'All artists and poets are creators.' -> (artists are creators) and (poets are creators)
Validating premise 2: Some creators are dreamers.
[INFO] Validated premise: 'Some creators are dreamers.' -> (creators are dreamers)
...
All premises are valid.
```

### Error Handling

If the `LogicProcessor` encounters an error (e.g., a premise that it cannot parse or validate), it will output an error message explaining the issue and, where possible, suggest a way to correct the input.

**Example Error**:
```plaintext
[ERROR] Invalid premise: 'Some text that doesn't make sense' - Failed to parse.
[SUGGESTION] Consider restructuring the statement to match known logical forms.
```

#### Sorites Test Set 1
1. **Sorite 1**: All artists and poets are creators. Some creators are dreamers. None of the dreamers are realists. All realists and scientists are logical. Some logical individuals are skeptics. None of the skeptics are believers.

2. **Sorite 2**: All historians and archaeologists are scholars. Some scholars are writers. None of the writers are plagiarists. All plagiarists and liars are deceivers. Some deceivers are successful. None of the successful individuals are unknown.

3. **Sorite 3**: All mathematicians and logicians are precise. Some precise people are engineers. None of the engineers are careless. All careless people and procrastinators are inefficient. Some inefficient workers are unemployed. None of the unemployed are wealthy.

4. **Sorite 4**: All philosophers and ethicists are thinkers. Some thinkers are idealists. None of the idealists are pragmatists. All pragmatists and realists are practical. Some practical people are inventors. None of the inventors are ordinary.

5. **Sorite 5**: All musicians and composers are artists. Some artists are visionaries. None of the visionaries are conformists. All conformists and followers are traditional. Some traditionalists are conservatives. None of the conservatives are radicals.

6. **Sorite 6**: All leaders and innovators are pioneers. Some pioneers are risk-takers. None of the risk-takers are cautious. All cautious people and planners are methodical. Some methodical individuals are perfectionists. None of the perfectionists are careless.

7. **Sorite 7**: All educators and mentors are guides. Some guides are counselors. None of the counselors are judges. All judges and arbiters are impartial. Some impartial individuals are mediators. None of the mediators are biased.

8. **Sorite 8**: All activists and reformers are advocates. Some advocates are lawyers. None of the lawyers are criminals. All criminals and wrongdoers are punished. Some punished individuals are innocent. None of the innocent are guilty.

9. **Sorite 9**: All scientists and researchers are inquisitive. Some inquisitive minds are curious. None of the curious are indifferent. All indifferent people and apathetic individuals are uninvolved. Some uninvolved individuals are bystanders. None of the bystanders are active participants.

10. **Sorite 10**: All doctors and nurses are healers. Some healers are compassionate. None of the compassionate are indifferent. All indifferent people and apathetic individuals are uninvolved. Some uninvolved individuals are bystanders. None of the bystanders are active participants.

11. **Sorite 11**: All travelers and explorers are adventurers. Some adventurers are brave. None of the brave are fearful. All fearful people and cowards are timid. Some timid people are introverts. None of the introverts are extroverts.

12. **Sorite 12**: All authors and poets are wordsmiths. Some wordsmiths are eloquent. None of the eloquent are inarticulate. All inarticulate people and mumblers are misunderstood. Some misunderstood individuals are lonely. None of the lonely are surrounded.

13. **Sorite 13**: All athletes and competitors are disciplined. Some disciplined people are dedicated. None of the dedicated are lazy. All lazy people and slackers are unmotivated. Some unmotivated individuals are apathetic. None of the apathetic are passionate.

14. **Sorite 14**: All artists and sculptors are creative. Some creative minds are innovative. None of the innovative are conventional. All conventional people and traditionalists are conservative. Some conservatives are cautious. None of the cautious are impulsive.

15. **Sorite 15**: All strategists and tacticians are planners. Some planners are visionaries. None of the visionaries are short-sighted. All short-sighted people and near-sighted individuals are limited. Some limited thinkers are constrained. None of the constrained are free.

#### Sorites Test Set 2

All mathematicians and physicists are scientists.

Some scientists are philosophers.

None of the philosophers are artists.

All artists and musicians are creative individuals.

Some creative individuals are entrepreneurs.

None of the entrepreneurs are followers.

Some followers are leaders.

All leaders are influential.

None of the influential are unnoticed.

Some unnoticed are ordinary.

All ordinary are common.

None of the common are unique.

Some unique are rare.

All rare things are valuable.

None of the valuable things are discarded.

Some discarded things are broken.

All broken things are useless.

None of the useless are desired.

Some desired things are unattainable.

All unattainable things are dreams.

None of the dreams are realities.

Some realities are harsh.

All harsh truths are painful.

None of the painful experiences are forgotten.

Some forgotten things are memories.

All memories are cherished.

None of the cherished things are insignificant.

Some insignificant things are overlooked.

All overlooked details are critical.

None of the critical details are trivial.

Some trivial matters are ignored.

All ignored warnings are dangerous.

None of the dangerous paths are safe.

Some safe paths are secure.

All secure locations are fortified.

None of the fortified places are vulnerable.

Some vulnerable spots are weak.

All weak points are exploited.

None of the exploited resources are renewable.

Some renewable resources are sustainable.

All sustainable practices are beneficial.

None of the beneficial actions are harmful.

Some harmful behaviors are addictive.

All addictive substances are controlled.

None of the controlled substances are legal.

Some legal products are regulated.

All regulated industries are monitored.

None of the monitored activities are secret.

Some secret operations are confidential.

All confidential information is restricted.

