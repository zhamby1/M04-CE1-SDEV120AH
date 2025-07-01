# Python Conditionals

## What Are Conditionals?

Conditionals allow you to make decisions within a program.  The follow the following if structure

- if this thing is true - the code executes
- if not (false) - the code does not execute

We use relational operators in Python to compare two values

### Relational Operators (Ignore the '' )

- '>' - greater than
- '>=' - great than or equal to
- '<' - less than
- '<=' - less than or equal to
- '==' - equal to
- '!=' - not equal to

## Single Alternative or If Statement
Python executes an if statement by using the keyword if, then the conditions, then it is followed by a colon.  Then all of the code you wish to execute if that if statement is true, is indented under the if statement

To indent (done automatically by VsCode), press the tab key

```python
if age >= 18:
    print("You can vote")
```
Python groups statements by indentation.  This is really important.  If you do not indent the code under the if statement, then it will not execute when the if statement evaluates to true.

## Dual Alternative
An if-else block of code does similar things to a single if statement, but has an alternative if the condition results in a false.

An else MUST have an if statement to correspond to.  In other words, you cannot have an else without an if.

You can, however, have an if without an else (single alternative)

The else statement just has an else: with all the indented code under it executing when the condition evaluates to false.  There is no else condition, because you are saying 'anything else do the following'

```python
if age >= 18:
    print("You can vote")
else:
    print("You can NOT vote")
```

The else should maintain the same indentation level as it's corresponding if statement.

