from random import randint, shuffle
import time, sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from threading import Thread

def swap(list, pos1, pos2):  # Swaps items inside of an array
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

def end_sort(start_time):
    end = time. time()
    print("--- %s seconds ---" % (round(time.time() - start_time, 2)))
    sys.exit()

def bubblesort(arr):
    swapped = True
    start = time. time()
    for i in range(len(arr)):
        if not swapped: end_sort(start)
        swapped = False
        
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr = swap(arr, j, j+1)
                swapped = True
            yield arr # Genreator object

finished = False
  
  
def visualize(): 
    N = 100
    A = list(range(1, N + 1)) 
    shuffle(A) 

    generator = bubblesort(A) 


    fig, ax = plt.subplots() 
    ax.set_title("Bubble Sort") 
    bar_sub = ax.bar(range(len(A)), A, align="edge") 
      
    ax.set_xlim(0, N) 
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes) 
    iteration = [0] 
      

    def update(A, rects, iteration):
        global finished
        if not finished:
            for rect, val in zip(rects, A): 
                rect.set_height(val) 
            iteration[0] += 1
            text.set_text(f"Operations: {iteration[0]}")
        else:
            text.set_text(f"Finished with {iteration[0]} iterations")
  

    anim = animation.FuncAnimation( 
        fig, 
        func=update, 
        fargs=(bar_sub, iteration), 
        frames=generator, 
        repeat=True, 
        blit=False, 
        interval=15,
        save_count=90000, 
    ) 
      
    # for showing the animation on screen 
    plt.show() 
    plt.close() 
  
  
if __name__ == "__main__": 
    visualize()

