import stopclock
import sorter
import generator
import finder
import argparse

#setup argparser
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--range", required=True, help="Number-Range in the Array")
ap.add_argument("-l", "--length", required=True, help="Length of the Array")
ap.add_argument("-s", "--search", required=True, help="Number to Search")
args = vars(ap.parse_args())

# Setup Classes
clock = stopclock.StopClock()
bubble_s = sorter.BubbleSorter()
insert_s = sorter.InsertionSorter()
select_s = sorter.SelectionSorter()
bucket_s =sorter.BucketSort()
generator = generator.RandomArrayGenerator()
finder = finder.RecursiveFinder()

# Generate Array with Random Numbers
arr = generator.gen_array(int(args["range"]), int(args["length"]))

#Sort Arrays and Take
clock.start_clock()
sorted_1 = bubble_s.sort(arr.copy())
clock.stop_clock("BubbleSort")

clock.start_clock()
sorted_2 = insert_s.sort(arr.copy())
clock.stop_clock("Insertion Sort")

clock.start_clock()
sorted_3 = select_s.sort(arr.copy())
clock.stop_clock("Selection Sort")

clock.start_clock()
sorted_4 = bucket_s.sort(arr.copy())
clock.stop_clock("Bucket Sort")

#Zahl finden
found = finder.find(sorted_4, int(args["search"]), 0, len(sorted_4))
print("The Element {}: ".format(args["search"]), found)
