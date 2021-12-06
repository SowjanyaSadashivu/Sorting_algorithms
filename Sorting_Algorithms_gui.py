from tkinter import *
from tkinter import ttk
import Sorting_algorithms as sa
from datetime import datetime as dt
import matplotlib.pyplot as plt
import random

s = sa.sorting_algorithms() 

root = Tk()
root.title('Sorting Algorithms')
root.config(bg = '#fffaea')


def algorithms():
    _sortingalg = selected_alg.get()
    _number = int(number.get())   
    _elements = list(elements.get().strip().split(' '))
    _elements = [int(i) for i in _elements]    
    if len(_elements) == _number:        
        if _sortingalg == 'Heap sort':
            sorted_list = s.heap_sort(_elements)
        if _sortingalg == 'Merge sort':
            sorted_list = s.merge_sort(_elements)
        if _sortingalg == 'Bubble sort':
            sorted_list = s.bubble_sort(_elements)
        if _sortingalg == 'Insertion sort':
            sorted_list = s.insertion_sort(_elements)
        if _sortingalg == 'Selection sort':
            sorted_list = s.selection_sort(_elements)
        if _sortingalg == 'Quick sort median':
            sorted_list = s.quick_sort_median(_elements)
        if _sortingalg == 'Quick sort regular':
            s.quick_sort_regular(_elements) 
            sorted_list = _elements       
    else:
        Label(UI_frame, text="no of elements is not equal to elemets entered", bg = 'mistyrose', fg = "red").grid(row=4, column = 1, padx = 5, pady = 5)  
        Label(UI_frame, text="Please re-enter the elements ", bg = 'mistyrose', fg = "red").grid(row=5, column = 1)     
        
    end_time = dt.now()
    average_time = end_time - start_time    
    sorted_list = [int(i) for i in sorted_list]    
    Label(UI_frame, text = "Sorted List of elements ", bg = 'mistyrose').grid(row = 6, column = 0, padx = 5, pady = 5)
    Label(UI_frame, text = sorted_list , bg = 'mistyrose', font=("Bernard", 12)).grid(row = 6, column = 1)
    Label(UI_frame, text = "Average run time ", bg = 'mistyrose').grid(row = 7, column = 0, padx = 5, pady = 5)
    Label(UI_frame, text = average_time, bg = 'mistyrose', font=("Bernard", 12)).grid(row = 7, column = 1)


def update_plot(_elements, rec, epochs):
    for rec, val in zip(rec, _elements):
        rec.set_height(val)
    epochs[0]+= 1
    text.set_text("No.of operations :{}".format(epochs[0]))

avr_time = []
def metrics():  
    _elements = list(elements.get().strip().split(' '))
    _elements = [int(i) for i in _elements]         
    sort_alg_list = ["heap_sort", "merge_sort", "bubble_sort", "insertion_sort", "selection_sort", "quick_sort_median", "quick_sort_regular"]
    for i in range(len(sort_alg_list)):
        if sort_alg_list[i] == "heap_sort":
            sorted_list = s.heap_sort(_elements)
        if sort_alg_list[i] == "merge_sort":
            sorted_list = s.merge_sort(_elements)
        if sort_alg_list[i] == "bubble_sort":
            sorted_list = s.bubble_sort(_elements)
        if sort_alg_list[i] == "insertion_sort":
            sorted_list = s.insertion_sort(_elements)
        if sort_alg_list[i] == "selection_sort":
            sorted_list = s.selection_sort(_elements)
        if sort_alg_list[i] == "quick_sort_median":
            sorted_list = s.quick_sort_median(_elements)
        if sort_alg_list[i] == "quick_sort_regular":
            sorted_list = s.quick_sort_regular(_elements)        
        
        end_time_all = dt.now()
        avg_time = end_time_all - start_time_all         
        avg_time = avg_time.total_seconds()
        avr_time.append(avg_time)      
    plt.figure()
    plt.title('Comparion of Sorting Algorithm runtime', pad = 10)
    plt.plot(sort_alg_list, avr_time, marker = 'd', color = 'red')
    plt.xlabel('Sorting Algorithms')
    plt.ylabel('Time in milliseconds')
    plt.xticks(rotation=45)
    plt.show()

random_generator = 0
n_number_value = 10
n_number = range(1000, 6000, 1000)
list_alg = {
    "n_number_value":[],
    "merge_sort" : [],
    "heap_sort" : [],
    "merge_sort" : [],
    "quick_sort_reguar": [],
    "quick_sort_median" : [],
    "insertion_sort" : [],
    "selection_sort" : [],
    "bubble_sort" : [],
}
def avgcase(size, algo):
    array = [ random.randint(0, size) for i in range(size) ]
    startTime = dt.now()
    if algo == "merge_sort":
        sortAlgorithm = s.merge_sort(array)
    if algo == "heap_sort":
        sortAlgorithm = s.heap_sort(array)
    if algo == "quick_sort_reguar":
        sortAlgorithm = s.quick_sort_regular(array)
    if algo == "quick_sort_median":
        sortAlgorithm = s.quick_sort_median(array)
    if algo == "insertion_sort":
        sortAlgorithm = s.insertion_sort(array)
    if algo == "selection_sort":
        sortAlgorithm = s.selection_sort(array)
    if algo == "bubble_sort":
        sortAlgorithm = s.bubble_sort(array)
  
    endTime = dt.now()
    average = endTime - startTime
    average = average.total_seconds() * 1000
    return average


def cal_avg_case():
    for n in n_number:
        list_alg['n_number_value'].append(n)
        average = avgcase(n , algo = "merge_sort")
        list_alg['merge_sort'].append(average)
        average = avgcase(n , algo = "heap_sort")
        list_alg['heap_sort'].append(average)
        average = avgcase(n , algo = "quick_sort_reguar")
        list_alg['quick_sort_reguar'].append(average)
        average = avgcase(n , algo = "quick_sort_median")
        list_alg['quick_sort_median'].append(average)
        average = avgcase(n , algo = "insertion_sort")
        list_alg['insertion_sort'].append(average)
        average = avgcase(n , algo = "selection_sort")
        list_alg['selection_sort'].append(average)
        average = avgcase(n , algo = "bubble_sort")
        list_alg['bubble_sort'].append(average)

def garphs():
    cal_avg_case()   
    plt.figure()
    plt.title('Comparion of Sorting Algorithm on N inputs', pad = 10)
    plt.plot(list_alg['n_number_value'], list_alg['bubble_sort'], color = 'red', label = "Bubble_sort")
    plt.plot(list_alg['n_number_value'], list_alg['heap_sort'], color = 'orange', label = "Heap_sort")
    plt.plot(list_alg['n_number_value'], list_alg['merge_sort'], color = 'brown', label = "Merge_sort")
    plt.plot(list_alg['n_number_value'], list_alg['quick_sort_reguar'], color = 'cyan', label = "Quick_regular_sort")
    plt.plot(list_alg['n_number_value'], list_alg['quick_sort_median'], color = 'magenta', label = "Quick_median_sort")
    plt.plot(list_alg['n_number_value'], list_alg['selection_sort'], color = 'purple', label = "Selection_sort")
    plt.plot(list_alg['n_number_value'], list_alg['insertion_sort'], color = 'blue', label = "Insertion_sort")
    plt.xlabel('Size of elements')
    plt.xticks(rotation=45)
    plt.ylabel('run time in milliseconds')
    plt.legend()
    plt.show()
   
selected_alg = StringVar()
sort_alg = [
    'Heap sort',  
    'Merge sort',
    'Bubble sort',
    'Insertion sort',
    'Selection sort',
    'Quick sort median',
    'Quick sort regular'
]

UI_frame = Frame(root, width = 600, height = 200, bg = 'mistyrose' )
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

Label(UI_frame, text = "Enter the number of elements ", bg = 'mistyrose').grid(row=0, padx = 5, pady = 5)
number = Entry(UI_frame, width = 30)
number.grid(row=0, column=1, padx = 5, pady = 5)


Label(UI_frame, text = "Enter the elements",  bg = 'mistyrose' ).grid(row=1, padx = 5, pady = 5)
elements = Entry(UI_frame, width = 30)
elements.grid(row=1, column=1, padx = 5, pady = 5)


Label(UI_frame, text = "Choose the Sorting Algorithm :", bg = 'mistyrose').grid(row = 2, column = 0, padx = 5, pady = 5)
ttk.OptionMenu(UI_frame, selected_alg, "Heap sort",  *sort_alg).grid(row=2, column=1, padx = 5, pady = 5)

Button(UI_frame, text = 'Sort the elements', command = algorithms).grid(row = 3, column = 1, padx = 5, pady = 5)
start_time = dt.now()

Button(UI_frame, text = 'show algo comparision', command = metrics).grid(row = 8, column = 0, padx = 5, pady = 5)
start_time_all =  dt.now()
Button(UI_frame, text = 'show algo N value comparision', command = garphs).grid(row = 8, column = 1, padx = 5, pady = 5)
root.mainloop()