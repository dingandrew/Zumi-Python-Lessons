import ipywidgets as widgets
import sys
from IPython.display import display
from IPython.display import clear_output

def create_multipleChoice_widget(description, options, correct_answer):
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        disabled = False
    )
    
    description_out = widgets.Output()
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            s = '\x1b[6;30;42m' + "Correct!" + '\x1b[0m' +"\n" #green color
        else:
            s = '\x1b[5;30;41m' + "Wrong. " + '\x1b[0m' +"\n" #red color
        with feedback_out:
            clear_output()
            print(s)
        return
    
    check = widgets.Button(description="submit")
    check.on_click(check_selection)
    
    
    return widgets.VBox([description_out, alternativ, check, feedback_out])


def quiz_one():
    Q1 = create_multipleChoice_widget('Which is an incorrect variable initialization?',['speed = 20','name = "Hello"','new_var'],'new_var')
    Q2 = create_multipleChoice_widget('Once a varible is assigned it cannot be changed.',['TRUE','FALSE'],'FALSE')
    Q3 = create_multipleChoice_widget('Which are valid variable names?',['speed1','1','port-1'],'speed1')

    display(Q1)
    display(Q2)
    display(Q3)
    
    
def quiz_three():
    Q1 = create_multipleChoice_widget('Can I use spaces and tabs to indent lines in one program?',['YES','NO'],'NO')
    Q2 = create_multipleChoice_widget('What type of error will I get if i make an indentation error',['IndentationError: unexpected indent', 'TypeError: invalid datatypes'],'IndentationError: unexpected indent')

    display(Q1)
    display(Q2)

