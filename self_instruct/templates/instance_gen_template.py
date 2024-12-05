


output_first_template_for_clf = '''Given the classification task definition and the class labels, generate an input that corresponds to each of the class labels. If the task doesn't require input, just generate possible class labels.

Task: Classify the sentiment of the sentence into positive, negative, or mixed.
Class label: mixed
Sentence: I enjoy the flavor of the restaurant but their service is too slow.
Class label: positive
Sentence: I had a great day today. The weather was beautiful and I spent time with friends and family.
Class label: negative
Sentence: I was really disappointed by the latest superhero movie. I would not recommend it to anyone.

Task: Given a dialogue, classify whether the user is satisfied with the service. You should respond with "satisfied" or "unsatisfied".
Class label: satisfied
Dialogue:
Agent: Thank you for your feedback. We will work to improve our service in the future.
Customer: I am happy with the service you provided. Thank you for your help.
Class label: unsatisfied
Dialogue:
Agent: I am sorry we will cancel that order for you, and you will get a refund within 7 business days.
Customer: Oh that takes too long. I want you to take quicker action on this.

Task: Given a person's policy preferences, classify their likely political alignment as either progressive or conservative.
Class label: progressive
Opinion: I believe that universal access to healthcare should be a fundamental right.
Class label: conservative
Opinion: I support minimal government intervention in economic markets.

Task: Classify if the following email is promotional or non-promotional.
Class label: promotional
Email: Check out our amazing new sale! We've got discounts on all of your favorite products.
Class label: non-promotional
Email: We hope you are doing well. Let us know if you need any help.

Task: Classify if the forum post contains inappropriate content.
Class label: inappropriate
Post: [Example of inappropriate content removed for safety]
Class label: appropriate
Post: The best way to cook a steak on the grill is to preheat it to medium-high heat.

Task: Does the information in the document support the claim? Respond with "support" or "unsupport".
Class label: unsupport
Document: After a record-breaking run that saw mortgage rates plunge to all-time lows and home prices soar to new highs, the U.S. housing market finally is slowing. While demand and price gains are cooling, any correction is likely to be a modest one, housing economists and analysts say. No one expects price drops on the scale of the declines experienced during the Great Recession.
Claim: The US housing market is going to crash soon.
Class label: support
Document: The U.S. housing market is showing signs of strain, with home sales and prices slowing in many areas. Mortgage rates have risen sharply in recent months, and the number of homes for sale is increasing. This could be the beginning of a larger downturn, with some economists predicting a potential housing crash in the near future.
Claim: The US housing market is going to crash soon.

Task: Answer the following multiple-choice question. Select A, B, C, or D.
Class label: C
Question: What is the capital of Germany?
A) London
B) Paris
C) Berlin
D) Rome
Class label: D
Question: What is the largest planet in our solar system?
A) Earth
B) Saturn
C) Mars
D) Jupiter
Class label: A
Question: What is the process by which plants make their own food?
A) Photosynthesis
B) Fermentation
C) Digestion
D) Metabolism
Class label: B
Question: Who wrote the novel "The Great Gatsby"?
A) Ernest Hemingway
B) F. Scott Fitzgerald
C) J.D. Salinger
D) Mark Twain

Task: Detect if there is a syntax error in the provided code. Output "true" if there is an error, output "false" if there is not.
Class label: true
Code:
def quick_sort(arr):
    if len(arr) < 2
        return arr
Class label: false
Code:
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

Task: Identify all categories that this news article belongs to from the following options: sports, politics, technology, entertainment. Output categories separated by commas.
Class label: sports
Article: The Golden State Warriors have won the NBA championship for the second year in a row.
Class label: politics
Article: The United States has announced new environmental regulations.
Class label: politics,sports
Article: The government has proposed increased funding for Olympic training programs.

Task: Given credit card information, classify whether the cardholder is at risk of default.
Class label: at-risk
Credit card statement: Large purchases at luxury retailers.
Spending habits: Frequent high-end purchases exceeding income.
Account balance: Over credit limit, three missed payments.
Class label: not-at-risk
Credit card statement: Regular purchases at grocery stores and utilities.
Spending habits: Consistent essential expenses within budget.
Account balance: 30% of credit limit, no missed payments.

Task: Classify if a social media post is relevant to the given topic.
Class label: relevant
Post: I can't believe the government is still not taking action on climate change. It's time for us to take matters into our own hands.
Hashtags: #climatechange #actnow
Topic: Climate change
Class label: not-relevant
Post: I just bought the new iPhone and it is amazing!
Hashtags: #apple #technology
Topic: Travel

Task: Answer 'yes' if the sentence explicitly answers the question, otherwise answer 'no'.
Class label: yes
Sentence: Jack played basketball for an hour after school.
Question: How long did Jack play basketball?
Class label: no
Sentence: The leaders of the Department of Homeland Security now appear before 88 committees.
Question: How often are they required to appear?

Task: Name the second largest city by population in Canada.
Class label: montreal

Task: Classify the type of mathematical equation.
Class label: linear
Equation: y = 2x + 5
Class label: quadratic
Equation: y = x^2 - 4x + 3

Task: Identify the first number in the given list.
Class label: 1
List: 1, 2, 3, 4, 5

Task: '''

input_first_template_for_gen = '''Come up with examples for the following tasks. Try to generate multiple examples when possible. If the task doesn't require additional input, you can generate the output directly.

Task: Which exercises are best for reducing belly fat at home?
Output:
- Lying Leg Raises
- Leg In And Out
- Plank
- Side Plank
- Sit-ups

Task: Extract all the country names in the paragraph, list them separated by commas.
Example 1
Paragraph: Dr. No is the sixth novel by the English author Ian Fleming to feature his British Secret Service agent James Bond. Written at Fleming's Goldeneye estate in Jamaica, it was first published in United Kingdom by Jonathan Cape in 1958. In the novel Bond looks into the disappearance in Jamaica of two fellow MI6 operatives who had been investigating Doctor No. Bond travels to No's Caribbean island and meets Honeychile Rider, who is there to collect shells. They are captured and taken to a luxurious facility carved into a mountain. The character of Doctor No, the son of a German missionary and a Chinese woman, was influenced by Sax Rohmer's Fu Manchu stories. Dr. No was the first of Fleming's novels to face widespread negative reviews in Britain, but it was received more favorably in United States.
Output: England, Britain, Jamaica, United Kingdom, Germany, China, United States

Task: Converting 85°F to Celsius.
Output: 85°F = 29.44°C

Task: Sort the given list ascendingly. 
Example 1
List: [10, 92, 2, 5, -4, 92, 5, 101]
Output: [-4, 2, 5, 5, 10, 92, 92, 101]
Example 2
List: [9.99, 10, -5, -1000, 5e6, 999]
Output: [-1000, -5, 9.99, 10, 999, 5e6]

Task: Suggest a better and more professional rephrasing of the following sentence.
Example 1
Sentence: This house is surprisingly not constructed very well, and you probably need more money to fix it after you buy it. If you ask me, I would suggest you to consider other candidates.
Output: Based on the construction quality, additional renovation costs may be necessary after purchase. I recommend exploring other properties.
Example 2
Sentence: Just so you know, we did an experiment last week and found really surprising results - language model can improve itself!
Output: Our experiments last week yielded remarkable results, demonstrating that the language model exhibits self-improvement capabilities.

Task: Read the following paragraph and answer a math question about the paragraph. You need to write out the calculation for getting the final answer.
Example 1
Paragraph: Gun violence in the United States results in tens of thousands of deaths and injuries annually, and was the leading cause of death for children 19 and younger in 2020. In 2018, the most recent year for which data are available as of 2021, the Centers for Disease Control and Prevention's (CDC) National Center for Health Statistics reports 38,390 deaths by firearm, of which 24,432 were by suicide. The rate of firearm deaths per 100,000 people rose from 10.3 per 100,000 in 1999 to 12 per 100,000 in 2017, with 109 people dying per day or about 14,542 homicides in total, being 11.9 per 100,000 in 2018. In 2010, there were 19,392 firearm-related suicides, and 11,078 firearm-related homicides in the U.S. In 2010, 358 murders were reported involving a rifle while 6,009 were reported involving a handgun; another 1,939 were reported with an unspecified type of firearm. In 2011, a total of 478,400 fatal and nonfatal violent crimes were committed with a firearm.
Question: How many more firearm-related deaths were there in 2018 compared to 2010?
Output:
```text
2018 total deaths: 38,390
2010 total deaths: 19,392 + 11,078 = 30,470
Difference: 38,390 - 30,470 = 7,920
Therefore, there were 7,920 more deaths by firearm in 2018 than in 2010.
```

Task: Write Python code to solve this leetcode problem.
Example 1
Problem: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Output:
```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
```

Task: Solve the equation and find the value of X. Show your steps.
Example 1
Equation: 10X + 5 = 10
Output:
```text
10X + 5 = 10
10X = 10 - 5
10X = 5
X = 5/10
X = 0.5
```

Example 2
Equation: X + Y + 120 = 100
Output:
```text
X + Y + 120 = 100
X + Y = 100 - 120
X + Y = -20
X = -20 - Y
```

Task: Write a program to compute the sum of integers from k to n.
Output:
```python
def sum_range(k: int, n: int) -> int:
    return sum(range(k, n + 1))
```

Task: Select the oldest person from the given list.
Example 1
List: George Washington, Confucius, Michael Jordan, Michelangelo
Output: Confucius
Example 2
List: Alan Turing, Geoffrey Hinton, Yann LeCun, Yoshua Bengio
Output: Alan Turing

Task: Turn down a job offer by sending an email to a recruiter explaining the reason.
Output:
```text
Dear [Recruiter],

Thank you for the generous offer to join your team. I've greatly admired [Company Name] and its products over the years. However, after careful consideration of my career goals, I've decided to accept a position with another organization.

I would appreciate staying connected and have followed you on LinkedIn. Thank you again for your time and consideration throughout the interview process.

Best regards,
[Your Name]
```

Task:'''
